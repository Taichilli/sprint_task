from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from worker import worker

files = ["file1", "file2", "file3", "file4", "file5", "file6", "file7", "file8", "file9", "file10"]


def downloaded(file):
    return f"downloaded: {file} done"

try:
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(downloaded, i) for i in files]

        done, not_done = wait(futures, return_when=ALL_COMPLETED)

        for i in done:
            i.result()
    worker(2)
except Exception as e:
    print(e)