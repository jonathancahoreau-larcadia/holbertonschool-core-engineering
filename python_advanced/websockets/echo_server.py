#!/usr/bin/env python3
"""Simple asyncio WebSocket echo server.

This module implements a minimal WebSocket server using the
`websockets` library. It listens on localhost:8765 and echoes back any
message received from connected clients.
"""

import asyncio
from websockets.asyncio.server import serve


async def connection_handler(websocket):
    async for message in websocket:
        await websocket.send(message)


async def main():
    async with serve(connection_handler, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
