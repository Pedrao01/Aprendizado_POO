from functools import wraps
from time import time, sleep

def require_login(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user['logged_in'] == True:
            print(f'the user: {user["name"]} is logged in!')
            return func(user, *args, **kwargs)
        raise PermissionError(f' The user: {user["name"]} is not logged in')
    return wrapper

def log_action(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        print(f'User {user["name"]} accessed get_balance.')
        return func(user, *args, **kwargs)
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        start = time()
        result = func(user, *args, **kwargs)
        end = time()
        print(f'Execution time {end - start:.6f} secunds')
        return result
    return wrapper

@require_login
@log_action
@timer
def get_balance(user):
    sleep(2)
    return f'{user["name"]}: R$1000,00'

user1 = {'name': 'Pedro', 'logged_in': False}
user2 = {'name': 'Andrey', 'logged_in': True}

user_list = [user1, user2]
for user in user_list:
    try:
        print(get_balance(user))
    except PermissionError as e:
        print(e)
