#!/usr/bin/env python3
"""WebSocket server with basic message validation.

Rejects empty (or whitespace-only) messages with "ERR:EMPTY",
and echoes valid messages back prefixed with "OK:".
"""
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    """Validate each incoming message before responding."""
    try:
        async for message in websocket:
            stripped = message.strip()
            if not stripped:
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{stripped}")
    except ConnectionClosed:
        pass


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
