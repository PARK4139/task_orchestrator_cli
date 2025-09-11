def ensure_power_saved_as_s4():
    from sources.functions.ensure_command_executed import ensure_command_executed
    from sources.functions.is_os_windows import is_os_windows
    if is_os_windows():
        ensure_command_executed(cmd=r'C:\Windows\System32\rundll32.exe powrprof.dll,SetSuspendState hibernate')
