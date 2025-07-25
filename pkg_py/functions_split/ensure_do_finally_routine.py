def ensure_do_finally_routine(D_PROJECT, __file__, STAMP_TRY_GUIDE):
    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.system_object.etc import PK_UNDERLINE
    script_to_run = rf"{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate"
    pk_print(str_working=PK_UNDERLINE)
    pk_print(str_working=f"{STAMP_TRY_GUIDE} {script_to_run}")
    pk_print(str_working=PK_UNDERLINE)
