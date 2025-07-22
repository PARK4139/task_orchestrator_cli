__author__ = 'pk == junghoon.park'

# from pkg_py.pk_system_object.directories import D_WORKING
#
#, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
# from pkg_py.pk_system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.print_red import print_red
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.pk_input import pk_input
from pkg_py.functions_split.get_nx_validated import get_nx_validated
from pkg_py.functions_split.get_no_blank_working_str_validated import get_no_blank_working_str_validated
from pkg_py.functions_split.get_pnx_validated import get_pnx_validated
from pkg_py.functions_split.pk_replace_f_nx_list_from_old_str_to_new_str import pk_replace_f_nx_list_from_old_str_to_new_str

if __name__ == "__main__":
    try:
        import traceback

        from colorama import init as pk_colorama_init

        pk_colorama_init_once()

        d_working = pk_input(working_str=rf'd_working=', limit_seconds=60, return_default=D_WORKING, get_input_validated=get_pnx_validated)
        while 1:
            old_str = pk_input(working_str="old_str=", limit_seconds=60, return_default='%%%OLD_STR%%%', get_input_validated=get_nx_validated)
            old_str = get_no_blank_working_str_validated(old_str)
            new_str = pk_input(working_str="new_str=", limit_seconds=60, return_default='%%%NEW_STR%%%', get_input_validated=get_nx_validated)
            new_str = get_no_blank_working_str_validated(new_str)
            pk_replace_f_nx_list_from_old_str_to_new_str(d_working=d_working, old_str=old_str, new_str=new_str)

    except:

        traceback_format_exc_list = traceback.format_exc().split("\n")
        print_red(PK_UNDERLINE)
        for line in traceback_format_exc_list:
            print_red(f'{STAMP_UNIT_TEST_EXCEPTION_DISCOVERED} {line}')
        print_red(PK_UNDERLINE)

    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        
