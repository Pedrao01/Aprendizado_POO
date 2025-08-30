from time import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'{end - start:.6f}')
        return result
    return wrapper

def require_positive(func):
    def wrapper(*args, **kwargs):
        print(f'Verificando: {args} {kwargs}')
        for arg in args:
            print(arg)
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError('Only positive numbers are allowed!')
        print(args)
        print('validação passou!')
        return func(*args, **kwargs)
    return wrapper

@timer
@require_positive
def soma(a, b):
    return a + b

try:
    print(soma(a=2, b=5))
    print(soma(a=-2, b=5))
except ValueError as e:
    print(f'Erro: {e}')
