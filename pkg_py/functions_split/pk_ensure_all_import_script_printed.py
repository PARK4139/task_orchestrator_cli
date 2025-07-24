import inspect

from pkg_py.functions_split.get_file_id import get_file_id
from pkg_py.system_object.directories import D_WORKING
from pkg_py.system_object.files import F_PK_WORKSPACE_PY
from pkg_py.workspace.pk_workspace import get_value_via_fzf_or_history_routine


def ensure_modules_printed_from_file(f_working):
    modules = get_modules_from_file(f_working)
    for module in modules:
        print(module)


def get_modules_from_file(f_working):
    # todo fix    수작업 결과보다 적었음. 잘못 로직을 만든 것 같음.
    from pkg_py.functions_split.get_list_from_f import get_list_from_f
    modules_parsed = set()
    lines = get_list_from_f(f=f_working)
    signiture1 = f'import '
    signiture2 = f'from '
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
    key_name = 'f_working'
    func_n = inspect.currentframe().f_code.co_name
    file_id = get_file_id(key_name, func_n)
    # editable = False
    editable = True
    init_options = [F_PK_WORKSPACE_PY]
    value = get_value_via_fzf_or_history_routine(key_name=key_name, file_id=file_id, init_options=init_options, editable=editable)
    f_working = value
    ensure_modules_printed_from_file(f_working=f_working)
