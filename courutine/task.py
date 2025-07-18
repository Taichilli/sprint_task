import types
import asyncio


@types.coroutine
def cour():
    print("Start")
    yield
    print("Finish")


async def main():
    await cour()

asyncio.run(main())