const API_KEY = prompt("Enter Company API Key");

async function loadDashboard() {
  const res = await fetch("/dashboard/summary", {
    headers: { "x-api-key": API_KEY }
  });

  if (!res.ok) return;

  const data = await res.json();
  document.getElementById("critical").innerText = data.critical;
  document.getElementById("medium").innerText = data.medium;
  document.getElementById("low").innerText = data.low;
}

async function loadHistory() {
  const decisionId = document.getElementById("decisionId").value;
  const container = document.getElementById("history");
  container.innerHTML = "";

  const res = await fetch(`/decision/${decisionId}/history`, {
    headers: { "x-api-key": API_KEY }
  });

  if (!res.ok) {
    container.innerHTML = "<p>Decision not found</p>";
    return;
  }

  const history = await res.json();

  history.forEach(h => {
    const div = document.createElement("div");
    div.className = `event ${h.risk}`;

    div.innerHTML = `
      <strong>${h.risk}</strong> · Regret ${h.regret}<br>
      <small>${h.created_at}</small>
      <p>${h.explanation}</p>
    `;

    container.appendChild(div);
  });
}

loadDashboard();
