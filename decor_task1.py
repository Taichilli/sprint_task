import time

def decor_task(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print( f'{end - start:.7f} seconds')
        return result
    return wrapper

@decor_task
def main():
    with open('text.txt', 'r',encoding='utf-8') as f:
        print(f.read())

main()

file_name = 'text.txt'
file_name2 = 'text2.txt'

@decor_task
def writer(file,file_2):
    with open(file_2, 'r', encoding='utf-8') as source:
        content = source.read()
    with open(file, 'r+',encoding='utf-8') as f:
        f.write(content + '\n')
        f.seek(0)
        print(f.read())


writer(file_name, file_name2)

