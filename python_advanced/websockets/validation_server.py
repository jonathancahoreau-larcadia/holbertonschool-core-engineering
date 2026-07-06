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
