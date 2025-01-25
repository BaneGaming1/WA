import asyncio
import websockets

async def test_websocket():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send(":D")
        response = await websocket.recv()
        print("P ^yijata zpr  va:", response)

        while True:
            message = input("Zadejte ':D' pro dal     vtip: ")
            if message == ':D':
                await websocket.send(message)  
                response = await websocket.recv() 
                print("P ^yijata zpr  va:", response)  
            else:
                print("Neplatn   zpr  va. Zadejte ':D' pro dal     vtip.")

asyncio.run(test_websocket())