from functools import wraps


def login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = kwargs.get("user")
        if not user:
            print("Access denied: please log in first.")
            return None
        return func(*args, **kwargs)
    return wrapper


def role(required_role):
    required_role = required_role.lower()

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = kwargs.get("user")
            if not user:
                print("Access denied: please log in first.")
                return None

            if user.role.lower() != required_role:
                print("Access denied: insufficient permissions.")
                return None

            return func(*args, **kwargs)
        return wrapper
    return decorator