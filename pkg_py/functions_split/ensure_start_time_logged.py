

def ensure_start_time_logged():
    from pkg_py.system_object.color_map import PK_ANSI_COLOR_MAP
    import time
    start_time = time.time()
    GREEN = PK_ANSI_COLOR_MAP['GREEN']
    RESET = PK_ANSI_COLOR_MAP['RESET']
    print(f"STARTED AT : {GREEN}{time.strftime('%Y-%m-%d %H:%M:%S')}{RESET}")
    return start_time


