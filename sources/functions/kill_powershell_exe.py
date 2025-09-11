def kill_powershell_exe(debug_mode=True):
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    try:
        pids = get_pids("powershell.exe")
        for pid in pids:
            ensure_process_killed_via_wmic(pid=pid)
    except:
        logging.debug(rf'''{'%%%FOO%%%' if LTA else ''}''')


