from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os


def run_console_blurred_exe():
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    # console_blurred.exe exec
    cmd_str = rf".\dist\console_blurred\console_blurred.exe"
    ensure_command_excuted_to_os(cmd_str)
