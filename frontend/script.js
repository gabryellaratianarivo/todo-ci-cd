const API = "http://localhost:5000/tasks";

async function loadTasks() {
  const res = await fetch(API);
  const tasks = await res.json();

  const list = document.getElementById("tasks");
  list.innerHTML = "";

  tasks.forEach(t => {
    const li = document.createElement("li");
    li.textContent = t.title;
    list.appendChild(li);
  });
}

async function addTask() {
  const input = document.getElementById("taskInput");

  if (!input.value) return;

  await fetch(API, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({title: input.value})
  });

  input.value = "";
  loadTasks();
}

loadTasks();
