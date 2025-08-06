def ensure_os_restarted():
    from pkg_py.functions_split.ensure_all_killed import ensure_all_killed

    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.get_list_sorted import get_list_sorted
    from pkg_py.functions_split.get_process_name_list import get_process_name_list
    from pkg_py.functions_split.is_os_linux import is_os_linux
    from pkg_py.functions_split.is_os_windows import is_os_windows

    # process_name_list = get_process_name_list()
    # process_name_list = get_list_sorted(working_list=process_name_list, mode_asc=1)
    # for process_name in process_name_list:
    #     print(process_name)


    if is_os_windows():
        cmd_list = ['shutdown.exe /r']
    elif is_os_linux():
        cmd_list = ['sudo reboot']  # 'systemctl reboot'
    else:
        cmd_list = ['sudo shutdown -r now']

    for cmd in cmd_list:
        ensure_command_excuted_to_os(cmd=cmd, mode='a')

    ensure_all_killed()