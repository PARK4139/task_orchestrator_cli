
"""
Args:
Print and return current alive threads.
Returns:
def debug_current_threads(verbose: bool = True) -> list:
for t in thread_list:
if verbose:
import threading
list: List of thread names.
print(f"  - name={t.name}, daemon={t.daemon}, alive={t.is_alive()}, ident={t.ident}")
print(f"[INFO] Active thread count: {len(thread_list)}")
return [t.name for t in thread_list]
thread_list = threading.enumerate()
verbose (bool): If True, prints detailed info.
