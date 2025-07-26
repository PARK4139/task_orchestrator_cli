from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def print_and_open_py_pkg_global_path():
    import sys

    for sys_path in sys.path:
        ensure_printed(str_working=sys_path)
        if is_pattern_in_prompt(prompt=sys_path, pattern='site-packages') == True:
            ensure_printed(f'''sys_path={sys_path}  {'%%%FOO%%%' if LTA else ''}''')
            ensure_printed(str_working=rf'echo "{sys_path}"')
            ensure_pnx_opened_by_ext(sys_path)
