#!/usr/bin/env python3
"""
ASGI WebSocket Server using Starlette
Serves HTTP and WebSocket connections
"""

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocket


async def homepage(request):
    """Serve HTML page at /"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>WebSocket Echo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
            }
            #messages {
                border: 1px solid #ccc;
                height: 300px;
                overflow-y: auto;
                padding: 10px;
                margin-bottom: 10px;
                background-color: #f9f9f9;
            }
            .message {
                margin: 5px 0;
                padding: 5px;
            }
            .sent {
                color: blue;
                text-align: right;
            }
            .received {
                color: green;
            }
            input, button {
                padding: 10px;
                font-size: 14px;
            }
            button {
                background-color: #4CAF50;
                color: white;
                border: none;
                cursor: pointer;
                border-radius: 4px;
            }
            button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <h1>WebSocket Echo Server</h1>
        <p>Connected: <span id="status">Connecting...</span></p>

        <div id="messages"></div>

        <input type="text" id="messageInput" placeholder="Type a message...">
        <button onclick="sendMessage()">Send</button>

        <script>
            const messagesDiv = document.getElementById('messages');
            const statusSpan = document.getElementById('status');
            const input = document.getElementById('messageInput');

            const ws = new WebSocket('ws://localhost:8000/ws');

            ws.onopen = function() {
                statusSpan.textContent = 'Connected ✓';
                statusSpan.style.color = 'green';
            };

            ws.onmessage = function(event) {
                const message = document.createElement('div');
                message.className = 'message received';
                message.textContent = '← Received: ' + event.data;
                messagesDiv.appendChild(message);
                messagesDiv.scrollTop = messagesDiv.scrollHeight;
            };

            ws.onerror = function(error) {
                statusSpan.textContent = 'Error: ' + error;
                statusSpan.style.color = 'red';
            };

            ws.onclose = function() {
                statusSpan.textContent = 'Disconnected';
                statusSpan.style.color = 'red';
            };

            function sendMessage() {
                const text = input.value;
                if (text.trim() !== '') {
                    ws.send(text);

                    const message = document.createElement('div');
                    message.className = 'message sent';
                    message.textContent = 'Sent: ' + text + ' →';
                    messagesDiv.appendChild(message);
                    messagesDiv.scrollTop = messagesDiv.scrollHeight;

                    input.value = '';
                }
            }

            input.addEventListener('keypress', function(event) {
                if (event.key === 'Enter') {
                    sendMessage();
                }
            });
        </script>
    </body>
    </html>
    """
    return HTMLResponse(html)


async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint at /ws"""
    await websocket.accept()

    try:
        while True:
            # Receive message from client
            data = await websocket.receive_text()

            # Echo back the same message
            await websocket.send_text(data)
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()


# Create ASGI application
app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
