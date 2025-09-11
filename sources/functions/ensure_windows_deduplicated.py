from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_windows_deduplicated():
    from collections import Counter
    import win32gui
    import win32con

    from sources.functions.get_windows_opened_with_hwnd import get_windows_opened_with_hwnd
    windows = get_windows_opened_with_hwnd()
    window_titles = [title for title, hwnd in windows]

    title_counts = Counter(window_titles)

    for title, count in title_counts.items():
        if count > 1:
            # Get all hwnds for the duplicated title
            duplicated_hwnds = [hwnd for t, hwnd in windows if t == title]

            # Keep the first one, close the rest
            for hwnd_to_close in duplicated_hwnds[1:]:
                try:
                    win32gui.PostMessage(hwnd_to_close, win32con.WM_CLOSE, 0, 0)
                    print(f"Closed duplicate window with title: {title}")
                except Exception as e:
                    print(f"Error closing window with title {title}: {e}")


def ensure_process_and_window_deduplicated_core(len_before=None, previous_windows_opened_list=None):
    from sources.functions.get_windows_opened_with_hwnd import get_windows_opened_with_hwnd
    from sources.objects.pk_local_test_activate import LTA
    import logging
    from sources.functions.ensure_windows_closed import ensure_windows_closed
    from sources.functions.ensure_window_to_front import ensure_window_to_front
    from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
    from sources.functions.ensure_func_info_loaded import ensure_func_info_loaded

    if previous_windows_opened_list is None:
        previous_windows_opened_list = get_windows_opened_with_hwnd()

    if len_before is None:
        len_before: int = 0

    # 윈도우 중복 제거
    current_windows_opened_list = get_windows_opened_with_hwnd()
    len_current = len(current_windows_opened_list)

    if len_before != len_current:
        logging.debug(f'''len_before={len_before}  {'%%%FOO%%%' if LTA else ''}''')
        logging.debug(f'''len_current={len_current}  {'%%%FOO%%%' if LTA else ''}''')
        ensure_iterable_log_as_vertical(item_iterable=current_windows_opened_list,
                                        item_iterable_n="current_windows_opened_list")
        len_before = len_current

    if len(current_windows_opened_list) != len(previous_windows_opened_list):
        # 창 중복 제거를 위한 기본 창 제목들
        windows_to_close = ["explorer.exe", "cmd.exe", "powershell.exe"]
        for window_title in windows_to_close:
            ensure_windows_closed(window_title)

        title = ensure_func_info_loaded(func_n="ensure_windows_closed")["title"]
        ensure_window_to_front(title)
        previous_windows_opened_list = current_windows_opened_list

    # ensure_slept(seconds=1)
    # ensure_console_cleared()


def is_process_and_window_deduplicated():
    return False
