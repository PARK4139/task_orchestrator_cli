

def ensure_end_time_logged():
    from pkg_py.pk_system_layer_color_map import PK_ANSI_COLOR_MAP
    import time
    end_time = time.time()
    GREEN = PK_ANSI_COLOR_MAP['GREEN']
    RESET = PK_ANSI_COLOR_MAP['RESET']
    print(f"ENDED AT : {GREEN}{time.strftime('%Y-%m-%d %H:%M:%S')}{RESET}")
    return end_time


