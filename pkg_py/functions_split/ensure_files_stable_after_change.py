from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_files_stable_after_change(f_list, stable_seconds_limit, monitoring_interval_seconds=0.2):
    from pkg_py.functions_split.ensure_slept import ensure_slept
    import os
    import time
    from pkg_py.functions_split.get_nx import get_nx

    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style

    f_list = [get_pnx_os_style(f) for f in f_list]

    def get_mtime_map(f_list):
        result = {}
        for f in f_list:
            f_clean = os.path.abspath(f.strip())
            try:
                if os.path.exists(f_clean):
                    result[f] = os.path.getmtime(f_clean)
                else:
                    ensure_printed(f" 경로 없음: {f_clean}", print_color='red')
            except Exception as e:
                ensure_printed(f" getmtime 실패: {f_clean} | {e}", print_color='red')
        return result

    f_nx_list = [get_nx(f) for f in f_list]
    ensure_printed(f" {stable_seconds_limit}초간 f_nx_list={f_nx_list} 변경 감시 시작...", print_color='white')
    baseline = get_mtime_map(f_list)
    start_time = time.time()

    while True:
        current = get_mtime_map(f_list)
        for f in f_list:
            if f in baseline and f in current and baseline[f] != current[f]:
                ensure_printed(f"f_list is not stable ({f})")
                return False
        if time.time() - start_time >= stable_seconds_limit:
            ensure_printed(f"f_list is stable for ({stable_seconds_limit})")
            return True

        ensure_slept(monitoring_interval_seconds)
