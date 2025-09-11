from sources.functions.ensure_command_executed import ensure_command_executed

from sources.functions.ensure_command_executed import ensure_command_executed


def run_console_blurred_exe():
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    # console_blurred.exe exec
    cmd_str = rf".\dist\console_blurred\console_blurred.exe"
    ensure_command_executed(cmd_str)
