import asyncio 

async def main():
    print('start main')
    await foo('text')
    print('finished main')

async def foo(text):
    print(text)
    await asyncio.sleep(10)

asyncio.run(main())