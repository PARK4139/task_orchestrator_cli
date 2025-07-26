from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.ensure_printed import ensure_printed


def is_leaf_d(d):
    import traceback

    import os
    ensure_printed(f'''d={d}  {'%%%FOO%%%' if LTA else ''}''')
    try:
        contents = os.listdir(d)
        if len(contents) > 0:
            return 0
        for content in contents:
            pnx = os.path.join(d, content)
            if is_d(pnx):
                return 0
        return 1
    except:
        ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
