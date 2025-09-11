from sources.objects.pk_local_test_activate import LTA
import logging


def move_without_overwrite_via_robocopy(src, dst):  # 명령어 자체가 안되는데 /mir 은 되는데 /move 안된다
    import inspect
    import os
    import traceback

    src = src
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    try:
        logging.debug(f'타겟이동 시도')
        # run_via_cmd_exe(rf'robocopy "{pnx_todo}" "{dst}" /MOVE')
        if os.path.exists(rf'{dst}\{os.path.dirname(src)}'):
            ensure_pnxs_move_to_recycle_bin(src)

    except Exception:
        logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
