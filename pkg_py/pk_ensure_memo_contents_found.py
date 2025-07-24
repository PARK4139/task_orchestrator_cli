import traceback

from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.pk_sleep import pk_sleep
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.files import F_MEMO_HOW_PK
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE


def found_memo_contents():
    from pkg_py.functions_split.ensure_f_list_change_stable import ensure_files_stable_after_change
    from pkg_py.functions_split.get_os_n import get_os_n
    from pkg_py.functions_split.chcp_65001 import chcp_65001
    from pkg_py.functions_split.print_memo_titles import print_memo_titles

    if get_os_n() == 'windows':
        chcp_65001()

    f_memo = rf'{F_MEMO_HOW_PK}'
    if not does_pnx_exist(f_memo):
        pk_print(f'''{f_memo} does not exist %%%FOO%%%''', print_color='red')
        return

    # line_list = get_list_from_f_pnx(f_pnx=f_memo)
    # line_list = get_str_from_list(item_list=line_list)
    # line_str = line_list
    # pk_print(f'''len(line_list)={len(line_list)} %%%FOO%%%''')
    # pk_print(f'''len(line_str)={len(line_str)} %%%FOO%%%''')
    # data = line_str
    # txt_highlighted = [
    #     "%%%FOO%%%",
    #     'mkr_',
    # ]
    # print_with_highlighted(txt_whole=data, txt_highlighted_list=txt_highlighted)

    # txt_str = input("Press Enter to continue...")
    # write_str_to_f_pnx(txt_str=txt_str, f_pnx=f_memo)

    f_monitored_list = [
        f_memo
    ]
    while 1:
        if ensure_files_stable_after_change(f_list=f_monitored_list, limit_seconds=30):
            print_memo_titles(f=f_memo)
        pk_sleep(milliseconds=900)


if __name__ == "__main__":
    try:
        # todo
        found_memo_contents()
        #     print memo title_list
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
