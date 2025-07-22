from pkg_py.functions_split.pk_print import pk_print


def ensure_do_finally_routine(D_PROJECT, __file__, STAMP_TRY_GUIDE):
    from pkg_py.pk_system_object.etc import PK_UNDERLINE
    script_to_run = rf"{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate"
    pk_print(working_str=PK_UNDERLINE)
    pk_print(working_str=f"{STAMP_TRY_GUIDE} {script_to_run}")
    pk_print(working_str=PK_UNDERLINE)
