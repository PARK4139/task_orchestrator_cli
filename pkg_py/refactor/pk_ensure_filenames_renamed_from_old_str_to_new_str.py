import traceback

from pkg_py.pk_system_object.directories import D_PK_SYSTEM_OBJECT
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT

from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.functions_split.pk_initialize_and_customize_logging_config import pk_initialize_and_customize_logging_config
from pkg_py.functions_split.pk_replace_f_nx_list_from_old_str_to_new_str import pk_replace_f_nx_list_from_old_str_to_new_str
from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE

if __name__ == "__main__":
    try:
        pk_initialize_and_customize_logging_config(__file__=__file__)
        d_working = D_PK_SYSTEM_OBJECT
        old_str = 'pk_system_layer_100_'
        new_str = ''
        pk_replace_f_nx_list_from_old_str_to_new_str(d_working=d_working, old_str=old_str, new_str=new_str)
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)

