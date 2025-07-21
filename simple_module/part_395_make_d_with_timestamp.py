import zipfile
import urllib
import pickle
import os
from zipfile import BadZipFile
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from datetime import date
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_014_pk_print import pk_print

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def make_d_with_timestamp(d_nx, dst):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    try:
        # 업무명
        d_nx = d_nx.strip()
        d_nx = d_nx.replace("\"", "")
        pk_print(
            f'''[ {get_time_as_('now')} ] work_n={d_nx}  {'%%%FOO%%%' if LTA else ''}''')
        if d_nx == "":
            pk_print(
                f'''[ {get_time_as_('now')} ] work_n가 입력되지 않았습니다  {'%%%FOO%%%' if LTA else ''}''')
            return

        # 경로
        dst = dst.strip()
        dst = get_pnx_os_style(dst)
        if is_pnx_required(dst):
            return
        pk_print(working_str=rf'''dst="{dst}"  {'%%%FOO%%%' if LTA else ''}''')

        # 타임스템프 생성
        timestamp = get_time_as_("yyyy MM dd (weekday) HH mm")
        pnx_new = rf"{dst}\{timestamp} {d_nx}"
        pnx_new = get_pnx_os_style(pnx_new)
        pk_print(working_str=rf'''pnx_new="{pnx_new}"  {'%%%FOO%%%' if LTA else ''}''')

        # d 생성 및 f 탐색기 열기 # todo
        ensure_pnx_made(pnx=pnx_new, mode="d")
        cmd = rf'explorer "{pnx_new}"'
        pk_print(working_str=rf'''cmd="{cmd}"  {'%%%FOO%%%' if LTA else ''}''')
        # cmd_run(cmd=cmd)
        # print_list_as_vertical(get_windows_opened(), items_name="get_windows_opened()")

        return
    except Exception as e:
        pk_print(f"Error: {str(e)}")
