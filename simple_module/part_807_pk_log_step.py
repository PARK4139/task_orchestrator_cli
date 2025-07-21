import win32com.client

from pkg_py.simple_module.part_014_pk_print import pk_print


def pk_log_step(step_label: str):
    import functools
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            pk_print(f"[{step_label}] Starting")
            result = func(*args, **kwargs)
            pk_print(f"[{step_label}] Completed")
            return result

        return wrapper

    return decorator
