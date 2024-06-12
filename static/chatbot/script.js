const chatLog = document.getElementById('chat-log');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');
const refreshButton = document.getElementById('refresh-button');
const backButton = document.getElementById('back-button');
const adminButton = document.getElementById('admin-button');
const buttonIcon = document.getElementById('button-icon');
const refreshIcon = document.getElementById('refresh-icon');

sendButton.addEventListener('click', sendMessage);
refreshButton.addEventListener('click', startNewSession);
backButton.addEventListener('click', goToMainPage);
adminButton.addEventListener('click', goToAdminPage);
userInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const message = userInput.value.trim();
    if (message === '') {
        return;
    }
    appendMessage('user', message);
    userInput.value = '';

    fetch('/chatbot/result/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ question: message, session_id: getSessionId() })
    })
        .then(response => response.json())
        .then(data => {
            appendMessage('bot', data.answer);
            buttonIcon.classList.add('fa-solid', 'fa-paper-plane');
            buttonIcon.classList.remove('fas', 'fa-spinner', 'fa-pulse');
        })
        .catch(error => {
            console.error('Error:', error);
            appendMessage('bot', 'Error: Check Your API Key!');
            buttonIcon.classList.add('fa-solid', 'fa-paper-plane');
            buttonIcon.classList.remove('fas', 'fa-spinner', 'fa-pulse');
        });

    buttonIcon.classList.remove('fa-solid', 'fa-paper-plane');
    buttonIcon.classList.add('fas', 'fa-spinner', 'fa-pulse');
}

function startNewSession() {
    fetch('/chatbot/new_session/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({})
    })
        .then(response => response.json())
        .then(data => {
            console.log('New session started:', data.session_id);
            // Clear the chat log
            chatLog.innerHTML = '';
            // Reset user input
            userInput.value = '';
            // Reset session ID cookie
            document.cookie = `sessionid=${data.session_id};path=/`;
        })
        .catch(error => {
            console.error('Error:', error);
        });

    refreshIcon.classList.add('fas', 'fa-spinner', 'fa-pulse');
    setTimeout(() => {
        refreshIcon.classList.remove('fas', 'fa-spinner', 'fa-pulse');
    }, 1000);
}

function goToMainPage() {
    window.location.href = '/';
}

function goToAdminPage() {
    window.location.href = '/admin/';
}

function appendMessage(sender, message) {
    const messageElement = document.createElement('div');
    const iconElement = document.createElement('div');
    const chatElement = document.createElement('div');
    const icon = document.createElement('i');

    chatElement.classList.add("chat-box");
    iconElement.classList.add("icon");
    messageElement.classList.add(sender);
    messageElement.innerText = message;

    if (sender === 'user') {
        icon.classList.add('fa-regular', 'fa-user');
        iconElement.setAttribute('id', 'user-icon');
    } else {
        icon.classList.add('fa-solid', 'fa-robot');
        iconElement.setAttribute('id', 'bot-icon');
    }

    iconElement.appendChild(icon);
    if (sender === 'user') {
        chatElement.appendChild(iconElement);
        chatElement.appendChild(messageElement);
    } else {
        chatElement.appendChild(messageElement);
        chatElement.appendChild(iconElement);
    }
    chatLog.appendChild(chatElement);
    chatLog.scrollTop = chatLog.scrollHeight;
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function getSessionId() {
    const sessionCookie = document.cookie.split('; ').find(row => row.startsWith('sessionid'));
    return sessionCookie ? sessionCookie.split('=')[1] : 'default-session-id';
}
