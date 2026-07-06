#!/usr/bin/env python3
"""Simple asyncio WebSocket client.

This module demonstrates a minimal WebSocket client using the
`websockets` library. It connects to a locally running WebSocket server,
sends a greeting message, and receives a response.
"""
import asyncio
from websockets.asyncio.client import connect


async def main():
    message = "Hello WebSocket"

    async with connect("ws://localhost:8765") as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        print(response)


if __name__ == "__main__":
    asyncio.run(main())
