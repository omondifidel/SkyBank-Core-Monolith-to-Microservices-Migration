// This tells the frontend to look for the API on the same domain it's hosted on
const API_URL = "/api/v1"; //This is the GPS coordinate for your FASTAPI container.

async function updateDashboard() {
    try {
        const response = await fetch(`${API_URL}/balance`);
        const data = await response.json();
        document.getElementById('balance').innerText = `$${data.balance}`;
    } catch (error) {
        console.error("Failed to fetch balance:", error);
    }
}

async function makeTransfer() {
    const amount = document.getElementById('amount').value;
    const response = await fetch(`${API_URL}/transfer`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ recipient_id: 2, amount: parseFloat(amount) })
    });
    
    const result = await response.json();
    alert(result.message || result.error);
    updateDashboard(); // Refresh the numbers
}

// Load balance on startup
updateDashboard();