#!/usr/bin/env python3
"""Simple asyncio WebSocket client.

This module demonstrates a minimal WebSocket client using the
`websockets` library. It connects to a WebSocket server, sends one
message, receives one response, and returns it.
"""
import asyncio
import os
import sys
from websockets.asyncio.client import connect


async def connect_and_send(uri, message):
    """Connect to a WebSocket server, send a message, and return response."""
    async with connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        return response


async def main():
    """Run the WebSocket client."""
    uri = os.getenv("WS_URI", "ws://localhost:8765")

    if len(sys.argv) > 1:
        message = sys.argv[1]
    elif os.getenv("WS_MESSAGE"):
        message = os.getenv("WS_MESSAGE")
    elif os.getenv("WS_URI"):
        message = "demo"
    else:
        message = "Hello WebSocket"

    response = await connect_and_send(uri, message)
    sys.stdout.write(response)


if __name__ == "__main__":
    asyncio.run(main())
