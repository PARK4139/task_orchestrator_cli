def ensure_console_paused(text=None):
    import logging

    from functions.get_caller_n import get_caller_n
    from objects.pk_etc import PK_UNDERLINE
    func_n = get_caller_n()
    logging.debug(PK_UNDERLINE)
    if text is None:
        text = f"paused by {func_n}() ,if you want to continue, press any key"
    else:
        text = f'{text}, if you want to continue, press any key'
    input(text)
