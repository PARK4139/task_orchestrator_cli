def run_powershell_exe_as_admin():
    from sources.functions.ensure_command_executed import ensure_command_executed
    from sources.functions.ensure_window_to_front import ensure_window_to_front
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    # ensure_command_executed('PowerShell -cmd "Start-Process powershell"')
    ensure_command_executed('powershell -cmd "Start-Process powershell -Verb RunAs"')
    ensure_window_to_front("관리자: Windows PowerShell")
