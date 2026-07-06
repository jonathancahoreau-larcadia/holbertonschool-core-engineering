#!/usr/bin/env python3
"""WebSocket server with basic message validation."""
import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    """Handle messages from one client and validate empty messages."""
    try:
        async for message in websocket:
            clean_message = message.strip()

            if not clean_message:
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{clean_message}")
    except ConnectionClosed:
        pass


async def main():
    """Start the validation WebSocket server."""
    async with serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
