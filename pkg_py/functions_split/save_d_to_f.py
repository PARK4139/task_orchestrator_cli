from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
# from pkg_py.system_object.is_os_windows import is_os_windows

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def save_d_to_f(d, f):
    with open(f, "w", encoding='utf-8') as f_obj:
        d = get_pnx_os_style(d)
        f_obj.write(d)
        if LTA:
            ensure_printed(f'''d={d} %%%FOO%%%''')
