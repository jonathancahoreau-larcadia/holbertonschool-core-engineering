#!/usr/bin/env python3
"""Simple asyncio WebSocket client.

This module demonstrates a minimal WebSocket client using the
`websockets` library. It connects to a locally running WebSocket server,
sends a greeting message, and receives a response.
"""
import asyncio
import os
import sys
from websockets.asyncio.client import connect


async def connect_and_send(uri, message):
    async with connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        return (response)


async def main():
    """Run the WebSocket client."""
    uri = os.getenv("WS_URI", "ws://localhost:8765")
    message = os.getenv("WS_MESSAGE", "Hello WebSocket")

    if len(sys.argv) > 1:
        message = sys.argv[1]

    response = await connect_and_send(uri, message)
    sys.stdout.write(response)


if __name__ == "__main__":
    asyncio.run(main())
