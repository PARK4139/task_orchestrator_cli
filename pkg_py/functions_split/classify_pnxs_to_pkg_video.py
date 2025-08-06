

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.ensure_printed import ensure_printed


def classify_pnxs_to_pkg_video(pnx, without_walking=True):
    import inspect
    func_n = inspect.currentframe().f_code.co_name

    # target_pnx가 유효한 _d_인지 확인
    if is_f(pnx=pnx):
        ensure_printed(f"{pnx} 는 정리할 수 있는 _d_가 아닙니다")
        return

    # f과 _d_ get
    txt_to_exclude_list = [
        F_DB_YAML,
        F_SUCCESS_LOG,
        F_LOCAL_PKG_CACHE_PRIVATE,
    ]
    if without_walking == False:
        dir_pnxs, file_pnxs = get_sub_pnx_list(pnx=pnx, txt_to_exclude_list=txt_to_exclude_list)
    else:
        dir_pnxs, file_pnxs = get_sub_pnx_list(pnx=pnx, txt_to_exclude_list=txt_to_exclude_list, without_walking=0)

    # f 처리
    x_allowed = [".mp4", '.avi', '.mkv', '.webm', '.mpg', '.flv', '.wmv']
    x_allowed = x_allowed + get_list_replaced_element_from_str_to_upper_case(working_list=x_allowed)
    pnx = get_pn(pnx)
    dst = rf"{pnx}\pkg_video"
    file_pnx = None
    for file_pnx in file_pnxs:
        file_pnx = file_pnx[0]
        file_p = get_p(file_pnx)
        file_x = get_x(file_pnx).replace(".", "")  # 확장자에서 점(.) remove
        if file_x in [ext.replace(".", "") for ext in x_allowed]:  # x_allowed의 확장자와 비교
            ensure_pnx_made(pnx=dst, mode="d")
            ensure_pnx_moved(pnx=file_pnx, d_dst=dst)
            ensure_printed(str_working=rf'''file_pnx="{file_pnx}"  {'%%%FOO%%%' if LTA else ''}''')
    ensure_printed(str_working=rf'''dst="{dst}"  {'%%%FOO%%%' if LTA else ''}''')
