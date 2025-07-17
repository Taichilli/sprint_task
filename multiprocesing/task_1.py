import multiprocessing
import time


def worker(work_id):
    print(f"worker start task_id: {work_id}")
    time.sleep(2)
    print(f"worker end task_id: {work_id}")


if __name__ == '__main__':

    processes = []

    for i in range(1,5):
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()
        processes.append(p)

    for i in processes:
        i.join()
