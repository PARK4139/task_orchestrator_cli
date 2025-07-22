from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def ensure_python_pkg_to_remote_os(py_pkg_n, **config_remote_os):
    # 파이썬 모듈 설치기능
    import importlib

    if not is_internet_connected():
        pk_print(f'''can not install python module for internet not connected  {'%%%FOO%%%' if LTA else ''}''',
                 print_color='red')
        raise

    # todo if config_remote_os['ip'] == 'localhost' or local private ip or local public ip:
    try:
        return importlib.import_module(py_pkg_n)
    except ModuleNotFoundError:
        pk_print(f"[ WARN ] '{py_pkg_n}' 모듈이 없습니다.", print_color='yellow')
        yn = input(f">> '{py_pkg_n}'를 설치하시겠습니까? (y/n): ").strip().lower()
        if yn != 'y':
            pk_print(f"[ ABORTED ] '{py_pkg_n}' 설치를 건너뜁니다.", print_color='yellow')
            return
        try:
            install_py_module(py_pkg_n)
            # todo installed 목록에서 확인 후 green
            pk_print(f"'{py_pkg_n}' installation", print_color='green')
            return importlib.import_module(py_pkg_n)
        except Exception as e:
            pk_print(f"'{py_pkg_n}' installation {e}", print_color='red')
            raise
