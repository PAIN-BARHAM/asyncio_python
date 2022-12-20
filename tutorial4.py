import asyncio 

async def main():
    print('start main')
    # Task in async
    task = asyncio.create_task(foo('text'))
    print("schedule a task")
    await asyncio.sleep(0.5)
    print('finished main')
    await asyncio.sleep(20)

async def foo(text):
    print(text)
    await asyncio.sleep(10)
    print('Finished foo')

asyncio.run(main())