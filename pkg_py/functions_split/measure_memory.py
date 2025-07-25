
# deep size 측정용 (optional, pip install pympler)
# deep 크기 측정 (가능한 경우)
# import gc; gc.collect()
# 강제 가비지 컬렉션 후 초기 메모리 측정 (선택)
# 반환 객체 크기 측정 (얕은 크기)
@functools.wraps(func)
after_rss = proc.memory_info().rss
before_rss = proc.memory_info().rss
deep_bytes = asizeof.asizeof(result)
deep_mb = deep_bytes / (1024 ** 2)
def pk_measure_memory(func):
def wrapper(*args, **kwargs):
delta_rss_mb = (after_rss - before_rss) / (1024 ** 2)
else:
except ImportError:
f"반환 객체 얕은 크기: {shallow_mb:.2f} MiB")
from pkg_py.functions_split.print import pk_print
from pympler import asizeof
have_pympler = False
have_pympler = True
if have_pympler:
import functools
import os
import psutil
import sys
msg += " (deep 측정하려면 `pip install pympler`)"
msg += f", 반환 객체 깊은 크기: {deep_mb:.2f} MiB"
msg = (f"[{func.__name__}] RSS 증가: {delta_rss_mb:.2f} MiB, "
pk_print(msg, print_color="yellow")
proc = psutil.Process(os.getpid())
result = func(*args, **kwargs)
return result
return wrapper
shallow_bytes = sys.getsizeof(result)
shallow_mb = shallow_bytes / (1024 ** 2)
try:
