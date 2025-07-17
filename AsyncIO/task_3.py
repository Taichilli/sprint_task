import aiohttp
import asyncio
import time

urls = [
    "https://docs.python.org/3/library/multiprocessing.html",
    "https://medium.com/nuances-of-programming/потоковые-и-многопроцессорные-модули-на-python-1a86a6d8986f",
    "https://habr.com/ru/companies/wunderfund/articles/700474/",
    "https://www.youtube.com/",
    "https://leetcd.com/eplore/"  # специально неверный
]

async def fetch(session, url):
    start = time.time()
    try:
        async with session.get(url, timeout=10) as response:
            end = time.time()
            if response.status == 200:
                return f"{url} — ping: {end - start:.2f} сек"
            else:
                return f" {url} — статус {response.status}"
    except Exception as e:
        return f"{url} — ошибка: {e}"

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for res in results:
            print(res)

asyncio.run(main())
