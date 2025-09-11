from functools import cache

from functions.get_gemini_cli_window_title_manual import get_gemini_cli_window_title_manual


# @ensure_function_return_ttl_cached(ttl_seconds=60 * 1 * 1, maxsize=10)
@cache  # 프로그램 실행 1회만 실행, 캐시하여 값 반환.
def get_gemini_cli_window_title():
    import logging

    from functions.get_gemini_cli_expected_titles import get_gemini_cli_expected_titles
    from functions.get_gemini_cli_window_title_auto import get_gemini_cli_window_title_auto

    gemini_cli_window_title = None

    options = get_gemini_cli_expected_titles()
    logging.debug(f"Options for window title search: {options}")

    # way 2 : auto
    gemini_cli_window_title = get_gemini_cli_window_title_auto(options)
    if gemini_cli_window_title:
        return gemini_cli_window_title

    # way 1 : manual (fallback)
    gemini_cli_window_title = get_gemini_cli_window_title_manual(options)
    if gemini_cli_window_title:
        return gemini_cli_window_title
