from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_process_and_window_deduplicated():
    from sources.functions import ensure_slept
    from sources.functions.ensure_windows_deduplicated import ensure_windows_deduplicated
    while 1:
        ensure_windows_deduplicated()
        ensure_slept(seconds=30)
