from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.ensure_printed import ensure_printed


def get_pids(process_img_n=None, pid=None):
    import inspect

    func_n = inspect.currentframe().f_code.co_name

    if process_img_n is not None and pid is not None:
        ensure_printed(rf"{func_n}() 동작 조건 불충족")
        return

    if process_img_n != None:
        cmd = f"tasklist | findstr {process_img_n}"
        std_list = ensure_command_excuted_to_os(cmd=cmd)
        pids = get_list_leaved_element_pattern(items=std_list, pattern=r'^\S+\s+(\d+)\s+[A-Za-z]')
        return pids
    elif pid != None:
        cmd = f'taskkill /f /pid {pid}"'
        std_list = ensure_command_excuted_to_os(cmd=cmd)
        pids = get_list_leaved_element_pattern(items=std_list, pattern=r'^\S+\s+(\d+)\s+[A-Za-z]')
        return pids
    else:
        cmd = f'taskkill'
        std_list = ensure_command_excuted_to_os(cmd=cmd)
        pids = std_list
        return pids
