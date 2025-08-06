def ensure_finally_routine_done(D_PROJECT, __file__):
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.etc import PK_UNDERLINE
    script_to_run = rf"{D_PROJECT}\.venv\Scripts\activate && python {__file__} && deactivate"
    ensure_printed(str_working=PK_UNDERLINE)
    ensure_printed(str_working=f"'[ TRY GUIDE ]' {script_to_run}")
    ensure_printed(str_working=PK_UNDERLINE)
