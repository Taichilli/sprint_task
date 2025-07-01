one = float(input('введите число'))
two = float(input('введите число'))

def log_function(file):
    def actual(func):
        def wrapper(*args, **kwargs):
            with open(file, 'a+') as f:
                f.write(f'\nTrace: called {func.__name__}()'
                  f' with args: {args}, kwargs: {kwargs}\n')

                output = func(*args, **kwargs)

                f.write(f'Trace: called {func.__name__}()'
                  f' with output: {output}\n')

            return output
        return wrapper
    return actual


@log_function('log.txt')
def test(a,b):
    return a+b

test(one,two)



