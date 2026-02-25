from functools import wraps
from typing import Callable, Iterable, Optional


def _extract_user_from_args_kwargs(args, kwargs) -> Optional[dict]:
    for key in ("user", "current_user"):
        if key in kwargs and kwargs[key]:
            return kwargs[key]

    if args:
        first = args[0]
        if isinstance(first, dict) and ("username" in first or "role" in first):
            return first

    try:
        from Models import users as users_mod
    except Exception:
        try:
            import Models.users as users_mod
        except Exception:
            users_mod = None

    if users_mod is not None:
        getter = getattr(users_mod, "get_current_user", None)
        if callable(getter):
            try:
                return getter()
            except Exception:
                return None

        if hasattr(users_mod, "current_user"):
            return getattr(users_mod, "current_user")

    return None


def login_required(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = _extract_user_from_args_kwargs(args, kwargs)
        if not user:
            print("Access denied: please log in first.")
            return None
        return func(*args, **kwargs)

    return wrapper


def role_required(required_role_or_roles: Iterable[str]):
    if isinstance(required_role_or_roles, str):
        required_roles = {required_role_or_roles.lower()}
    else:
        required_roles = {r.lower() for r in required_role_or_roles}

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = _extract_user_from_args_kwargs(args, kwargs)
            if not user:
                print("Access denied: please log in first.")
                return None

            role = None
            if isinstance(user, dict):
                role = user.get("role") or user.get("role_name")
            else:
                role = getattr(user, "role", None)

            if not role or role.lower() not in required_roles:
                print("Access denied: insufficient permissions.")
                return None

            return func(*args, **kwargs)

        return wrapper

    return decorator


__all__ = ["login_required", "role_required"]
