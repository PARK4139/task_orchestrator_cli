def kill_cmd_exe():
    try:
        pids = get_pids("cmd.exe")
        for pid in pids:
            ensure_process_killed(pid=pid)
    except:
        ensure_printed(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')


