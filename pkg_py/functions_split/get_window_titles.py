from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured
from pkg_py.system_object.ttl_cache_manager import ensure_function_ttl_cached


@ensure_seconds_measured
# @ensure_function_ttl_cached(ttl_seconds=60, maxsize=64)
def get_window_titles(process_img_n=None):
    # test result = 0.000 passed via @ensure_seconds_measured at 250413

    import win32gui
    import win32process

    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.local_test_activate import LTA

    import traceback
      # pywin32
    

    import psutil
    if process_img_n is not None:
        titles = []

        # 프로세스 목록에서 이름으로 PID 찾기
        pids = [p.info['pid'] for p in psutil.process_iter(['name', 'pid']) if p.info['name'] == process_img_n]
        if LTA:
            ensure_printed(f"Found PIDs : '{process_img_n}': {pids}")
        if not pids:
            ensure_printed(f"Process '{process_img_n}' not found.")
            return titles

        # PID에 연결된 창 검색
        def enum_windows_callback(hwnd, pids):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid in pids:
                title = win32gui.GetWindowText(hwnd)
                if title:  # 제목이 있는 창만 추가
                    titles.append(title)

        for pid in pids:
            win32gui.EnumWindows(enum_windows_callback, [pid])
        if LTA:
            print(f"Window titles for process '{process_img_n}': {titles}")
        return titles
    if process_img_n is None:
        window_titles = []
        try:
            def enum_windows_callback(hwnd, lparam):
                if win32gui.IsWindowVisible(hwnd):
                    current_window_title = win32gui.GetWindowText(hwnd)
                    if current_window_title:  # 제목이 비어 있지 않은 경우에만 추가
                        window_titles.append(current_window_title)
                return 1  # 계속해서 다른 창들도 검색

            win32gui.EnumWindows(enum_windows_callback, None)
        except Exception as e:
            ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

        return window_titles
