import asyncio
import random
import websockets


jokes = [
    "Víte, proč programátoři nemohou používat myčku nádobí? Protože se snaží vyvolat funkci wash() bez toho, aby zavřeli dveře.",
    "Proč programátoři nosí brýle? Protože nemohou C#.",
    "Kolik programátorů je potřeba na výměnu žárovky? Žádný, to je hardwarový problém!",
    "Jak se programátorovi dostane do hlavy nápad? Není to bug, je to funkce!",
    "Proč je programátor jako barman? Oba mají potíže s uzavíráním.",
    "Jak se programátor modlí? Říká: 'Načítám.'",
    "Co dělá programátor, když se mu rozbije auto? Opravi to pomocí debugu.",
    "Jak programátor počítá ovce, když nemůže usnout? Zpátky k debuggeru!",
    "Proč programátoři milují přírodu? Protože má spoustu stromů a listů.",
    "Jaký je rozdíl mezi programátorem a špatným kouzelníkem? Programátor ví, že ne všechno může být magie."
]

async def joke_server(websocket, path):
    while True:
        try:
            message = await websocket.recv()
            if message == ":D":
                next_joke = random.choice(jokes)  
                await websocket.send(next_joke)  
            else:
                await websocket.send("Prosím, pošlete ':D' pro získání dalšího vtipu!")
        except websockets.ConnectionClosed:
            print("Klient se odpojil.")
            break

async def main():
    server = await websockets.serve(joke_server, "0.0.0.0", 8765)
    print("WebSocket server běží na ws://0.0.0.0:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
