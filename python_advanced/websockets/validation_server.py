#!/usr/bin/env python3
"""Validation WebSocket server.

This module provides a minimal WebSocket server using the `websockets`
library. It listens on localhost:8765 and validates incoming messages:
- empty or whitespace-only messages are responded to with "ERR:EMPTY"
- non-empty messages are echoed back prefixed with "OK:".

Run this file as a script to start the server.
"""

import asyncio
from websockets.asyncio.server import serve


async def echo(websocket):
    async for message in websocket:
        clean_message = message.strip()
        if not clean_message:
            await websocket.send("ERR:EMPTY")
        else:
            await websocket.send(f"OK:{clean_message}")


async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
