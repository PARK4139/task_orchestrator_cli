from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_cursor_worked_done():
    from sources.functions.ensure_spoken import ensure_spoken
    ensure_spoken("CURSOR 작업 완료")
