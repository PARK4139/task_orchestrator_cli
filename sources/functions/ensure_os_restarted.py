from sources.functions.ensure_windows_deduplicated import ensure_windows_deduplicated


def ensure_os_restarted():
    from sources.functions.ensure_applications_killed import ensure_applications_killed

    from sources.functions.ensure_command_executed import ensure_command_executed
    from sources.functions.is_os_linux import is_os_linux
    from sources.functions.is_os_windows import is_os_windows


    ensure_applications_killed(task_orchestrator_cli_application_killing_mode=False)

    if is_os_windows():
        cmd_list = ['shutdown.exe /r']
    elif is_os_linux():
        cmd_list = ['sudo reboot']  # 'systemctl reboot'
    else:
        cmd_list = ['sudo shutdown -r now']

    for cmd in cmd_list:
        ensure_command_executed(cmd=cmd, mode='a')


