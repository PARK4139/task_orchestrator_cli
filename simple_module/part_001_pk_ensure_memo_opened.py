

# import win32gui


from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style


#
# from pkg_py.pk_system_layer_encodings import Encoding
# from pkg_py.pk_system_layer_files import F_MEMO_HOW_PK, F_MEMO_WORK_PK


def pk_ensure_memo_opened():
    f_list = [
        F_MEMO_HOW_PK,
        F_MEMO_WORK_PK,
    ]
    for f in f_list:
        f = get_pnx_os_style(f)
        cmd_to_os(cmd=f'code {f}')
    state = True
