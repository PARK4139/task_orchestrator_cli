
# pk_colorama_init_once()
# todo : 통계자료 수집
@wraps(func)
def pk_measure_seconds(func):
def wrapper(*args, **kwargs):
elapsed_seconds = time.time() - time_s
from functools import wraps
from pkg_py.functions_split.print import pk_print
from pkg_py.system_object.local_test_activate import LTA
func_n = inspect.currentframe().f_code.co_name
if not LTA:
import inspect
import time
pk_print(str_working=f"[ @{func_n} ] [ {func.__name__}() ]  elapsed_seconds={elapsed_seconds:.4f}",print_color='yellow')  # todo 'elapsed_seconds={elapsed_seconds:.4f}' 에 노랗게 해고 싶다.
result = func(*args, **kwargs)  # 원래 함수 실행
return func
return result  # 원래 함수의 반환값 그대로 반환
return wrapper
time_s = time.time()
