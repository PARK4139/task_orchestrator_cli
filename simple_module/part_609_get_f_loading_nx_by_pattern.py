from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_307_get_window_opened_list import get_window_opened_list


def get_f_loading_nx_by_pattern(pattern):
    import re

    window_opened_list = get_window_opened_list()
    for window_opened in window_opened_list:
        match = re.search(pattern, window_opened)
        if match:
            f_loading_nx_matched = match.group(1)
            pk_print(f'''f_loading_nx_matched={f_loading_nx_matched}  {'%%%FOO%%%' if LTA else ''}''')
            return f_loading_nx_matched
        # else:
        #     pk_print(f'''not matched  {'%%%FOO%%%' if LTA else ''}''')
