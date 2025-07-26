from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os


def ensure_command_excuted_to_os_with_splited_arg(cmd, capture_output=False, **kwargs):
    """ensure_command_excuted_to_os로 OS 명령 실행"""
    cmd_str = ' '.join(cmd) if isinstance(cmd, (list, tuple)) else str(cmd)
    print(f"> {cmd_str}")
    return ensure_command_excuted_to_os(cmd=cmd_str)
