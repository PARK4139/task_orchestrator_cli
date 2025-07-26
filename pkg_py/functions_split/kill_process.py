def ensure_process_killed(img_name=None, pid=None):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    ensure_printed(str_working=rf'''{PK_UNDERLINE}{func_n}()  {'%%%FOO%%%' if LTA else ''}''')
    # function_arg_names= [param.name for param in inspect.signature(process_kill).parameters.values()] # fail
    Nones = [img_name, pid]
    None_count = Nones.count(None)
    if None_count == 2:
        ensure_printed(str_working=rf''' 이 {func_n}()의 인자는 최대 1개 까지 받을 수 있습니다.  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
    if None_count == 1:
        if img_name is not None:
            img_name = img_name.replace("\'", "")
            img_name = img_name.replace("\"", "")
            ensure_command_excuted_to_os(f'taskkill /f /im "{img_name}"')
            ensure_command_excuted_to_os(f'wmic process where name="{img_name}" delete ')
        if pid is not None:
            # ensure_command_excuted_to_os(f'taskkill /f /pid {pid}', debug_mode=debug_mode)
            ensure_command_excuted_to_os(f'taskkill /f /pid {pid}')
    if None_count == 0:
        ensure_printed(str_working=rf''' 이 {func_n}()의 인자는 최소 1개의 인자가 요구됩니다.  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
