from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.move_pnx import move_pnx
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.directories import D_PK_RECYCLE_BIN


def ensure_pnxs_move_to_recycle_bin(pnx):
    import traceback
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    pnx = get_pnx_os_style(pnx=pnx)
    if does_pnx_exist(pnx):
        try:
            # send2trash.send2trash(pnx)
            # shutil.move(pnx, D_PK_RECYCLE_BIN)
            ensure_pnx_made(D_PK_RECYCLE_BIN, mode='d')
            move_pnx(pnx=pnx, d_dst=D_PK_RECYCLE_BIN)
        except:
            ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
    if does_pnx_exist(pnx):
        ensure_printed(f'''{func_n}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
    if not does_pnx_exist(pnx):
        ensure_printed(f'''{func_n}  {'%%%FOO%%%' if LTA else ''}''', print_color='green')
