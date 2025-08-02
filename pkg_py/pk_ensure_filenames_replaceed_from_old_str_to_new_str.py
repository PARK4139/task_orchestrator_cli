__author__ = 'pk == junghoon.park'

# from pkg_py.system_object.directories import D_PK_WORKING
#
#, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
# from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.print_red import print_red
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.input import input
from pkg_py.functions_split.get_nx_validated import get_nx_validated
from pkg_py.functions_split.get_no_blank_str_working_validated import get_no_blank_str_working_validated
from pkg_py.functions_split.get_pnx_validated import get_pnx_validated
from pkg_py.functions_split.replace_f_nx_list_from_old_str_to_new_str import replace_f_nx_list_from_old_str_to_new_str

if __name__ == "__main__":
    try:
        import traceback

        from colorama import init as pk_colorama_init

        ensure_colorama_initialized_once()

        d_working = pk_input(str_working=rf'd_working=', limit_seconds=60, return_default=D_PK_WORKING, get_input_validated=get_pnx_validated)
        while 1:
            old_str = pk_input(str_working="old_str=", limit_seconds=60, return_default='%%%OLD_STR%%%', get_input_validated=get_nx_validated)
            old_str = get_no_blank_str_working_validated(old_str)
            new_str = pk_input(str_working="new_str=", limit_seconds=60, return_default='%%%NEW_STR%%%', get_input_validated=get_nx_validated)
            new_str = get_no_blank_str_working_validated(new_str)
            pk_replace_f_nx_list_from_old_str_to_new_str(d_working=d_working, old_str=old_str, new_str=new_str)

    except:

        traceback_format_exc_list = traceback.format_exc().split("\n")
        print_red(PK_UNDERLINE)
        for line in traceback_format_exc_list:
            print_red(f'{STAMP_UNIT_TEST_EXCEPTION_DISCOVERED} {line}')
        print_red(PK_UNDERLINE)

    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        
