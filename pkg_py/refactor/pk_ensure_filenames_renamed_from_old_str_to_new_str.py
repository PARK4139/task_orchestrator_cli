import traceback

from pkg_py.system_object.directories import D_SYSTEM_OBJECT
from pkg_py.system_object.directories  import D_PROJECT

from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
from pkg_py.functions_split.pk_ensure_finally_routine_done import pk_ensure_finally_routine_done
from pkg_py.functions_split.initialize_and_customize_logging_config import initialize_and_customize_logging_config
from pkg_py.functions_split.replace_f_nx_list_from_old_str_to_new_str import replace_f_nx_list_from_old_str_to_new_str
# pk_#

if __name__ == "__main__":
    try:
        initialize_and_customize_logging_config(__file__=__file__)
        d_working = D_SYSTEM_OBJECT
        old_str = 'pk_system_layer_100_'
        new_str = ''
        pk_replace_f_nx_list_from_old_str_to_new_str(d_working=d_working, old_str=old_str, new_str=new_str)
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        pk_ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)

