
continue
d_dst = os.path.join(d_working, nx_delimiter)
def pk_organize_f_list_by_nx_delimiter(d_working, nx_delimiter):
f_filtered = os.path.join(d_working, f_nx)
f_list_moved_flag = False
f_list_moved_flag = True
f_target = os.path.join(d_dst, f_nx)
for f_nx in os.listdir(d_working):
from PIL import Image
from base64 import b64encode
from concurrent.futures import ThreadPoolExecutor
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.print import pk_print
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.print_state import pk_print_state
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from prompt_toolkit import PromptSession
from selenium.common.exceptions import ElementClickInterceptedException
func_n = inspect.currentframe().f_code.co_name
if not f_list_moved_flag:
if not os.path.exists(d_dst):
if not os.path.isfile(f_filtered):  # _d_는 무시
if nx_delimiter in f_nx:
if os.path.exists(f_target):
import inspect
import os
import shutil
import tarfile
os.makedirs(d_dst)
pk_print(f"'{nx_delimiter}'를 포함하는 f이 없습니다.")
pk_print(f"'{stamp_func_n} {f_nx}' f이 '{d_dst}'로 이동되었습니다.")
pk_print(f"이동 불가: '{f_nx}' f이 이미 존재합니다.", print_color='red')
pk_print(f'''d_dst={d_dst}  {'%%%FOO%%%' if LTA else ''}''')
shutil.move(f_filtered, f_target)
stamp_func_n = rf'''[{func_n}()]'''
