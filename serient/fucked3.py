import asyncio
import os
import socket

# 获取当前系统主机名
hostname = socket.gethostname()
# 获取主机名对应的IP地址
local_ip = socket.gethostbyname(hostname)
print(local_ip)
try:
    import websockets
    async def echo(websocket, path):
        async for message in websocket:
            print(f"Received message: {message}")
            await websocket.send("Execution succeed!")

    start_server = websockets.serve(echo, local_ip, 8222)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
except ImportError:
    os.system("pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple websockets")
    os.system("python fuck.py")