from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def is_f_contained_feature_str(feature_str, d_pnx):
    import os
    if not os.path.exists(d_pnx):
        pk_print(f'''Directory does not exist: {d_pnx}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        return 0
    for filename in os.listdir(d_pnx):
        if feature_str in filename:
            return 1
    return 0
