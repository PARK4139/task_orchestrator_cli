from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style


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
                        # ensure_printed(f'''result_tuple[f]={result_tuple[f]}  {'%%%FOO%%%' if LTA else ''}''',print_color="blue")
                    else:
                        ensure_printed(f"f not found: {f}", print_color='red')
                except FileNotFoundError:
                    ensure_printed(f"Error accessing file: {f}", print_color='red')
        return result_tuple
    return {}
