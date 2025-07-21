

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def is_empty_d(d_src, debug_mode=True):
    import os
    import traceback

    try:
        if len(os.listdir(d_src)) == 0:
            return 1
        else:
            return 0
    except:
        pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        return None
