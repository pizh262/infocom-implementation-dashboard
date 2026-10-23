const projectContainer = document.getElementById("projects");
const projectSelect = document.getElementById("projectId");
const assigneeSelect = document.getElementById("assigneeId");
const taskContainer = document.getElementById("tasks");
const message = document.getElementById("message");

const projectLabels = {
    on_track: "В сроке",
    risk: "Есть риски",
    blocked: "Блокер"
};

const taskLabels = {
    todo: "К выполнению",
    in_progress: "В работе",
    done: "Выполнена",
    blocked: "Блокер"
};

async function api(url, options = {}) {
    const response = await fetch(url, {
        ...options,
        headers: {
            "Content-Type": "application/json",
            ...options.headers
        }
    });

    const data = await response.json();

    if (!response.ok) {
        throw new Error(data.error || "Ошибка запроса");
    }

    return data;
}

function showMessage(text, isError = false) {
    message.textContent = text;
    message.style.color = isError ? "#b91c1c" : "#166534";
}

async function loadProjects() {
    const projects = await api("/api/projects");

    projectContainer.replaceChildren();
    projectSelect.replaceChildren();

    for (const project of projects) {
        const card = document.createElement("article");
        card.className = `project-card ${project.status}`;

        const title = document.createElement("h3");
        title.textContent = project.name;

        const badge = document.createElement("span");
        badge.className = `badge ${project.status}`;
        badge.textContent = projectLabels[project.status];

        card.append(title, badge);
        projectContainer.append(card);

        const option = document.createElement("option");
        option.value = project.id;
        option.textContent = project.name;
        projectSelect.append(option);
    }
}

async function loadUsers() {
    const users = await api("/api/users");
    assigneeSelect.replaceChildren();

    for (const user of users) {
        const option = document.createElement("option");
        option.value = user.id;
        option.textContent = user.name;
        assigneeSelect.append(option);
    }
}

async function loadTasks() {
    const tasks = await api("/api/tasks");
    taskContainer.replaceChildren();

    for (const task of tasks) {
        const card = document.createElement("article");
        card.className = "task-card";

        const info = document.createElement("div");
        const title = document.createElement("h3");
        title.textContent = task.title;

        const details = document.createElement("p");
        details.textContent =
            `${task.project_name} · ${task.assignee_name} · ` +
            `Дедлайн: ${task.deadline}`;

        const status = document.createElement("p");
        status.textContent = `Статус: ${taskLabels[task.status]}`;

        info.append(title, details, status);

        const actions = document.createElement("div");
        actions.className = "task-actions";

        const select = document.createElement("select");

        for (const [value, label] of Object.entries(taskLabels)) {
            const option = document.createElement("option");
            option.value = value;
            option.textContent = label;
            option.selected = value === task.status;
            select.append(option);
        }

        const updateButton = document.createElement("button");
        updateButton.textContent = "Сохранить статус";
        updateButton.type = "button";

        updateButton.addEventListener("click", async () => {
            try {
                await api(`/api/tasks/${task.id}`, {
                    method: "PATCH",
                    body: JSON.stringify({ status: select.value })
                });
                showMessage("Статус задачи обновлён");
                await refresh();
            } catch (error) {
                showMessage(error.message, true);
            }
        });

        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Удалить";
      deleteButton.type = "button";

        deleteButton.addEventListener("click", async () => {
            if (!confirm("Удалить эту задачу?")) return;

            try {
                await api(`/api/tasks/${task.id}`, {
                    method: "DELETE"
                });
                showMessage("Задача удалена");
                await refresh();
            } catch (error) {
                showMessage(error.message, true);
            }
        });

        actions.append(select, updateButton, deleteButton);
        card.append(info, actions);
        taskContainer.append(card);
    }
}

async function refresh() {
    try {
        await loadProjects();
        await loadUsers();
        await loadTasks();
    } catch (error) {
        showMessage(error.message, true);
    }
}

document.getElementById("projectForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const name = document.getElementById("projectName").value.trim();

    try {
        await api("/api/projects", {
            method: "POST",
            body: JSON.stringify({ name })
        });

        event.target.reset();
        showMessage("Проект создан");
        await refresh();
    } catch (error) {
        showMessage(error.message, true);
    }
});

document.getElementById("taskForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const form = new FormData(event.target);
    const payload = {
        title: form.get("title").trim(),
        project_id: Number(form.get("project_id")),
        assignee_id: Number(form.get("assignee_id")),
        deadline: form.get("deadline"),
        status: form.get("status")
    };

    try {
        await api("/api/tasks", {
            method: "POST",
            body: JSON.stringify(payload)
        });

        event.target.reset();
        showMessage("Задача создана");
        await refresh();
    } catch (error) {
        showMessage(error.message, true);
    }
});

document.getElementById("refreshButton").addEventListener("click", refresh);

refresh();
