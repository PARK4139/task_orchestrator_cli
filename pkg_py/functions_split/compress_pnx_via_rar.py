

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.system_object.encodings import Encoding

from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_d_working import get_d_working


from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.encodings import Encoding
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_d_working import get_d_working


def compress_pnx_via_rar(src, dst, with_timestamp=1):
    import os.path
    from datetime import datetime

    import inspect

    # todo ensure wsl

    func_n = inspect.currentframe().f_code.co_name

    # 전처리
    # src = get_pnx_windows_style(pnx=src)
    src = get_pnx_unix_style(pnx=src)
    dst = get_pnx_unix_style(pnx=dst)

    # 정의
    d_working = get_d_working()

    pnx = src
    p = get_p(pnx)
    n = get_n(pnx)
    nx = get_nx(pnx)
    x = get_x(pnx)
    x = x.lstrip('.')  # 확장자에서 점 remove

    rar = "rar"  # via rar
    timestamp = ""
    if with_timestamp:
        timestamp = rf"{PK_BLANK}{datetime.now().strftime('%Y %m %d %H %M %S')}"
    pn_rar = rf"{p}/{n}.{rar}"
    dst_nx_rar = rf"{dst}/{n}.{rar}"
    dst_nx_timestamp_rar = rf"{dst}/{n}{timestamp}.{rar}"

    # 로깅
    # ensure_printed(str_working=rf'''dst="{dst}"  {'%%%FOO%%%' if LTA else ''}''')
    # ensure_printed(str_working=rf'''pnx="{pnx}"  {'%%%FOO%%%' if LTA else ''}''')
    # ensure_printed(str_working=rf'''p="{p}"  {'%%%FOO%%%' if LTA else ''}''')
    # ensure_printed(str_working=rf'''n="{n}"  {'%%%FOO%%%' if LTA else ''}''')
    # ensure_printed(str_working=rf'''nx="{nx}"  {'%%%FOO%%%' if LTA else ''}''')
    # ensure_printed(str_working=rf'''x="{x}"  {'%%%FOO%%%' if LTA else ''}''')
    # ensure_printed(str_working=rf'''dst_nx_rar="{dst_nx_rar}"  {'%%%FOO%%%' if LTA else ''}''')
    # ensure_printed(str_working=rf'''dst_nx_timestamp_rar="{dst_nx_timestamp_rar}"  {'%%%FOO%%%' if LTA else ''}''')
    # ensure_printed(string = rf'''dst_nx_timestamp_rar="{dst_nx_timestamp_rar}"  {'%%%FOO%%%' if LTA else ''}''')

    # 삭제
    move_pnx_to_pk_recycle_bin(pnx=pn_rar)

    # 생성
    ensure_pnx_made(pnx=dst, mode='d')

    # 이동
    os.chdir(p)

    # 압축
    wsl_pn_rar = get_pnx_wsl_unix_style(pnx=pn_rar)
    cmd = f'wsl rar a "{wsl_pn_rar}" "{nx}"'
    ensure_command_excuted_to_os(cmd, encoding=Encoding.CP949)

    # copy
    copy_pnx_with_overwrite(pnx=pn_rar, dst=dst)

    # rename
    rename_pnx(src=dst_nx_rar, pnx_new=dst_nx_timestamp_rar)

    ensure_printed(str_working=rf'''wsl_pn_rar="{wsl_pn_rar}"  {'%%%FOO%%%' if LTA else ''}''')
    dst_nx = rf"{dst}/{nx}"
    ensure_printed(str_working=rf'''desktop_nx="{dst_nx}"  {'%%%FOO%%%' if LTA else ''}''')

    # remove
    move_pnx_to_pk_recycle_bin(pnx=dst_nx)
    move_pnx_to_pk_recycle_bin(pnx=dst_nx_rar)

    # chdir
    os.chdir(d_working)

    # logging
    ensure_printed(str_working=rf'''dst_nx_rar="{dst_nx_rar}"  {'%%%FOO%%%' if LTA else ''}''')
    ensure_printed(str_working=rf'''[{func_n}] dst_nx_timestamp_rar="{dst_nx_timestamp_rar}"  {'%%%FOO%%%' if LTA else ''}''',
             print_color='green')

    return dst_nx_timestamp_rar
