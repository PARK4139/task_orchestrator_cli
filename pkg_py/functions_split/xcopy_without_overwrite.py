from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.ensure_printed import ensure_printed


def xcopy_without_overwrite(pnx, pnx_future):
    import inspect
    import os
    import traceback

    func_n = inspect.currentframe().f_code.co_name
    try:
        if os.path.exists(pnx_future):
            pnx_future = rf"{os.path.dirname(pnx_future)}\{os.path.basename(pnx)[0]}_{get_time_as_('%Y_%m_%d_%H_%M_%S_%f')}{os.path.basename(pnx)[1]}"
        cmd_to_os_like_person_as_admin(rf'echo a | xcopy "{pnx}" "{pnx_future}" /e /h /k')
        if is_f(pnx):
            cmd_to_os_like_person_as_admin(rf'echo f | xcopy "{pnx}" "{pnx_future}" /e /h /k')
        else:
            cmd_to_os_like_person_as_admin(rf'echo d | xcopy "{pnx}" "{pnx_future}" /e /h /k')
    except Exception:
        print(rf"subprocess.CalledProcessError 가 발생하여 재시도를 수행합니다 {inspect.currentframe().f_code.co_name}")
        ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
