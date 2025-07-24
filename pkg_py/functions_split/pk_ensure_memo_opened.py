
def pk_ensure_memo_opened():
    from pkg_py.functions_split.cmd_to_os import cmd_to_os
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.system_object.files import F_MEMO_WORK_PK, F_MEMO_HOW_PK
    f_list = [
        F_MEMO_HOW_PK,
        F_MEMO_WORK_PK,
    ]
    for f in f_list:
        f = get_pnx_os_style(f)
        cmd_to_os(cmd=f'explorer.exe {f}')
    state = True
