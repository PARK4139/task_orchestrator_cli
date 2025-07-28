from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.functions_split.lock_os import lock_os
from pkg_py.functions_split.ensure_slept import ensure_slept


def ensure_os_locked():
    from datetime import datetime, time

    def parse_time_ranges(text_list):
        """sample: ["12:00-13:00", "15:00-15:10"] -> [(time(12,0), time(13,0)), (time(15,0), time(15,10))]"""
        ranges = []
        for txt in text_list:
            try:
                start_str, end_str = txt.split("-")
                h1, m1 = map(int, start_str.strip().split(":"))
                h2, m2 = map(int, end_str.strip().split(":"))
                ranges.append((time(h1, m1), time(h2, m2)))
            except:
                continue
        return ranges

    def is_now_in_time_ranges(now_time, time_ranges):
        for start, end in time_ranges:
            if start <= now_time <= end:
                return True
        return False

    # 샘플 설정 시간
    sleep_time_ranges_text = ["00:12-05:30"]
    lunch_time_ranges_text = ["12:00-13:00"]
    break_time_ranges_text = ["15:00-15:15"]
    exercise_time_ranges_text = ["18:30-18:50"]

    # 파싱
    all_time_blocks = (
            parse_time_ranges(sleep_time_ranges_text)
            + parse_time_ranges(lunch_time_ranges_text)
            + parse_time_ranges(break_time_ranges_text)
            + parse_time_ranges(exercise_time_ranges_text)
    )

    last_cleared_hour = -1  # 아직 클리어된 적 없음을 의미

    while True:
        now = datetime.now()
        now_time = now.time()

        # 1 시간 마다 콘솔 클리어
        if now.hour != last_cleared_hour:
            ensure_console_cleared()
            last_cleared_hour = now.hour

        # 시간 블럭에 해당하면 잠금
        if is_now_in_time_ranges(now_time, all_time_blocks):
            pk_lock_os()

        ensure_slept(milliseconds=10000)
