import os
import sqlite3
from datetime import date
from pathlib import Path

from flask import Flask, g, jsonify, render_template, request

app = Flask(__name__)

DATABASE = Path(
    os.environ.get("DATABASE_PATH", "projects.db")
)

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db

@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            assignee_id INTEGER NOT NULL,
            deadline TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'todo'
                CHECK (status IN ('todo', 'in_progress',
                                  'done', 'blocked')),
            FOREIGN KEY (project_id) REFERENCES projects(id),
            FOREIGN KEY (assignee_id) REFERENCES users(id)
        );
        """
    )

    user_count = db.execute(
        "SELECT COUNT(*) FROM users"
    ).fetchone()[0]

    if user_count == 0:
        db.executemany(
            "INSERT INTO users (name) VALUES (?)",
            [
                ("Анна Смирнова",),
                ("Иван Петров",),
                ("Мария Иванова",),
            ],
        )

    project_count = db.execute(
        "SELECT COUNT(*) FROM projects"
    ).fetchone()[0]

    if project_count == 0:
        db.executemany(
            "INSERT INTO projects (name) VALUES (?)",
            [
                ("Внедрение CRM",),
                ("Внедрение ERP",),
                ("Миграция данных",),
            ],
        )

    db.commit()

def calculate_project_status(project_id):
    db = get_db()

    tasks = db.execute(
        """
        SELECT deadline, status
        FROM tasks
        WHERE project_id = ?
        """,
        (project_id,),
    ).fetchall()

    # Блокер имеет более высокий приоритет.
    if any(task["status"] == "blocked" for task in tasks):
        return "blocked"

    today = date.today().isoformat()

    # Завершённые задачи не считаются просроченными.
    if any(
        task["status"] != "done"
        and task["deadline"] < today
        for task in tasks
    ):
        return "risk"

    return "on_track"

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/api/projects")
def get_projects():
    db = get_db()
    projects = db.execute(
        "SELECT id, name FROM projects ORDER BY id"
    ).fetchall()

    result = []
    for project in projects:
        result.append({
            "id": project["id"],
            "name": project["name"],
            "status": calculate_project_status(project["id"]),
        })

    return jsonify(result)

"/api/projects"
def create_project():
    data = request.get_json(silent=True) or {}
    name = data.get("name")

    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "Название проекта обязательно"}), 400

    db = get_db()
    cursor = db.execute(
        "INSERT INTO projects (name) VALUES (?)",
        (name.strip(),),
    )
    db.commit()

    return jsonify({
        "id": cursor.lastrowid,
        "name": name.strip(),
        "status": "on_track",
    }), 201

@app.get("/api/users")
def get_users():
    db = get_db()
    users = db.execute(
        "SELECT id, name FROM users ORDER BY name"
    ).fetchall()

    return jsonify([dict(user) for user in users])

@app.get("/api/tasks")
def get_tasks():
    db = get_db()
    tasks = db.execute(
        """
        SELECT t.id, t.project_id, p.name AS project_name,
        t.title, t.assignee_id, u.name AS assignee_name,
               t.deadline, t.status
        FROM tasks t
        JOIN projects p ON p.id = t.project_id
        JOIN users u ON u.id = t.assignee_id
        ORDER BY t.id DESC
        """
    ).fetchall()

    return jsonify([dict(task) for task in tasks])

"/api/tasks"
def create_task():
    data = request.get_json(silent=True) or {}

    title = data.get("title")
    deadline = data.get("deadline")
    project_id = data.get("project_id")
    assignee_id = data.get("assignee_id")
    status = data.get("status", "todo")

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "Название задачи обязательно"}), 400

    if not isinstance(deadline, str) or not deadline.strip():
        return jsonify({"error": "Дедлайн обязателен"}), 400

    try:
        date.fromisoformat(deadline)
        project_id = int(project_id)
        assignee_id = int(assignee_id)
    except (TypeError, ValueError):
        return jsonify({"error": "Некорректные данные"}), 400

    if status not in ("todo", "in_progress", "done", "blocked"):
        return jsonify({"error": "Некорректный статус"}), 400

    db = get_db()

    project = db.execute(
        "SELECT id FROM projects WHERE id = ?", (project_id,)
    ).fetchone()

    user = db.execute(
        "SELECT id FROM users WHERE id = ?", (assignee_id,)
    ).fetchone()

    if project is None:
        return jsonify({"error": "Проект не найден"}), 404

    if user is None:
        return jsonify({"error": "Исполнитель не найден"}), 404

    cursor = db.execute(
        """
        INSERT INTO tasks
            (project_id, title, assignee_id, deadline, status)
        VALUES (?, ?, ?, ?, ?)
        """,
        (project_id, title.strip(), assignee_id, deadline, status),
    )
    db.commit()

    return jsonify({
        "id": cursor.lastrowid,
        "project_id": project_id,
        "title": title.strip(),
        "assignee_id": assignee_id,
        "deadline": deadline,
        "status": status,
        "project_status": calculate_project_status(project_id),
    }), 201

@app.patch("/api/tasks/<int:task_id>")
def update_task(task_id):
    data = request.get_json(silent=True) or {}
    allowed = {"title", "deadline", "assignee_id", "status"}
    updates = {key: value for key, value in data.items()
               if key in allowed}

    if not updates:
        return jsonify({"error": "Нет данных для обновления"}), 400

    if "title" in updates:
        if not isinstance(updates["title"], str) or not updates["title"].strip():
            return jsonify({"error": "Название не может быть пустым"}), 400
        updates["title"] = updates["title"].strip()

    if "deadline" in updates:
        try:
            date.fromisoformat(updates["deadline"])
        except (TypeError, ValueError):
            return jsonify({"error": "Некорректный дедлайн"}), 400

    if "status" in updates and updates["status"] not in (
        "todo", "in_progress", "done", "blocked"
    ):
        return jsonify({"error": "Некорректный статус"}), 400

    db = get_db()
    task = db.execute(
        "SELECT id, project_id FROM tasks WHERE id = ?",
        (task_id,),
    ).fetchone()

    if task is None:
        return jsonify({"error": "Задача не найдена"}), 404

    if "assignee_id" in updates:
        try:
            updates["assignee_id"] = int(updates["assignee_id"])
        except (TypeError, ValueError):
            return jsonify({"error": "Некорректный исполнитель"}), 400

        user = db.execute(
            "SELECT id FROM users WHERE id = ?",
            (updates["assignee_id"],),
        ).fetchone()

        if user is None:
            return jsonify({"error": "Исполнитель не найден"}), 404

    assignments = ", ".join(
        f"{column} = ?" for column in updates
    )
    values = list(updates.values()) + [task_id]

    db.execute(
        f"UPDATE tasks SET {assignments} WHERE id = ?",
        values,
    )
    db.commit()

    return jsonify({
        "id": task_id,
        "project_id":
