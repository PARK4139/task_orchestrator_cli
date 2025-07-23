

# import win32process
# from project_database.test_project_database import MySqlUtil

from pkg_py.pk_system_object.is_os_windows import is_os_windows

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.pk_print import pk_print


def get_user_n_wsl_via_whoami(wsl_disto_n):
    std_out_list = None
    if is_os_windows():
        std_out_list = cmd_to_os(f'wsl -d {wsl_disto_n} whoami')
    else:
        std_out_list = cmd_to_os(rf'whoami', encoding='utf-8')
    std_out_list = get_list_without_none_and_duplicates(std_out_list)
    user_n_list = std_out_list
    if len(std_out_list) == 1:
        pk_print(rf'''users_wsl[0]="{user_n_list[0]}"  {'%%%FOO%%%' if LTA else ''}''')
        return user_n_list[0]
    else:
        pk_print(f"현재 wsl에 로그인된 사용자가 한명이 아닙니다 user_n_list=[{user_n_list}]", print_color='red')
        raise
