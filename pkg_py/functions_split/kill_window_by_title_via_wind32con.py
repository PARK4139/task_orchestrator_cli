from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def kill_window_by_title_via_wind32con(window_title):
    import traceback
    import win32con  # pywin32
    # import win32gui  # pywin32

    def enum_windows_callback(hwnd, lparam):
        try:
            if win32gui.IsWindowVisible(hwnd):
                current_window_title = win32gui.GetWindowText(hwnd)
                if current_window_title == window_title:
                    win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
                    pk_print(f'close window ({window_title})', print_color='blue')
                    return 0  # 창을 찾았으면 더 이상 탐색하지 않음
        except:
            pk_print(f"{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}", print_color='red')
        return 1  # 계속 탐색

    try:
        # 모든 창을 탐색하여 해당 제목을 찾음
        win32gui.EnumWindows(enum_windows_callback, None)
    except:
        pk_print(f"{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}", print_color='red')
