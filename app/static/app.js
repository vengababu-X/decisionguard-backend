const API_KEY = prompt("Enter Company API Key");

async function loadHistory() {
  const decisionId = document.getElementById("decisionId").value;
  const container = document.getElementById("results");

  container.innerHTML = "";

  if (!decisionId) {
    container.innerHTML = "<p>Please enter a decision ID</p>";
    return;
  }

  const response = await fetch(`/decision/${decisionId}/history`, {
    headers: {
      "x-api-key": API_KEY
    }
  });

  if (!response.ok) {
    container.innerHTML = "<p>Error fetching decision history</p>";
    return;
  }

  const history = await response.json();

  if (history.length === 0) {
    container.innerHTML = "<p>No history found</p>";
    return;
  }

  history.forEach(item => {
    const card = document.createElement("div");
    card.className = `card ${item.risk}`;

    card.innerHTML = `
      <strong>Risk:</strong> ${item.risk}<br/>
      <strong>Regret:</strong> ${item.regret}<br/>
      <strong>Chosen Cost:</strong> ${item.chosen_cost}<br/>
      <strong>Alternatives:</strong> ${item.alternatives}<br/>
      <small>${item.created_at}</small>
      <p>${item.explanation}</p>
    `;

    container.appendChild(card);
  });
}
