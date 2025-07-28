import traceback

from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.functions_split.ensure_files_stable_after_change import ensure_files_stable_after_change
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_slept import ensure_slept
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.files import F_MEMO_HOW_PK
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE


def ensure_memo_contents_found():
    from pkg_py.functions_split.get_os_n import get_os_n
    from pkg_py.functions_split.chcp_65001 import chcp_65001
    from pkg_py.functions_split.ensure_memo_titles_printed import ensure_memo_titles_printed

    if get_os_n() == 'windows':
        chcp_65001()

    f_memo = rf'{F_MEMO_HOW_PK}'
    if not does_pnx_exist(f_memo):
        ensure_printed(f'''{f_memo} does not exist %%%FOO%%%''', print_color='red')
        return

    # line_list = get_list_from_f_pnx(f_pnx=f_memo)
    # line_list = get_str_from_list(item_list=line_list)
    # line_str = line_list
    # ensure_printed(f'''len(line_list)={len(line_list)} %%%FOO%%%''')
    # ensure_printed(f'''len(line_str)={len(line_str)} %%%FOO%%%''')
    # data = line_str
    # txt_highlighted = [
    #     "%%%FOO%%%",
    #     'mkr_',
    # ]
    # print_with_highlighted(txt_whole=data, txt_highlighted_list=txt_highlighted)

    # txt_str = input("Press Enter to continue...")
    # ensure_str_writen_to_f_pnx(txt_str=txt_str, f_pnx=f_memo)

    # f_monitored_list = [
    #     f_memo
    # ]
    # while 1:
    #     if ensure_files_stable_after_change(f_list=f_monitored_list, stable_seconds_limit=30):
    #         ensure_memo_titles_printed(f=f_memo)
    #     ensure_slept(milliseconds=900)
    ensure_memo_titles_printed(f=f_memo)

if __name__ == "__main__":
    try:
        # todo
        ensure_memo_contents_found()
        #     print memo title_list
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
