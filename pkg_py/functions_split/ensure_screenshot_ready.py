from pkg_py.functions_split import ensure_slept
from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_screenshot_ready():
    from pkg_py.functions_split.ensure_window_minimized import ensure_window_minimized
    import inspect
    from pkg_py.system_object.etc import pk_
    from pkg_py.functions_split.ensure_pressed import ensure_pressed
    func_n = inspect.currentframe().f_code.co_name
    ensure_window_minimized(window_title=f"{pk_}{func_n}")
    ensure_slept(milliseconds=50)
    ensure_pressed("win", "shift", "s")
