

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.simple_module.part_014_pk_print import pk_print


def cmd_to_os_v_1_0_1(cmd: str, mode="", encoding=None):
    import subprocess
    import traceback

    from enum import Enum
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    encoding: Enum

    std_list = []
    if mode == "a":
        pk_print(working_str=rf'''cmd="{cmd}" mode="async"  {'%%%FOO%%%' if LTA else ''}''')
    else:
        pk_print(working_str=rf'''cmd="{cmd}" mode="동기"  {'%%%FOO%%%' if LTA else ''}''')
    if encoding != Encoding.UTF8:
        encoding = Encoding.CP949  # UTF8 가 아니면 CP949 로 강제
    if mode == "a":  # async
        subprocess.Popen(args=cmd, shell=True, encoding=encoding.value)
        return
    else:
        try:
            process = subprocess.Popen(
                args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding=encoding.value,
                # text=True,  # 텍스트 모드 활성화
            )
        except UnicodeDecodeError:
            # 실패하면 UTF-8로 변경하여 시도
            encoding = Encoding.UTF8
            process = subprocess.Popen(args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding=encoding.value)

        try:
            stdout, stderr = process.communicate()
            if stdout:
                for std_str in stdout.splitlines():
                    std_list.append(std_str.strip())
                    # pk_print(f"STD_OUT: {std_str.strip()}", print_color='green')
                    pk_print(f"STD_OUT: {std_str.strip()}")
            if stderr:
                for std_str in stderr.splitlines():
                    std_list.append(std_str.strip())
                    pk_print(f"STD_ERR: {std_str.strip()}", print_color='red')
        except:
            pk_print(f'''[{func_n}()] {traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

        finally:
            try:
                if process and process.poll() is None:
                    process.terminate()
            except:
                pk_print(f'''[{func_n}()] {traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        return std_list
