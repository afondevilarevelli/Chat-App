const roomName = JSON.parse(document.getElementById('room-name').textContent);

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chats/'
    + roomName
    + '/'
);

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    document.querySelector('#chat-log').value += '- ' + (data.message + '\n');
};

chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-input-text').focus();
document.querySelector('#chat-input-text').onkeyup = function (e) {
    if (e.keyCode === 13) { // enter, return
        document.querySelector('#chat-input-btn').click();
    }
};

document.querySelector('#chat-input-btn').onclick = function (e) {
    const messageInputDom = document.querySelector('#chat-input-text');
    const message = messageInputDom.value;
    if(message == '')
        return
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
};