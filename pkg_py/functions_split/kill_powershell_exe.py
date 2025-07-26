def kill_powershell_exe(debug_mode=True):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    try:
        pids = get_pids("powershell.exe")
        for pid in pids:
            kill_process_via_wmic(pid=pid)
    except:
        ensure_printed(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')


