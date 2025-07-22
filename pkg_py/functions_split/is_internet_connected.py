

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def is_internet_connected():
    # if not ping(ip='google.com'):
    if not ping(ip='8.8.8.8'):
        pk_print(f'''internet not connected. {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        return 0
    return 1
