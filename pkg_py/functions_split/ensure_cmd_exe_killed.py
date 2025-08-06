def ensure_cmd_exe_killed():
    from pkg_py.functions_split.ensure_process_killed_by_image_name import ensure_process_killed_by_image_name

    ensure_process_killed_by_image_name('cmd.exe')
