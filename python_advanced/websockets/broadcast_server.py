#!/usr/bin/env python3
"""Simple asyncio WebSocket broadcast server.

This module implements a minimal WebSocket server using the `websockets`
library. It listens on localhost:8765 and broadcasts any received message
to all connected clients, prefixing each message with "B:".
"""

import asyncio
from websockets.asyncio.server import serve


connected_clients = set()


async def connection_handler(websocket):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            for client in connected_clients.copy():
                try:
                    await client.send(f"B:{message}")
                except Exception:
                    connected_clients.discard(client)
    finally:
        connected_clients.discard(websocket)


async def main():
    async with serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
