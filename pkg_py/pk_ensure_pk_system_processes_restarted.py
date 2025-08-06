from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
from pkg_py.functions_split.ensure_pk_system_processes_restarted import ensure_pk_system_processes_restarted
from pkg_py.system_object.directories  import D_PROJECT
# pk_#

if __name__ == "__main__":
    try:
        import traceback
        ensure_pk_system_processes_restarted()

    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
        
