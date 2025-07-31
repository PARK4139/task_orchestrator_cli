

def get_windows_opened():
    from pkg_py.functions_split.get_windows_opened_via_win32gui import get_windows_opened_via_win32gui
    # return get_windows_opened_via_psutil()
    # return get_windows_opened_via_pygetwindow()
    return get_windows_opened_via_win32gui()

