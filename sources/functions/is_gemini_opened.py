from functions.get_gemini_cli_window_title_auto import get_gemini_cli_window_title_auto
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def is_gemini_opened():
    gemini_cli_window_title = get_gemini_cli_window_title_auto()
    if gemini_cli_window_title:
        return True
    return False
