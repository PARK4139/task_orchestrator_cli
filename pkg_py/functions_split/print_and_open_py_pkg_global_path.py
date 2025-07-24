from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def print_and_open_py_pkg_global_path():
    import sys

    for sys_path in sys.path:
        pk_print(str_working=sys_path)
        if is_pattern_in_prompt(prompt=sys_path, pattern='site-packages') == True:
            pk_print(f'''sys_path={sys_path}  {'%%%FOO%%%' if LTA else ''}''')
            pk_print(str_working=rf'echo "{sys_path}"')
            open_pnx_by_ext(sys_path)
