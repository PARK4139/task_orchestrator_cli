

# import win32process
# import win32gui
# import pywin32
# import pywin32
# from project_database.test_project_database import MySqlUtil

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def cmd_to_os_like_person_as_admin(cmd):
    import platform
    import subprocess
    import traceback

    # todo : refactor : need refactorying
    # 검증도 필요하다. like_pserson 으로 동작 하지 않는다.
    if not platform.system() == 'Windows':
        cmd = cmd.replace("\\", "/")
    try:
        if platform.system() == 'Windows':
            # lines=subprocess.check_output('chcp 65001 >nul', shell=True).decode('utf-8').split('\n')
            # lines=subprocess.check_output(cmd, shell=True).decode('euc-kr').split('\n')
            lines = subprocess.check_output(cmd, shell=True).decode('utf-8').split('\n')
        return lines
    except:
        pk_print(working_str=rf'''traceback.format_exc()="{traceback.format_exc()}"  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        # os.system(cmd)
    return None
