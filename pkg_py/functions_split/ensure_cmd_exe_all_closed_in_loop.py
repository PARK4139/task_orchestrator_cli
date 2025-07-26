def ensure_cmd_exe_all_closed_in_loop():
    while True:
        key_name = 'window_opened'
        values = get_windows_opened()
        func_n = inspect.currentframe().f_code.co_name
        # sys.stdout.reconfigure(encoding='utf-8') # fail
        # values = values.replace('–', '-')  # 유니코드 EN DASH → 하이픈
        values = [get_values_sanitize_for_cp949(v) for v in values]
        ensure_iterable_printed_as_vertical(item_iterable=values, item_iterable_n="values")
        window_opened = get_value_via_fzf_or_history(key_name=key_name, options=values, file_id=get_file_id(key_name, func_n))
        window_opened = get_pnx_os_style(window_opened)
        ensure_printed(f'''window_opened={window_opened} {'%%%FOO%%%' if LTA else ''}''')

        pk_ensure_process_killed(window_title=window_opened)
        # ensure_slept(seconds=1000)
        # ensure_slept(seconds=500)
        ensure_slept(milliseconds=200)


