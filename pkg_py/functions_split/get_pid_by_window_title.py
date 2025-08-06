def get_pid_by_window_title(window_title_seg):  # 테스트필요
    import psutil
    from pkg_py.functions_split.get_window_titles import get_window_titles
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.local_test_activate import LTA
    import inspect
    import pygetwindow
    func_n = inspect.currentframe().f_code.co_name
    # window_titles=pygetwindow.getAllTitles()
    window_titles = get_window_titles()
    matching_window = [w for w in window_titles if window_title_seg.lower() in w.lower()]

    if not matching_window:
        return f"No window found with title containing: '{window_title_seg}'"

    # Assuming the first match
    window_title_match = matching_window[0]
    print(f"Found window: {window_title_match}")

    for process in psutil.process_iter(['pid', 'name']):
        try:
            process_name = process.info['name']
            process_id = process.info['pid']
            process_window_titles = pygetwindow.getWindowsWithTitle(window_title_match)

            ensure_printed(f'process_name="{process_name}"  {'%%%FOO%%%' if LTA else ''}')
            ensure_printed(f'process_id="{process_id}"  {'%%%FOO%%%' if LTA else ''}')
            ensure_printed(f'process_window_titles="{process_window_titles}"  {'%%%FOO%%%' if LTA else ''}')

            if process_window_titles:
                return process_id
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:

            ensure_printed(f"Error processing {process.info['pid']}: {e}")
            continue
    return f"No PID found for window title: '{window_title_match}'"
