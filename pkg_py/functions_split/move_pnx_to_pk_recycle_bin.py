from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.move_pnx import move_pnx
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.pk_system_object.directories import D_PK_RECYCLE_BIN


def move_pnx_to_pk_recycle_bin(pnx):
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
            pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
    if does_pnx_exist(pnx):
        pk_print(f'''{func_n}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
    if not does_pnx_exist(pnx):
        pk_print(f'''{func_n}  {'%%%FOO%%%' if LTA else ''}''', print_color='green')
