import asyncio
from task_1 import work



async def main():
    await asyncio.gather(
        work("A",2),
        work("B",1),
        work("F",3)
    )

asyncio.run(main())