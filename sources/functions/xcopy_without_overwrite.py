from sources.objects.pk_local_test_activate import LTA
from sources.functions.is_f import is_f
import logging


def xcopy_without_overwrite(pnx, pnx_future):
    import inspect
    import os
    import traceback

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    try:
        if os.path.exists(pnx_future):
            pnx_future = rf"{os.path.dirname(pnx_future)}\{os.path.basename(pnx)[0]}_{get_time_as_('%Y_%m_%d_%H_%M_%S_%f')}{os.path.basename(pnx)[1]}"
        ensure_command_executed_like_human_as_admin(rf'echo a | xcopy "{pnx}" "{pnx_future}" /e /h /k')
        if is_f(pnx):
            ensure_command_executed_like_human_as_admin(rf'echo f | xcopy "{pnx}" "{pnx_future}" /e /h /k')
        else:
            ensure_command_executed_like_human_as_admin(rf'echo d | xcopy "{pnx}" "{pnx_future}" /e /h /k')
    except Exception:
        print(rf"subprocess.CalledProcessError 가 발생하여 재시도를 수행합니다 {inspect.currentframe().f_code.co_name}")
        logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
