from functions.get_gemini_prompt_interface_title import get_gemini_cli_assistance_title
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def is_gemini_cli_assistance_opened():
    from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
    import logging
    window_title = get_gemini_cli_assistance_title()
    if is_window_opened_via_window_title(window_title):
        logging.debug(f'gemini interface is already opened')
        return True
    logging.debug(f'gemini interface is not opened')
    return False
