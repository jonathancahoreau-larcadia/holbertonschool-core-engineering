"""Simple asyncio WebSocket echo server.

This module implements a minimal WebSocket server using the
`websockets` library. It listens on localhost:8765 and echoes back any
message received from connected clients.
"""

import asyncio
from websockets.asyncio.server import serve


async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)


async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
