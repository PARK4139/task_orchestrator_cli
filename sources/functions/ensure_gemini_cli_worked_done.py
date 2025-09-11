from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_gemini_cli_worked_done():
    from sources.functions import ensure_spoken
    ensure_spoken("GEMINI 작업 완료")
