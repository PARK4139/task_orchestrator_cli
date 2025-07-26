

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def is_empty_d(d_src, debug_mode=True):
    import os
    import traceback

    try:
        if len(os.listdir(d_src)) == 0:
            return 1
        else:
            return 0
    except:
        ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        return None
