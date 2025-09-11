from sources.functions import ensure_slept
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_screenshot_ready():
    from sources.functions.ensure_window_minimized import ensure_window_minimized
    import inspect
    from sources.objects.pk_etc import pk_
    from sources.functions.ensure_pressed import ensure_pressed
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    ensure_window_minimized(window_title=f"{pk_}{func_n}")
    ensure_slept(milliseconds=50)
    ensure_pressed("win", "shift", "s")
