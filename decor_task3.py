from datetime import datetime, timezone

one = float(input('введите число'))
two = float(input('введите число'))

def log_function(file):
    def actual(func):
        def wrapper(*args, **kwargs):
            with open(file, 'a+',encoding='utf-8') as f:

                f.write(f'\nИмя функции: {func.__name__}()'
                f' Входные данные args: {args}, kwargs: {kwargs}| время запуска: {datetime.now(timezone.utc)}--> UTC\n')

                output = func(*args, **kwargs)

                f.write(f'Имя функции: {func.__name__}()'
                f' Выходные данные: {output}| Локальное время: {datetime.now(timezone.utc).astimezone()}\n')

            return output
        return wrapper
    return actual


@log_function('log.txt')
def test(a,b):
    return a+b

test(one,two)



