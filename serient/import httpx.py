import httpx
client=httpx.Client(http2=True) #重点：要用HTTP2
website="https://note.ms/1111111"
i=0
while i<1:
    form={"t":"12345"}
    header={"Referer":website+str(i)} #另一个重点：一样的Referer
    client.post(website+str(i),data=form,headers=header)
    print(i)