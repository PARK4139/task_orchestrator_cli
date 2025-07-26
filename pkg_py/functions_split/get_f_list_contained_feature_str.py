from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def get_f_list_contained_feature_str(feature_str, d_pnx):
    import os
    if not os.path.exists(d_pnx):
        ensure_printed(f'''Directory does not exist: {d_pnx}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        return None
    else:
        ensure_printed(f'''Searching for feature_str="{feature_str}" in directory: {d_pnx}  {'%%%FOO%%%' if LTA else ''}''')
    files_filtered = []
    for filename in os.listdir(d_pnx):
        if feature_str in filename:
            full_path = os.path.join(d_pnx, filename)
            ensure_printed(f'''Found file: {full_path}  {'%%%FOO%%%' if LTA else ''}''')
            files_filtered.append(full_path)
    else:
        ensure_printed(
            f'''No file containing feature_str="{feature_str}" found in directory: {d_pnx}  {'%%%FOO%%%' if LTA else ''}''')
    return files_filtered
