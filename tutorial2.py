import asyncio 

async def main():
    print('start main')
    task = asyncio.create_task(foo('text'))
    print("schedule a task")
    await task
    print('finished main')

async def foo(text):
    print(text)
    await asyncio.sleep(10)

asyncio.run(main())