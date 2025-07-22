from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def move_without_overwrite_via_robocopy(src, dst):  # 명령어 자체가 안되는데 /mir 은 되는데 /move 안된다
    import inspect
    import os
    import traceback

    src = src
    func_n = inspect.currentframe().f_code.co_name
    try:
        pk_print(f'타겟이동 시도')
        # run_via_cmd_exe(rf'robocopy "{pnx_todo}" "{dst}" /MOVE')
        if os.path.exists(rf'{dst}\{os.path.dirname(src)}'):
            move_pnx_to_pk_recycle_bin(src)

    except Exception:
        pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
