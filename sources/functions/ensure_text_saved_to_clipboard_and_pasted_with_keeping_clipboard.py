from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_text_saved_to_clipboard_and_pasted_with_keeping_clipboard(text, wsl_mode=False):
    import logging
    import logging
    import traceback

    from sources.functions.ensure_exception_routine_done import ensure_exception_routine_done

    from sources.functions.ensure_text_saved_to_clipboard import ensure_text_saved_to_clipboard
    from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
    from sources.functions.ensure_pressed import ensure_pressed
    from sources.functions.get_str_from_clipboard import get_str_from_clipboard
    from sources.objects.pk_local_test_activate import LTA

    text_bkup = get_str_from_clipboard()
    text_bkup_list = text_bkup.split("\n")
    try:
        # paste for backup
        ensure_iterable_log_as_vertical(item_iterable=text_bkup_list, item_iterable_n="text_bkup_list")

        # copy
        ensure_text_saved_to_clipboard(str_working=text)
        logging.debug(rf'''text={text}  {'%%%FOO%%%' if LTA else ''}''')

        # paste
        if wsl_mode == True:
            ensure_pressed("ctrl", "c")
            ensure_pressed("ctrl", "shift", "v")
        else:
            ensure_pressed("ctrl", "v")
    except Exception as exception:
        ensure_exception_routine_done(__file__=__file__,traceback=traceback, exception=exception)
    finally:
        # copy for restore
        ensure_text_saved_to_clipboard(str_working=text_bkup)
