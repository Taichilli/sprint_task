from multiprocessing import Pool
from task_1 import worker

if __name__ == '__main__':
    with Pool(4) as pool:
        pool.map(worker, range(1, 5))