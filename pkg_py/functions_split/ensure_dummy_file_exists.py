from pkg_py.pk_system_object.PkMessages2025 import PkMessages2025

from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
from pkg_py.functions_split.get_x import get_x
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.get_p import get_p
from pkg_py.functions_split.ensure_func_info_saved import ensure_func_info_saved


def ensure_dummy_file_exists(file_pnx):
    import inspect
    file_pnx = get_pnx_os_style(file_pnx)
    ensure_pnx_made(get_p(file_pnx), mode="d")
    func_n = inspect.currentframe().f_code.co_name
    if not does_pnx_exist(file_pnx):
        x = get_x(file_pnx)
        with open(file_pnx, 'wb') as f:
            f.write(b'\x00')  # 1바이트 더미
        func_data = {
            "n": func_n,
            "state": PkMessages2025.success,
            "file_pnx": file_pnx,
        }
        ensure_func_info_saved(func_n, func_data)
        # return func_data
        # 이제 return 안하고 db 에서 가져와도 됨.
