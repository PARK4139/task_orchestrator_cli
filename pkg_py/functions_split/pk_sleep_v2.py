

from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.functions_split.pk_print import pk_print


def pk_sleep_v2(milliseconds=None, seconds=None, minutes=None, hours=None, mode_countdown=1):
    import inspect
    import time
    func_n = inspect.currentframe().f_code.co_name

    # 인자 유효성 검사
    time_units = {"milliseconds": milliseconds, "seconds": seconds, "minutes": minutes, "hours": hours}
    provided_units = {k: v for k, v in time_units.items() if v is not None}
    if len(provided_units) != 1:
        pk_print(str_working=f"{func_n}() 함수는 {list(time_units.keys())} 중 하나만 정의되어야 합니다.")
        return
    unit, value = next(iter(provided_units.items()))

    # 시간을 초 단위로 변환
    time_value = None
    if unit == "milliseconds":
        time_value = value / 1000
    elif unit == "seconds":
        time_value = value
    elif unit == "minutes":
        time_value = value * 60
    elif unit == "hours":
        time_value = value * 3600
    if mode_countdown:
        remaining = int(time_value)

        # 시간, 분, 초로 변환하는 함수
        def format_time(seconds_left):
            hours = seconds_left // 3600
            minutes = (seconds_left % 3600) // 60
            seconds = seconds_left % 60
            return f"{hours:02}:{minutes:02}:{seconds:02}"

        # 카운트다운 시작
        for i in range(remaining, 0, -1):
            formatted_time = format_time(i)
            pk_print(str_working=f"[{PkMessages2025.TIME_LEFT}] [hours:minute:seconds] [{formatted_time}]")
            time.sleep(1)

        # 남은 시간이 소수점으로 딱 맞지 않는 경우, 잉여 시간 처리
        leftover = time_value - remaining
        if leftover > 0:
            time.sleep(leftover)
        else:
            pk_print(str_working="count down complete")
    else:
        time.sleep(time_value)
