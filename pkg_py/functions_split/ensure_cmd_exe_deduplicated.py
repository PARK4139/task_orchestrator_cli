def ensure_cmd_exe_deduplicated():
    key_name = 'window_opened'
    func_n = inspect.currentframe().f_code.co_name
    values = get_windows_opened()
    values = [get_values_sanitize_for_cp949(v) for v in values]
    print_iterable_as_vertical(item_iterable=values, item_iterable_n="values")
    window_opened = get_value_via_fzf_or_history(key_name=key_name, options=values, file_id=get_file_id(key_name, func_n))
    while True:
        window_opened = get_pnx_os_style(window_opened)
        ensure_printed(f'''window_opened={window_opened} {'%%%FOO%%%' if LTA else ''}''')
        pk_ensure_process_deduplicated(window_title_seg=window_opened)
        # ensure_slept(milliseconds=1000)
        ensure_slept(milliseconds=200)


