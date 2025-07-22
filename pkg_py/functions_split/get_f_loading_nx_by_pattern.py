
from pkg_py.pk_interface_graphic_user import get_windows_opened
from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print



def get_f_loading_nx_by_pattern(pattern):
    import re

    window_opened_list = get_windows_opened()
    for window_opened in window_opened_list:
        match = re.search(pattern, window_opened)
        if match:
            f_loading_nx_matched = match.group(1)
            pk_print(f'''f_loading_nx_matched={f_loading_nx_matched}  {'%%%FOO%%%' if LTA else ''}''')
            return f_loading_nx_matched
        # else:
        #     pk_print(f'''not matched  {'%%%FOO%%%' if LTA else ''}''')
