import asyncio



async def work(task:str,delay:int):
    print(f"Start working: {task}")
    await asyncio.sleep(delay)
    print(f"End Working: {task}")


asyncio.run(work("A",2))