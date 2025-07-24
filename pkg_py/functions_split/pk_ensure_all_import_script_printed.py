from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_pnx_list_from_d_working import get_pnxs_from_d_working
from pkg_py.functions_split.is_f import is_f


def pk_ensure_modules_printed_from_file(f_working):
    from pkg_py.functions_split.get_list_from_f import get_list_from_f
    # # # todo fix    수작업 결과보다 적었음. 잘못 로직을 만든 것 같음.
    line_imported_pkg_set = set()
    line_list = get_list_from_f(f=f_working)
    signiture1 = f'import'
    signiture2 = f'from'
    for line in line_list:
        line = line.strip()
        if line.startswith('#'):
            line = line.replace('#', "", 1)
        if line.startswith(signiture1):
            line_imported_pkg_set.add(line.strip())
        if line.startswith(signiture2):
            line_imported_pkg_set.add(line.strip())
    line_imported_pkg_set = sorted(line_imported_pkg_set, reverse=True)
    for line_imported_pkg in line_imported_pkg_set:
        print(line_imported_pkg)


def pk_ensure_modules_printed():
    import os
    # d_working = rf"{os.environ['USERPROFILE']}\Downloads\pk_system\pkg_py\functions_split"  # pk_option
    # d_working = rf"{os.environ['USERPROFILE']}\Downloads\pk_system\pkg_py\workspace"  # pk_option
    d_working = rf"{D_PKG_PY}"  # pk_option
    pnxs = get_pnxs_from_d_working(d_working=d_working)
    for pnx in pnxs:
        if is_f(pnx):
            f_working = pnx
            pk_ensure_modules_printed_from_file(f_working=f_working)
