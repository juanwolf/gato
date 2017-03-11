// Note that the path doesn't matter for routing; any WebSocket
// connection gets bumped over to WebSocket consumers
socket = new WebSocket("ws://" + window.location.host + "/chat/");

socket.onmessage = function(e) {
    var chatSection = document.getElementById("chat-section");
    var p = document.createElement('p');
    var node = document.createTextNode(e.data);
    p.appendChild(node);
    chatSection.appendChild(p);
};
// Call onopen directly if socket is already open
if (socket.readyState == WebSocket.OPEN) socket.onopen();

var sendButton = document.getElementById("send-button");
sendButton.onclick = function() {
    var textAreaValue = document.getElementById("textarea").value;
    socket.send(JSON.stringify({"username": "Bernard", "message": textAreaValue}));

};


