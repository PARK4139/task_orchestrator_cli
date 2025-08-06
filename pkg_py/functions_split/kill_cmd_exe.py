def kill_cmd_exe():
    from pkg_py.functions_split import ensure_printed
    from pkg_py.functions_split.ensure_process_killed_by_pid import ensure_process_killed_by_pid
    from pkg_py.functions_split.get_pids import get_pids
    from pkg_py.system_object.local_test_activate import LTA
    try:
        pids = get_pids(process_img_n ="cmd.exe")
        for pid in pids:
            ensure_process_killed_by_pid(pid=pid)
    except:
        ensure_printed(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')