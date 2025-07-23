from pkg_py.functions_split.pk_measure_seconds import pk_measure_seconds


@pk_measure_seconds
def ensure_f_list_change_stable(f_list, limit_seconds, monitoring_interval_seconds=0.2):
    from pkg_py.functions_split.pk_sleep import pk_sleep
    import os
    import time
    from pkg_py.functions_split.get_nx import get_nx

    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style

    f_list = [get_pnx_os_style(f) for f in f_list]

    def get_mtime_map(f_list):
        result = {}
        for f in f_list:
            try:
                if os.path.exists(f):
                    result[f] = os.path.getmtime(f)
                else:
                    pk_print(f"❌ 경로 없음: {f}", print_color='red')
            except Exception as e:
                pk_print(f"❌ getmtime 실패: {f} | {e}", print_color='red')
        # if LTA:
        #     pk_print(f"[DEBUG] get_mtime_map -> {result}")
        return result

    f_nx_list = [get_nx(f) for f in f_list]
    pk_print(f"⏳ {limit_seconds}초간 f_nx_list={f_nx_list} 변경 감시 시작...", print_color='white')
    baseline = get_mtime_map(f_list)
    start_time = time.time()

    while True:
        current = get_mtime_map(f_list)
        for f in f_list:
            if f in baseline and f in current and baseline[f] != current[f]:
                pk_print(f"f_list is not stable ({f})")
                return False
        if time.time() - start_time >= limit_seconds:
            pk_print(f"f_list is stable for ({limit_seconds})")
            return True

        pk_sleep(monitoring_interval_seconds)
