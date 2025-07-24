from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_pnx_list_from_d_working import get_pnxs_from_d_working
from pkg_py.functions_split.is_f import is_f


def ensure_modules_printed_from_file(f_working):
    modules = get_modules_from_file(f_working)
    for module in modules:
        print(module)

def get_modules_from_file(f_working):
    # todo fix    수작업 결과보다 적었음. 잘못 로직을 만든 것 같음.
    from pkg_py.functions_split.get_list_from_f import get_list_from_f
    modules_parsed = set()
    lines = get_list_from_f(f=f_working)
    signiture1 = f'import'
    signiture2 = f'from'
    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            line = line.replace('#', "", 1)
        if line.startswith(signiture1):
            modules_parsed.add(line.strip())
        if line.startswith(signiture2):
            modules_parsed.add(line.strip())
    modules_parsed = sorted(modules_parsed, reverse=True)
    modules = []
    for line_imported_pkg in modules_parsed:
        modules.append(line_imported_pkg)
    return modules

def ensure_modules_printed():
    import os
    # d_working = rf"{os.environ['USERPROFILE']}\Downloads\pk_system\pkg_py\functions_split"  # pk_option
    # d_working = rf"{os.environ['USERPROFILE']}\Downloads\pk_system\pkg_py\workspace"  # pk_option
    d_working = rf"{D_PKG_PY}"  # pk_option
    pnxs = get_pnxs_from_d_working(d_working=d_working)
    for pnx in pnxs:
        if is_f(pnx):
            f_working = pnx
            ensure_modules_printed_from_file(f_working=f_working)
