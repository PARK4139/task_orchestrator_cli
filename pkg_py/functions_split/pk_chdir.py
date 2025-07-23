

# import win32gui
# import win32gui

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def pk_chdir(d_dst):
    import os

    d_before = os.getcwd()
    os.chdir(path=d_dst)
    d_after = os.getcwd()
    if d_before == d_after:
        pk_print(working_str=rf''' {'%%%FOO%%%' if LTA else ''}''', print_color='red')
