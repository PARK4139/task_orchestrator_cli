from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_window_minimized_like_human():
    from sources.functions.ensure_pressed import ensure_pressed
    ensure_pressed("alt", "space")
    ensure_pressed("n")
