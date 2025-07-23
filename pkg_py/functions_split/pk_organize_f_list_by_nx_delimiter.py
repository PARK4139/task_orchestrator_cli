import tarfile
from selenium.common.exceptions import ElementClickInterceptedException
from prompt_toolkit import PromptSession
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.pk_print_state import pk_print_state

from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
from base64 import b64encode
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.pk_system_object.local_test_activate import LTA

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def pk_organize_f_list_by_nx_delimiter(d_working, nx_delimiter):
    import inspect
    import os

    import shutil

    d_dst = os.path.join(d_working, nx_delimiter)
    if not os.path.exists(d_dst):
        os.makedirs(d_dst)
        pk_print(f'''d_dst={d_dst}  {'%%%FOO%%%' if LTA else ''}''')

    f_list_moved_flag = False
    for f_nx in os.listdir(d_working):
        f_filtered = os.path.join(d_working, f_nx)

        if not os.path.isfile(f_filtered):  # _d_는 무시
            continue

        if nx_delimiter in f_nx:
            f_target = os.path.join(d_dst, f_nx)

            if os.path.exists(f_target):
                pk_print(f"이동 불가: '{f_nx}' f이 이미 존재합니다.", print_color='red')
                continue

            shutil.move(f_filtered, f_target)
            func_n = inspect.currentframe().f_code.co_name
            stamp_func_n = rf'''[{func_n}()]'''
            pk_print(f"'{stamp_func_n} {f_nx}' f이 '{d_dst}'로 이동되었습니다.")
            f_list_moved_flag = True

    if not f_list_moved_flag:
        pk_print(f"'{nx_delimiter}'를 포함하는 f이 없습니다.")
