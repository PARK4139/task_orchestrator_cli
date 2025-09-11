def ensure_cmd_exe_deduplicated_once():
    # TODO : 로직검증필요

    import logging
    from pathlib import Path

    from functions.get_caller_n import get_caller_n
    from functions.ensure_value_completed_advanced import ensure_value_completed_advanced
    from sources.functions.ensure_process_deduplicated import ensure_process_deduplicated
    from sources.functions.ensure_slept import ensure_slept
    from sources.functions.get_values_sanitize_for_cp949 import get_values_sanitize_for_cp949
    from sources.functions.get_windows_opened_with_hwnd import get_windows_opened_with_hwnd
    from sources.objects.pk_local_test_activate import LTA

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    values = get_windows_opened_with_hwnd()
    values = [get_values_sanitize_for_cp949(v) for v in values]

    key_name = "window_opened"
    selected = ensure_value_completed_advanced(key_name=key_name, func_n=func_n, options=values, editable=False)
    window_opened = selected

    while True:
        window_opened = Path(window_opened)
        logging.debug(f'''window_opened={window_opened} {'%%%FOO%%%' if LTA else ''}''')
        ensure_process_deduplicated(window_title_seg=window_opened)
        # ensure_slept(milliseconds=1000)
        ensure_slept(milliseconds=200)
