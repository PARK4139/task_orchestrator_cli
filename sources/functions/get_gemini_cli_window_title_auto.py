from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def get_gemini_cli_window_title_auto(gemini_cli_expected_titles=None):
    import logging

    from functions.get_gemini_cli_expected_titles import get_gemini_cli_expected_titles
    from functions.get_windows_opened import get_windows_opened

    gemini_cli_window_title = None

    if gemini_cli_expected_titles is None:
        gemini_cli_expected_titles = get_gemini_cli_expected_titles()

    # way 2 : auto
    logging.debug("Automatic detection attempted.")
    windows_opened = get_windows_opened()
    for option in gemini_cli_expected_titles:
        for window_opened in windows_opened:
            compare_result = " 같다 " if len(option) == len(window_opened) else " 다르다 "
            compare_title = f"'{option}' 와 '{window_opened}' 길이비교결과"
            compare_condition = rf"{len(option)}와 {len(window_opened)}는 {compare_result}"
            gap = 1
            logging.debug(f"{compare_title} {compare_condition} {compare_result}")
            if window_opened == option:
                gemini_cli_window_title = option
                logging.debug(f'gemini is already opened')
                return gemini_cli_window_title
    logging.debug(f'gemini is not opened')
    return gemini_cli_window_title
