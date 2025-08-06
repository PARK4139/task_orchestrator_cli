from pkg_py.functions_split.ensure_process_killed import ensure_process_killed
from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
from pkg_py.functions_split.get_d_working_in_python import get_pwd_in_python
from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
from pkg_py.functions_split.ensure_copied import ensure_copied
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.is_os_linux import is_os_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.map_massages import PkMessages2025


import traceback

from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
from pkg_py.functions_split.get_nx import get_nx
import ipdb

from pkg_py.functions_split.ensure_console_debuggable import ensure_console_debuggable
from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
from pkg_py.system_object.directories  import D_PROJECT
from pkg_py.system_object.local_test_activate import LTA
# pk_#

if __name__ == "__main__":
    try:
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))

        pwd = get_pwd_in_python()
        ensure_printed(f'''pwd={pwd} {'%%%FOO%%%' if LTA else ''}''')

        # OS별 클립보드 복사 처리
        if is_os_windows():
            ensure_copied(pwd)
        elif is_os_linux():
            # Linux에서는 xclip 또는 xsel 사용
            try:
                import subprocess
                subprocess.run(['xclip', '-selection', 'clipboard'], input=pwd.encode(), check=True)
            except (subprocess.CalledProcessError, FileNotFoundError):
                try:
                    subprocess.run(['xsel', '--clipboard'], input=pwd.encode(), check=True)
                except (subprocess.CalledProcessError, FileNotFoundError):
                    # 클립보드 도구가 없으면 출력만
                    ensure_printed(f"{PkMessages2025.CLIPBOARD_COPY_FAILED}. {PkMessages2025.PATH}: {pwd}")
        else:
            # macOS에서는 pbcopy 사용
            try:
                import subprocess
                subprocess.run(['pbcopy'], input=pwd.encode(), check=True)
            except (subprocess.CalledProcessError, FileNotFoundError):
                ensure_printed(f"{PkMessages2025.CLIPBOARD_COPY_FAILED}. {PkMessages2025.PATH}: {pwd}")

        ensure_program_suicided(__file__) # pk_option

        if LTA:
            ensure_console_debuggable(ipdb)
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)

