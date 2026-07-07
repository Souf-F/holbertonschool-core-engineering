#!/usr/bin/env python3
"""WebSocket client.

Exposes connect_and_send(uri, message) to send one message to a
WebSocket server and return its response. When run directly, connects
to the server at WS_URI (defaulting to ws://localhost:8765) and
prints the response for the message "demo".
"""
import asyncio
import os
import websockets


async def connect_and_send(uri, message):
    """Send message to uri over a WebSocket and return the response."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        return await websocket.recv()


async def main():
    uri = os.environ.get("WS_URI", "ws://localhost:8765")
    response = await connect_and_send(uri, "demo")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
