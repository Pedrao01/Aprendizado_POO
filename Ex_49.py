from functools import wraps
from time import time, sleep

def timer(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        start = time()
        result = func(user, *args, **kwargs)
        end = time()
        print(f'execution time: {end - start:.6f}')
        return result
    return wrapper

def requere_role(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user['role'] != required_role:
                raise PermissionError(f'access denied! corruent role = {user["role"]}, required role = {required_role}')
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@timer
@requere_role('admin')
def process_data(user, n):
    sleep(n)
    return f'dormiu por {n}s'

user_admin = {'name': 'Alice', 'role': 'admin'}
user_guest = {'name': 'Bob', 'role': 'guest'}

try:
    print(process_data(user_admin, 3))
    print(process_data(user_guest, 3))
except PermissionError as e:
    print(e)
