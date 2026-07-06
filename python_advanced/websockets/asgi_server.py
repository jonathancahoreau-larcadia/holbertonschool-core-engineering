#!/usr/bin/env python3
"""ASGI WebSocket server using Starlette.

This module defines a simple ASGI application with a WebSocket endpoint.
The app serves an HTML homepage at `/` and echoes back any text received
from clients connected to `/ws`.
"""

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute


async def homepage(request):
    return HTMLResponse("<h1>WebSocket App</h1>")


async def websocket_endpoint(websocket):
    await websocket.accept()
    while True:
        message = await websocket.receive_text()
        await websocket.send_text(message)


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
