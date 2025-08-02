if __name__ == '__main__':
    import traceback

    from pkg_py.functions_split.ensure_tree_analized_option import ensure_tree_analized_option
    from pkg_py.functions_split.chcp_65001 import chcp_65001
    from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
    from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
    from pkg_py.functions_split.ensure_slept import ensure_slept
    from pkg_py.functions_split.get_os_n import get_os_n
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE

    try:

        if get_os_n() == 'windows':
            chcp_65001()

        while 1:
            ensure_tree_analized_option(d_src=rf"D:\pk_classifying")
            ensure_slept(hours=3)
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
