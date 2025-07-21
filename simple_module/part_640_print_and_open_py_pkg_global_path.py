from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def print_and_open_py_pkg_global_path():
    import sys

    for sys_path in sys.path:
        pk_print(working_str=sys_path)
        if is_pattern_in_prompt(prompt=sys_path, pattern='site-packages') == True:
            pk_print(f'''sys_path={sys_path}  {'%%%FOO%%%' if LTA else ''}''')
            pk_print(working_str=rf'echo "{sys_path}"')
            open_pnx_by_ext(sys_path)
