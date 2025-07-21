from pkg_py.simple_module.part_757_pk_ensure_all_import_script_printed import pk_ensure_modules_printed

if __name__ == "__main__":
    import traceback
    from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
    from pkg_py.pk_system_layer_etc import PK_UNDERLINE
    from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE, STAMP_EXCEPTION_DISCOVERED
    from pkg_py.simple_module.part_014_pk_print import pk_print
    from pkg_py.simple_module.part_834_ensure_do_finally_routine import ensure_do_finally_routine
    try:
        pk_ensure_modules_printed()
    except:
        traceback_format_exc_list = traceback.format_exc().split("\n")
        pk_print(working_str=f'{PK_UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            pk_print(working_str=f'{STAMP_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        pk_print(working_str=f'{PK_UNDERLINE}', print_color='red')

    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
