

# import win32process
# import win32gui
# import pywin32
# from project_database.test_project_database import MySqlUtil

from pkg_py.functions_split.pk_print import pk_print


def pk_sleep_v1(milliseconds=None, seconds=None, minutes=None, hours=None, mode_countdown=1):
    import inspect
    import time

    func_n = inspect.currentframe().f_code.co_name

    # 인자 유효성 검사
    time_units = {"milliseconds": milliseconds, "seconds": seconds, "minutes": minutes, "hours": hours}
    provided_units = {k: v for k, v in time_units.items() if v is not None}
    if len(provided_units) != 1:
        pk_print(
            prompt=f"{func_n}() 함수는 {list(time_units.keys())} 중 하나만 정의되어야 합니다."
        )
        return
    unit, value = next(iter(provided_units.items()))
    if unit == "milliseconds":
        time_value = value / 1000
    elif unit == "seconds":
        time_value = value
    elif unit == "minutes":
        time_value = value * 60
    elif unit == "hours":
        time_value = value * 3600
    time.sleep(time_value)  # time 객체를 써야함
