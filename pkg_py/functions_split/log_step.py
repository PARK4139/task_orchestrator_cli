
@functools.wraps(func)
def decorator(func):
def pk_log_step(step_label: str):
def wrapper(*args, **kwargs):
from pkg_py.functions_split.print import pk_print
import functools
import win32com.client
pk_print(f"[{step_label}] Completed")
pk_print(f"[{step_label}] Starting")
result = func(*args, **kwargs)
return decorator
return result
return wrapper
