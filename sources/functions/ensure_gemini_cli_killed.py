from functions.get_gemini_cli_window_title_auto import get_gemini_cli_window_title_auto
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_gemini_cli_killed():
    from sources.functions.ensure_windows_killed_like_human import ensure_windows_killed_like_human
    window_title = get_gemini_cli_window_title_auto()
    if window_title is not None:
        ensure_windows_killed_like_human(window_title)
