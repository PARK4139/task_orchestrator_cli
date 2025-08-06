from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_screen_saved_and_wait_for_x_minuite_and_ensure_os_locked():
    from pkg_py.functions_split import ensure_slept, ensure_console_cleared
    from pkg_py.functions_split.ensure_os_locked import ensure_os_locked
    from pkg_py.functions_split.ensure_screen_saved import ensure_screen_saved
    ensure_screen_saved()
    ensure_slept(minutes=50)
    ensure_os_locked()
