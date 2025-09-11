def compress_pnx_via_rar(src, dst, with_timestamp=1):
    import logging
    import os.path
    import traceback
    from datetime import datetime

    from functions import ensure_pnx_made, ensure_spoken
    from functions.copy_pnx_with_overwrite import copy_pnx_with_overwrite
    from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose
    from functions.ensure_pnxs_move_to_recycle_bin import ensure_pnxs_move_to_recycle_bin
    from functions.get_caller_n import get_caller_n
    from functions.get_n import get_n
    from functions.get_p import get_p
    from functions.get_x import get_x
    from functions.rename_pnx import rename_pnx
    from objects.pk_etc import PK_BLANK
    from sources.functions.ensure_command_executed import ensure_command_executed
    from sources.functions.get_d_working import get_d_working
    from sources.functions.get_nx import get_nx
    from sources.functions.get_pnx_unix_style import get_pnx_unix_style
    from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
    from sources.objects.encodings import Encoding
    from sources.objects.pk_local_test_activate import LTA

    try:

        # todo ensure wsl

        func_n = get_caller_n()

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
        # logging.debug(rf'''dst="{dst}"  {'%%%FOO%%%' if LTA else ''}''')
        # logging.debug(rf'''pnx="{pnx}"  {'%%%FOO%%%' if LTA else ''}''')
        # logging.debug(rf'''p="{p}"  {'%%%FOO%%%' if LTA else ''}''')
        # logging.debug(rf'''n="{n}"  {'%%%FOO%%%' if LTA else ''}''')
        # logging.debug(rf'''nx="{nx}"  {'%%%FOO%%%' if LTA else ''}''')
        # logging.debug(rf'''x="{x}"  {'%%%FOO%%%' if LTA else ''}''')
        # logging.debug(rf'''dst_nx_rar="{dst_nx_rar}"  {'%%%FOO%%%' if LTA else ''}''')
        # logging.debug(rf'''dst_nx_timestamp_rar="{dst_nx_timestamp_rar}"  {'%%%FOO%%%' if LTA else ''}''')
        # logging.debug(string = rf'''dst_nx_timestamp_rar="{dst_nx_timestamp_rar}"  {'%%%FOO%%%' if LTA else ''}''')

        # 삭제
        ensure_pnxs_move_to_recycle_bin(pnxs=[pn_rar])

        # 생성
        ensure_pnx_made(pnx=dst, mode='d')

        # 이동
        os.chdir(p)

        # 압축
        wsl_pn_rar = get_pnx_wsl_unix_style(pnx=pn_rar)
        cmd = f'wsl rar a "{wsl_pn_rar}" "{nx}"'
        ensure_command_executed(cmd, encoding=Encoding.CP949)

        # copy
        copy_pnx_with_overwrite(pnx=pn_rar, dst=dst)

        # rename
        rename_pnx(src=dst_nx_rar, pnx_new=dst_nx_timestamp_rar)

        logging.debug(rf'''wsl_pn_rar="{wsl_pn_rar}"  {'%%%FOO%%%' if LTA else ''}''')
        dst_nx = rf"{dst}/{nx}"
        logging.debug(rf'''desktop_nx="{dst_nx}"  {'%%%FOO%%%' if LTA else ''}''')

        # remove
        ensure_pnxs_move_to_recycle_bin(pnxs=[dst_nx])
        ensure_pnxs_move_to_recycle_bin(pnxs=[dst_nx_rar])

        # chdir
        os.chdir(d_working)

        # logging
        logging.debug(rf'''dst_nx_rar="{dst_nx_rar}"  {'%%%FOO%%%' if LTA else ''}''')
        logging.debug(rf'''[{func_n}] dst_nx_timestamp_rar="{dst_nx_timestamp_rar}"  {'%%%FOO%%%' if LTA else ''}''')

        return dst_nx_timestamp_rar
    except:
        ensure_debug_loged_verbose(traceback)
    finally:
        ensure_spoken(wait=True)
