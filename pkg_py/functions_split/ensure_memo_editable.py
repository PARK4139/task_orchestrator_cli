def ensure_memo_editable():
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.system_object.files import F_MEMO_WORK_PK, F_MEMO_HOW_PK
    f_list = [
        F_MEMO_HOW_PK,
        F_MEMO_WORK_PK,
    ]
    for f in f_list:
        f = get_pnx_os_style(f)
        ensure_command_excuted_to_os(cmd=f'explorer.exe {f}')
