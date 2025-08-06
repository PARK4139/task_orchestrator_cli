def ensure_os_locked():
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.is_os_windows import is_os_windows
    from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
    from pkg_py.functions_split.save_power_as_s3 import save_power_as_s3

    from datetime import datetime, time
    from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
    from pkg_py.functions_split.ensure_slept import ensure_slept

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

    # 파싱
    all_time_blocks = (
        parse_time_ranges(sleep_time_ranges_text)
    )

    last_cleared_min = -1  # 아직 클리어된 적 없음을 의미

    while True:
        now = datetime.now()
        now_time = now.time()

        if now.min != last_cleared_min:
            ensure_console_cleared()
            last_cleared_min = now.min

        # 시간 블럭에 해당하면 잠금
        if is_now_in_time_ranges(now_time, all_time_blocks):
            if is_os_windows():
                save_power_as_s3()
            elif is_os_wsl_linux():
                save_power_as_s3()
            else:
                ensure_command_excuted_to_os('echo TBD')

        ensure_slept(milliseconds=10000)
