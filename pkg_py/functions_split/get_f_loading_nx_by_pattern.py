
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed



def get_f_loading_nx_by_pattern(pattern):
    import re

    window_opened_list = get_windows_opened()
    for window_opened in window_opened_list:
        match = re.search(pattern, window_opened)
        if match:
            f_loading_nx_matched = match.group(1)
            ensure_printed(f'''f_loading_nx_matched={f_loading_nx_matched}  {'%%%FOO%%%' if LTA else ''}''')
            return f_loading_nx_matched
        # else:
        #     ensure_printed(f'''not matched  {'%%%FOO%%%' if LTA else ''}''')
