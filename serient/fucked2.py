import asyncio
import websockets
print("input:")
nnn=input()
async def hello():
    async with websockets.connect(f"ws://{nnn}:9222") as websocket:
        while True:
            
            message = input()
            await websocket.send(message)
            print(f"Sent message: {message}")
            
            response = await websocket.recv()
            print(f"Received response: {response}")

asyncio.get_event_loop().run_until_complete(hello())