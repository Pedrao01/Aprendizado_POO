from functools import wraps


def require_role(request):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user['role'] != request:
                raise PermissionError(f'Access denied! Atual role = {user["role"]}, required role = {request}')
            return func(user, *args, **kwargs)
        return wrapper
    return decorator


@require_role('admin')
def delete_user(user, user_id):
    return f'user {user_id}, was deleted!'

@require_role('guest')
def view_dashboard(user):
    return 'painel de controle'


corrent_user = {'name': 'Alice', 'role': 'admin'}

try:
    print(delete_user(corrent_user, 123))
    print(view_dashboard(corrent_user))
except PermissionError as e:
    print(f'Erro:{e}')
