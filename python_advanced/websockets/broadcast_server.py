#!/usr/bin/env python3
"""WebSocket server handling broadcast communication.

Keeps track of connected clients and forwards every message to all
of them, prefixed with "B:".
"""
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

CONNECTED_CLIENTS = set()


async def broadcast(message):
    """Send message to every currently connected client."""
    for client in list(CONNECTED_CLIENTS):
        try:
            await client.send(message)
        except ConnectionClosed:
            CONNECTED_CLIENTS.discard(client)


async def connection_handler(websocket):
    """Register the client, broadcast its messages, then clean up."""
    CONNECTED_CLIENTS.add(websocket)
    try:
        async for message in websocket:
            await broadcast(f"B:{message}")
    except ConnectionClosed:
        pass
    finally:
        CONNECTED_CLIENTS.discard(websocket)


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
