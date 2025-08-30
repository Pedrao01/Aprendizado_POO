import random
from functools import wraps

def retry(times):#decorator with parametri
    def decorator(func):#real decorator
        @wraps(func)
        def wrapper(*args, **kwargs):
            for c in range(0, times):
                try:#Executes if the returned value doesn't give an error
                    result = func(*args, **kwargs)
                    print(f'success in the attempt {c+1}!')
                    return result
                except ValueError as e:#Executes if the returned ValueError
                    print(f'Attempt {c+1}: {e}')
            return f'Falha nas {times} tentativas'
        return wrapper
    return decorator


@retry(times=3)#passing parameter to the decorator
def unstable_operation():#function to be decorated
    x = random.randint(0, 1)
    if x == 0:
        raise ValueError('falhou :(')
    return 'deu certo :)'

#call the function
print(unstable_operation())
