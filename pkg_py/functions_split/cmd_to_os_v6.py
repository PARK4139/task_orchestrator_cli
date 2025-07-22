

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.stamps import STAMP_ATTEMPTED
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical


def cmd_to_os_v6(cmd: str, mode="", encoding=None, mode_with_window=1):
    def decode_with_fallback(byte_data, primary_encoding):
        try:
            return byte_data.decode(primary_encoding)
        except UnicodeDecodeError:
            return byte_data.decode('cp949', errors='replace')

    if encoding is None:
        encoding = Encoding.UTF8
    if mode == "":
        mode = 'sync'
    if mode == "a":
        mode = 'async'
    if LTA:
        pk_print(working_str=rf'''{STAMP_ATTEMPTED} {cmd} encoding={encoding:5s} mode={mode}''')
    std_list = []
    if mode == "async":
        if mode_with_window:
            import subprocess
            subprocess.Popen(args=cmd, shell=True)
            return
        else:
            import subprocess
            subprocess.Popen(args=cmd, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
            return
    else:
        try:
            process = None
            if mode_with_window:
                import subprocess
                process = subprocess.Popen(args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                import subprocess
                process = subprocess.Popen(args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
            stdout_bytes, stderr_bytes = process.communicate()
            stdout = None
            stderr = None
            try:
                stdout = decode_with_fallback(stdout_bytes, encoding.value)
                stderr = decode_with_fallback(stderr_bytes, encoding.value)
            except AttributeError:
                stdout = decode_with_fallback(stdout_bytes, encoding)
                stderr = decode_with_fallback(stderr_bytes, encoding)

            if stdout:
                std_list.extend(line.strip() for line in stdout.splitlines())
            if stderr:
                std_list.extend(line.strip() for line in stderr.splitlines())

            print_iterable_as_vertical(item_iterable=std_list, item_iterable_n=rf'{cmd}')

        except Exception:
            import traceback
            pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

        finally:
            try:
                if process and process.poll() is None:
                    process.terminate()

                # 필터링
                # useless_list = get_list_from_f(f=F_ALIAS_CMD) + [" {'%%%FOO%%%' if LTA else ''}", ""]
                # std_list = [x for x in std_list if x not in useless_list]

            except Exception:
                import traceback
                pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

        return std_list
