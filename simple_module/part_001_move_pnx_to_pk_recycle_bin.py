

from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist


def move_pnx_to_pk_recycle_bin(pnx):
    import traceback

    # import send2trash
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
