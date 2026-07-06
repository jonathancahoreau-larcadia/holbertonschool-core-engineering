#!/usr/bin/env python3
"""Simple asyncio WebSocket unicast server.

This module implements a minimal WebSocket server using the `websockets`
library. It accepts client connections on localhost:8765 and echoes each
received message back to the sender prefixed with "U:".
"""

import asyncio
from websockets.asyncio.server import serve


connected_clients = set()


async def connection_handler(websocket):
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
    finally:
        connected_clients.discard(websocket)


async def main():
    async with serve(connection_handler, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
