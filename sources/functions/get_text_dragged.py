def get_text_dragged():
    from sources.functions.get_text_from_clipboard import get_text_from_clipboard
    from sources.functions.ensure_slept import ensure_slept
    from sources.functions.ensure_pressed import ensure_pressed

    import clipboard
    clipboard_current_contents = get_text_from_clipboard()
    while 1:
        ensure_pressed("ctrl", "c")
        ensure_slept(milliseconds=15)
        text_dragged = get_text_from_clipboard()
        if clipboard_current_contents != text_dragged:
            break
    clipboard.copy(clipboard_current_contents)
    return text_dragged


def get_text_dragged_alternative():
    from sources.functions.get_text_from_clipboard import get_text_from_clipboard
    from sources.functions.ensure_slept import ensure_slept
    from sources.objects.pk_local_test_activate import LTA
    import logging

    from sources.functions.ensure_pressed import ensure_pressed

    import inspect
    import clipboard
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    clipboard_current_contents = get_text_from_clipboard()
    ensure_pressed("ctrl", "c")
    text_dragged = get_text_from_clipboard()
    logging.debug(rf'''text_dragged="{text_dragged}"  {'%%%FOO%%%' if LTA else ''}''')
    clipboard.copy(clipboard_current_contents)

    return text_dragged
