import random
from functools import wraps
from time import time

def require_role(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, value, *args, **kwargs):
            if user['role'] != required_role:
                raise PermissionError(f'access denied! current role = {user["role"]}, required role = {required_role}')
            return func(user, value, *args, **kwargs)
        return wrapper
    return decorator

def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(user, value, *args, **kwargs):
            for c in range(0, times):
                try:
                    result = func(user, value, *args, **kwargs)
                    return result
                except ValueError as e:
                    print(e)
            return f'All {times} attements failed!'
        return wrapper
    return decorator

def check(func):
    @wraps(func)
    def wrapper(user, value, *args, **kwargs):
        x = random.randint(1,10)
        if x <= 3:
            raise ValueError('Temporary failure of the banking system!')
        result = func(user, value, *args, **kwargs)
        return result
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(user, value, *args, **kwargs):
        start = time()
        resulted = func(user, value, *args, **kwargs)
        end = time()
        print(f'Execution time {end - start:.6f} seconds.')
        return resulted
    return wrapper

@require_role('admin')
@timer
@retry(times=2)
@check
def tranferir(user, value):
    return f'Transfer of {value} completed!'


user_admin = {"name": "Alice", "role": "admin"}
user_guest = {"name": "Bob", "role": "guest"}

try:
    print(tranferir(user_admin, 100))
    print(tranferir(user_guest, 50))
except PermissionError as e:
    print(e)
