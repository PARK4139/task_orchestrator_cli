

from pkg_py.functions_split.ensure_command_excuted_to_os_v6 import ensure_command_excuted_to_os_v6


def ensure_command_excuted_to_os(cmd: str, mode="", encoding=None, mode_with_window=1):
    # std_list = ensure_command_excuted_to_os_v_1_0_1(cmd=cmd, mode=mode, encoding=encoding)
    # std_list = ensure_command_excuted_to_os_v_1_0_2(cmd=cmd, mode=mode, encoding=encoding)
    # std_list = ensure_command_excuted_to_os_v_1_0_3(cmd=cmd, mode=mode, encoding=encoding)
    # std_list = ensure_command_excuted_to_os_v_1_0_5(cmd=cmd, mode=mode, encoding=encoding)
    std_list = ensure_command_excuted_to_os_v6(cmd=cmd, mode=mode, encoding=encoding, mode_with_window=mode_with_window)
    return std_list
