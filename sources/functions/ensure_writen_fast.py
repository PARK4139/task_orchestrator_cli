def ensure_writen_fast(string: str):
    from sources.functions import ensure_slept
    from sources.functions.ensure_text_saved_to_clipboard_and_pasted_with_keeping_clipboard import ensure_text_saved_to_clipboard_and_pasted_with_keeping_clipboard
    import logging
    ensure_slept(milliseconds=500)
    ensure_text_saved_to_clipboard_and_pasted_with_keeping_clipboard(string)
    logging.debug(rf"{string}")
