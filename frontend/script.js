const API = "http://127.0.0.1:5000/tasks";

const taskList = document.getElementById("taskList");

async function fetchTasks() {
  taskList.innerHTML = "";

  const res = await fetch(API);
  const tasks = await res.json();

  if (tasks.length === 0) {
    taskList.innerHTML = "<p>No tasks yet</p>";
    return;
  }

  tasks.forEach(task => {
    const li = document.createElement("li");

    li.innerHTML = `
      <b>${task.title}</b> - ${task.status}
      <br>${task.description || ""}
      <br>
      <button onclick="markComplete(${task.id})">Complete</button>
      <button onclick="deleteTask(${task.id})">Delete</button>
    `;

    taskList.appendChild(li);
  });
}

async function createTask() {
  const title = document.getElementById("title").value;
  const description = document.getElementById("description").value;

  if (!title) {
    alert("Title required");
    return;
  }

  await fetch(API, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, description })
  });

  fetchTasks();
}

async function markComplete(id) {
  await fetch(API + "/" + id, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ status: "completed" })
  });

  fetchTasks();
}

async function deleteTask(id) {
  await fetch(API + "/" + id, {
    method: "DELETE"
  });

  fetchTasks();
}

fetchTasks();
