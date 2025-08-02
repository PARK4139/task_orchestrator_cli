def ensure_os_restarted():
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.get_list_sorted import get_list_sorted
    from pkg_py.functions_split.get_process_name_list import get_process_name_list
    from pkg_py.functions_split.is_os_linux import is_os_linux
    from pkg_py.functions_split.is_os_windows import is_os_windows

    process_name_list = get_process_name_list()
    process_name_list = get_list_sorted(working_list=process_name_list, mode_asc=1)
    for process_name in process_name_list:
        print(process_name)

    # import ipdb
    # ipdb.set_trace()

    # OS별 재시작 명령어 설정
    if is_os_windows():
        # Windows 재시작 명령어
        cmd_list = [
            'shutdown.exe /r',
        ]
    elif is_os_linux():
        # Linux 재시작 명령어
        cmd_list = [
            'sudo reboot',
            # 또는 'systemctl reboot'
        ]
    else:
        # macOS 재시작 명령어
        cmd_list = [
            'sudo shutdown -r now',
        ]

    for cmd in cmd_list:
        ensure_command_excuted_to_os(cmd=cmd, mode='a')

