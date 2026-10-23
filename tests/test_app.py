from datetime import date, timedelta

import pytest

import app as project_app

@pytest.fixture()
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(
        project_app,
        "DATABASE",
        tmp_path / "test_projects.db",
    )

    with project_app.app.app_context():
        project_app.init_db()

    project_app.app.config["TESTING"] = True

    with project_app.app.test_client() as test_client:
        yield test_client

def create_task(client, **overrides):
    payload = {
        "title": "Подготовить документацию",
        "project_id": 1,
        "assignee_id": 1,
        "deadline": (date.today() + timedelta(days=5)).isoformat(),
        "status": "todo",
    }
    payload.update(overrides)

    return client.post("/api/tasks", json=payload)

def test_get_projects(client):
    response = client.get("/api/projects")

    assert response.status_code == 200
    assert len(response.get_json()) >= 1

def test_create_task(client):
    response = create_task(client)

    assert response.status_code == 201
    assert response.get_json()["title"] == "Подготовить документацию"

def test_task_without_deadline_is_rejected(client):
    response = create_task(client, deadline="")

    assert response.status_code == 400

def test_blocker_changes_project_status(client):
    response = create_task(
        client,
        status="blocked",
    )

    assert response.status_code == 201

    status_response = client.get("/api/projects/1/status")

    assert status_response.status_code == 200
    assert status_response.get_json()["status"] == "blocked"

def test_overdue_task_changes_project_status(client):
    yesterday = (date.today() - timedelta(days=1)).isoformat()

    response = create_task(
        client,
        deadline=yesterday,
        status="in_progress",
    )

    assert response.status_code == 201

    status_response = client.get("/api/projects/1/status")

    assert status_response.status_code == 200
    assert status_response.get_json()["status"] == "risk"

def test_missing_project_returns_404(client):
    response = create_task(client, project_id=99999)

    assert response.status_code == 404
