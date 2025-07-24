import pandas as pd
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from dirsync import sync
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_f import is_f

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def classify_pnxs_to_pkg_video(pnx, without_walking=True):
    import inspect

    func_n = inspect.currentframe().f_code.co_name

    # pnx_todo가 유효한 d인지 확인
    if is_f(pnx=pnx):
        pk_print(f"{pnx} 는 정리할 수 있는 d가 아닙니다")
        return

    # f과 d get
    txt_to_exclude_list = [
        F_DB_YAML,
        F_SUCCESS_LOG,
        F_LOCAL_PKG_CACHE,
    ]
    if without_walking == False:
        d_list, f_list = get_sub_pnx_list(pnx=pnx, txt_to_exclude_list=txt_to_exclude_list)
    else:
        d_list, f_list = get_sub_pnx_list(pnx=pnx, txt_to_exclude_list=txt_to_exclude_list, without_walking=0)

    # f 처리
    x_allowed = [".mp4", '.avi', '.mkv', '.webm', '.mpg', '.flv', '.wmv']
    x_allowed = x_allowed + get_list_replaced_element_from_str_to_upper_case(working_list=x_allowed)
    pnx = get_pn(pnx)
    dst = rf"{pnx}\pkg_video"
    f = None
    for f in f_list:
        f = f[0]
        file_p = get_p(f)
        file_x = get_x(f).replace(".", "")  # 확장자에서 점(.) remove
        if file_x in [ext.replace(".", "") for ext in x_allowed]:  # x_allowed의 확장자와 비교
            ensure_pnx_made(pnx=dst, mode="d")
            move_pnx(pnx=f, d_dst=dst)
            pk_print(str_working=rf'''f="{f}"  {'%%%FOO%%%' if LTA else ''}''')
    pk_print(str_working=rf'''dst="{dst}"  {'%%%FOO%%%' if LTA else ''}''')
