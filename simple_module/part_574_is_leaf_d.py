from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_014_pk_print import pk_print


def is_leaf_d(d):
    import traceback

    import os
    pk_print(f'''d={d}  {'%%%FOO%%%' if LTA else ''}''')
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
        pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
