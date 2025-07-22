from pkg_py.functions_split.cmd_to_os import cmd_to_os

from pkg_py.functions_split.cmd_to_os import cmd_to_os


def cmd_to_os_with_splited_arg(cmd, capture_output=False, **kwargs):
    """cmd_to_os로 OS 명령 실행"""
    cmd_str = ' '.join(cmd) if isinstance(cmd, (list, tuple)) else str(cmd)
    print(f"> {cmd_str}")
    return cmd_to_os(cmd=cmd_str)
