
def decor_task(iter):

    def actual(func):
        import time

        def wrapper(*args, **kwargs):
            for i in range(iter):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                with open('result.txt', 'a+' , encoding='utf-8') as f:
                    f.write(f'{end - start:.12f} seconds'+ '\n')
        return wrapper
    return actual

file_name = 'text.txt'
x = []

@decor_task(iter =10)
def open_text(file):
    with open(file, 'r+', encoding='utf-8') as f:
        for i in f.read().split():
            x.append(i)

open_text(file_name)
print(x)





