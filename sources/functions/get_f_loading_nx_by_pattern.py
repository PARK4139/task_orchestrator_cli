
from sources.objects.pk_local_test_activate import LTA
import logging



def get_f_loading_nx_by_pattern(pattern):
    import re

    window_opened_list = get_windows_opened_with_hwnd()
    for window_opened in window_opened_list:
        match = re.search(pattern, window_opened)
        if match:
            f_loading_nx_matched = match.group(1)
            logging.debug(f'''f_loading_nx_matched={f_loading_nx_matched}  {'%%%FOO%%%' if LTA else ''}''')
            return f_loading_nx_matched
        # else:
        #     logging.debug(f'''not matched  {'%%%FOO%%%' if LTA else ''}''')
