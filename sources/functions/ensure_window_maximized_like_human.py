from sources.functions import ensure_slept
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_window_maximized_like_human():
    from sources.functions import ensure_slept
    from sources.functions.ensure_seconds_measured import ensure_seconds_measured
    from sources.functions.ensure_pressed import ensure_pressed
    # ensure_slept(milliseconds=80)
    ensure_pressed("alt", "space")
    ensure_slept(milliseconds=80)
    ensure_pressed("x")
    ensure_slept(milliseconds=80)
