def kill_cmd_exe():
    try:
        pids = get_pids("cmd.exe")
        for pid in pids:
            kill_process(pid=pid)
    except:
        ensure_printed(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')


