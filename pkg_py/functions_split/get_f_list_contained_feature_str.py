from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def get_f_list_contained_feature_str(feature_str, d_pnx):
    import os
    if not os.path.exists(d_pnx):
        pk_print(f'''Directory does not exist: {d_pnx}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        return None
    else:
        pk_print(f'''Searching for feature_str="{feature_str}" in directory: {d_pnx}  {'%%%FOO%%%' if LTA else ''}''')
    files_filtered = []
    for filename in os.listdir(d_pnx):
        if feature_str in filename:
            full_path = os.path.join(d_pnx, filename)
            pk_print(f'''Found file: {full_path}  {'%%%FOO%%%' if LTA else ''}''')
            files_filtered.append(full_path)
    else:
        pk_print(
            f'''No file containing feature_str="{feature_str}" found in directory: {d_pnx}  {'%%%FOO%%%' if LTA else ''}''')
    return files_filtered
