#!/usr/bin/env python3
"""WebSocket server handling unicast communication.

Keeps track of connected clients and replies only to the sender,
prefixing each response with "U:".
"""
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

CONNECTED_CLIENTS = set()


async def connection_handler(websocket):
    CONNECTED_CLIENTS.add(websocket)
    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
    except ConnectionClosed:
        pass
    finally:
        CONNECTED_CLIENTS.discard(websocket)


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
