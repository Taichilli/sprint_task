import threading
from worker import worker

lock = threading.Lock()

counter = 0

def appender():
    global counter
    for i in range(100):
        with lock:
            counter += 1

try:
    t = threading.Thread(target=appender)
    t2 =threading.Thread(target=appender)
    t3 = threading.Thread(target=appender)

    t.start()
    t2.start()
    t3.start()

    t.join()
    t2.join()
    t3.join()

    print(counter)
    worker(1)
except Exception as e:
    print(e)

