

def ensure_window_to_front_core(window_title_seg):
    from pkg_py.pk_system_layer_100_Local_test_activate import LTA
    import win32gui  # pywin32
    import win32con  # pywin32
    from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
    from pkg_py.simple_module.part_014_pk_print import pk_print
    import traceback
    import pywintypes
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    pk_print(f'''func_n={func_n} {'%%%FOO%%%' if LTA else ''}''')
    try:
        def enum_windows_callback(hwnd, lparam):
            if win32gui.IsWindowVisible(hwnd):
                current_window_title = win32gui.GetWindowText(hwnd)
                if window_title_seg.lower() in current_window_title.lower():
                    # 창을 전면에 표시하려면 먼저 ShowWindow 호출 후 SetForegroundWindow 호출
                    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # 최소화된 창 복원
                    pk_sleep(seconds=0.2)  # 창 복원 후 잠시 대기
                    # SetForegroundWindow를 재시도
                    try:
                        win32gui.SetForegroundWindow(hwnd)  # 창을 제일 앞으로 가져옴
                    except Exception as e:
                        # pk_print(f'''f"SetForegroundWindow 호출 재시도 Error: {str(e)}""''')
                        pk_sleep(seconds=0.2)  # 잠시 대기 후 재시도
                        # pk_print(f'''f"win32gui.SetForegroundWindow(hwnd) 호출 재시도{str(e)}"" ''', print_color='red')
                        win32gui.SetForegroundWindow(hwnd)  # 재시도
                    return 0  # 더 이상 검색하지 않음
            return 1  # 계속 검색

        try:
            win32gui.EnumWindows(enum_windows_callback, None)
        except pywintypes.error:
            # pk_print(f"{traceback.format_exc()}", print_color='red')
            pass
    except Exception as e:
        pk_print(f"{traceback.format_exc()}", print_color='red')
