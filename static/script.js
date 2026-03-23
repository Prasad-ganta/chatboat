function handleKey(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}

async function sendMessage() {
    let input = document.getElementById("message");
    let chatbox = document.getElementById("chatbox");

    let message = input.value;

    if (!message) return;

    chatbox.innerHTML += `<div class="message user">${message}</div>`;
    input.value = "";

    chatbox.innerHTML += `<div class="message bot" id="typing">Typing...</div>`;
    chatbox.scrollTop = chatbox.scrollHeight;

    let response = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ message: message })
    });

    let data = await response.json();

    document.getElementById("typing").remove();

    chatbox.innerHTML += `<div class="message bot">${data.reply}</div>`;
    chatbox.scrollTop = chatbox.scrollHeight;
}