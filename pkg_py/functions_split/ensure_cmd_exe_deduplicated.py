def ensure_cmd_exe_deduplicated():
    import inspect

    from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.ensure_process_deduplicated import ensure_process_deduplicated
    from pkg_py.functions_split.ensure_slept import ensure_slept
    from pkg_py.functions_split.get_file_id import get_file_id
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.get_value_via_fzf_or_history import get_value_via_fzf_or_history
    from pkg_py.functions_split.get_values_sanitize_for_cp949 import get_values_sanitize_for_cp949
    from pkg_py.system_object.gui_util import get_windows_opened
    from pkg_py.system_object.local_test_activate import LTA
    key_name = 'window_opened'
    func_n = inspect.currentframe().f_code.co_name
    values = get_windows_opened()
    values = [get_values_sanitize_for_cp949(v) for v in values]
    ensure_iterable_printed_as_vertical(item_iterable=values, item_iterable_n="values")
    window_opened = get_value_via_fzf_or_history(key_name=key_name, options=values, file_id=get_file_id(key_name, func_n))
    while True:
        window_opened = get_pnx_os_style(window_opened)
        ensure_printed(f'''window_opened={window_opened} {'%%%FOO%%%' if LTA else ''}''')
        ensure_process_deduplicated(window_title_seg=window_opened)
        # ensure_slept(milliseconds=1000)
        ensure_slept(milliseconds=200)
