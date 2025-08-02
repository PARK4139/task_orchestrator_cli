from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
from pkg_py.functions_split.get_pk_token import get_pk_token
from pkg_py.functions_split.ensure_copied import ensure_copied
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.directories import D_PKG_TOML
from pkg_py.system_object.etc import PK_UNDERLINE

if __name__ == "__main__":
    try:
        import traceback
        github_pat = get_pk_token(f_token=f'{D_PKG_TOML}/pk_token_github_pat.toml', initial_str='')
        ensure_copied(github_pat)
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)

    finally:
        # ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        ensure_printed(str_working=f'{PK_UNDERLINE}')
        # ensure_printed(str_working=f'{STAMP_TRY_GUIDE} {script_to_run_python_program_in_venv}')
        ensure_printed(str_working=f'{PK_UNDERLINE}')