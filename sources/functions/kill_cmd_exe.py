def kill_cmd_exe():
    import logging
    from sources.functions.ensure_process_killed_by_pid import ensure_process_killed_by_pid
    from sources.functions.get_pids import get_pids
    from sources.objects.pk_local_test_activate import LTA
    try:
        pids = get_pids(process_img_n ="cmd.exe")
        for pid in pids:
            ensure_process_killed_by_pid(pid=pid)
    except:
        logging.debug(rf'''{'%%%FOO%%%' if LTA else ''}''')