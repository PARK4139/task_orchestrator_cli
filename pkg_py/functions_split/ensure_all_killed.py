def ensure_all_killed():
    from pkg_py.functions_split.ensure_process_and_window_deduplicated import ensure_process_and_window_deduplicated
    from pkg_py.functions_split.ensure_cmd_exe_killed import ensure_cmd_exe_killed
    from pkg_py.functions_split.ensure_pk_system_processes_killed import ensure_pk_system_processes_killed
    from pkg_py.functions_split.ensure_potplayer_killed import ensure_potplayer_killed
    from pkg_py.functions_split.ensure_process_killed_by_image_name import ensure_process_killed_by_image_name
    from pkg_py.functions_split import ensure_slept

    # import ipdb
    # from pkg_py.functions_split.ensure_windows_printed import ensure_windows_printed
    # ensure_windows_printed()
    # ipdb.set_trace()

    ensure_potplayer_killed()
    ensure_slept(milliseconds=100)

    ensure_process_killed_by_image_name('code.exe')
    ensure_process_killed_by_image_name('cursor.exe')
    ensure_process_killed_by_image_name('pycharm64.exe')
    ensure_slept(milliseconds=100)

    ensure_cmd_exe_killed()
    ensure_slept(milliseconds=100)

    ensure_pk_system_processes_killed()
    ensure_slept(milliseconds=100)

    ensure_process_and_window_deduplicated()
    ensure_slept(milliseconds=100)
