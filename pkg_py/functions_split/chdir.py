
# import win32gui
d_after = os.getcwd()
d_before = os.getcwd()
def pk_chdir(d_dst):
from pkg_py.functions_split.print import pk_print
from pkg_py.pk_system_object.local_test_activate import LTA
if d_before == d_after:
import os
os.chdir(path=d_dst)
pk_print(working_str=rf''' {'%%%FOO%%%' if LTA else ''}''', print_color='red')
