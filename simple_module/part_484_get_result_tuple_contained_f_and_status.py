from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style


def get_result_tuple_contained_f_and_status(d):
    import os

    d = get_pnx_os_style(d)
    if is_d(d):
        result_tuple = {}
        for root, _, f_nx_list in os.walk(d):
            for f_nx in f_nx_list:
                f = os.path.join(root, f_nx)
                try:
                    if os.path.exists(f):
                        result_tuple[f] = os.path.getmtime(f)
                        # pk_print(f'''result_tuple[f]={result_tuple[f]}  {'%%%FOO%%%' if LTA else ''}''',print_color="blue")
                    else:
                        pk_print(f"f not found: {f}", print_color='red')
                except FileNotFoundError:
                    pk_print(f"Error accessing file: {f}", print_color='red')
        return result_tuple
    return {}
