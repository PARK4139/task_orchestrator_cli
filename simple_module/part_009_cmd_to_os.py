

from pkg_py.simple_module.part_011_cmd_to_os_v6 import cmd_to_os_v6


def cmd_to_os(cmd: str, mode="", encoding=None, mode_with_window=1):
    # std_list = cmd_to_os_v_1_0_1(cmd=cmd, mode=mode, encoding=encoding)
    # std_list = cmd_to_os_v_1_0_2(cmd=cmd, mode=mode, encoding=encoding)
    # std_list = cmd_to_os_v_1_0_3(cmd=cmd, mode=mode, encoding=encoding)
    # std_list = cmd_to_os_v_1_0_5(cmd=cmd, mode=mode, encoding=encoding)
    std_list = cmd_to_os_v6(cmd=cmd, mode=mode, encoding=encoding, mode_with_window=mode_with_window)
    return std_list
