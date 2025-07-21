from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.pk_system_layer_100_os import is_os_windows

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def save_d_to_f(d, f):
    with open(f, "w", encoding='utf-8') as f_obj:
        d = get_pnx_os_style(d)
        f_obj.write(d)
        if LTA:
            pk_print(f'''d={d} %%%FOO%%%''')
