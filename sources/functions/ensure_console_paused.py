def ensure_console_paused(text=None):
    import logging

    from functions.get_caller_n import get_caller_n
    from objects.pk_etc import PK_UNDERLINE
    func_n = get_caller_n()
    logging.debug(PK_UNDERLINE)
    if text is None:
        text = f"paused by {func_n}(), Tip : press Enter to continue"
    else:
        text = f'{text}, Tip : press Enter to continue'
    input(text)
