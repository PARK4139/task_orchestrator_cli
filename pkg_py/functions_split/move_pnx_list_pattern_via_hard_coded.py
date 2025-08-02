import colorama
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.system_object.files import F_HISTORICAL_PNX
from os.path import dirname
from functools import lru_cache
from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def move_pnx_list_pattern_via_hard_coded():
    import inspect

    func_n = inspect.currentframe().f_code.co_name

    # pnx=rf"D:\#기타\pkg_dirs"
    # pnx=rf"D:\#기타\pkg_files"
    pnx = rf"D:\#기타"
    pnx = rf"D:\#기타\pkg_files\pkg_video"

    txt_to_exclude_list = [
        F_DB_YAML,
        F_SUCCESS_LOG,
        F_LOCAL_PKG_CACHE,
    ]

    # d_list, f_list=get_sub_pnxs_without_walking(pnx=item_pnx, txt_to_exclude_list=txt_to_exclude_list)
    d_list, f_list = get_sub_pnx_list(pnx=pnx, txt_to_exclude_list=txt_to_exclude_list)

    # pnxs=d_list
    pnxs = f_list

    # pattern 대체 timestamp 를 붙이기
    # pnxs_and_pnxs_new=[]
    # for item in pnxs:
    #     pattern_new=''
    #     item_without_reg=re.sub(pattern, pattern_new, item[0]) # 날짜/시간 패턴을 모두 remove
    #     item_pn=get_pn(item_without_reg)
    #     item_x=get_x(item_without_reg)
    #     timestamp=get_time_as_("now")
    #     item_new=""
    #     if is_file(item[0]):
    #         item_new=f"{item_pn}_{timestamp}.{item_x}"
    #     else:
    #         item_new=f"{item_pn}_{timestamp}{item_x}"
    #     pnxs_and_pnxs_new.append([item[0], item_new])

    # [문자열] 패턴은 f명의 맨앞이나 뒤로 이동
    pnxs_and_pnxs_new = []
    for item in pnxs:
        item_pnx = item[0]
        pattern = r'(\[.*?\])'
        # item_pnx_new=get_str_moved_pattern_to_front(pattern=pattern, item_pnx=item_pnx)
        item_pnx_new = get_f_n_moved_pattern(pattern=pattern, pnx_working=item_pnx, mode_front=0)
        if item_pnx != item_pnx_new:  # item_pnx item_pnx_new가 다르면 추가
            pnxs_and_pnxs_new.append([item_pnx, item_pnx_new])

    # 확인
    ensure_iterable_printed_as_vertical(item_iterable=pnxs_and_pnxs_new, item_iterable_n="바꿀 대상")
    ensure_printed(str_working=rf'''len(pnxs_and_pnxs_new)="{len(pnxs_and_pnxs_new)}"  {'%%%FOO%%%' if LTA else ''}''')

    # 적용
    rename_pnxs(pnx_list=pnxs_and_pnxs_new)
