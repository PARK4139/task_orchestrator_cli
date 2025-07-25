
# from project_database.test_project_database import MySqlUtil
# 인자 유효성 검사
)
def pk_sleep_v1(milliseconds=None, seconds=None, minutes=None, hours=None, mode_countdown=1):
elif unit == "hours":
elif unit == "minutes":
elif unit == "seconds":
from pkg_py.functions_split.print import pk_print
func_n = inspect.currentframe().f_code.co_name
if len(provided_units) != 1:
if unit == "milliseconds":
import inspect
import time
pk_print(
prompt=f"{func_n}() 함수는 {list(time_units.keys())} 중 하나만 정의되어야 합니다."
provided_units = {k: v for k, v in time_units.items() if v is not None}
return
time.sleep(time_value)  # time 객체를 써야함
time_units = {"milliseconds": milliseconds, "seconds": seconds, "minutes": minutes, "hours": hours}
time_value = value
time_value = value * 3600
time_value = value * 60
time_value = value / 1000
unit, value = next(iter(provided_units.items()))
