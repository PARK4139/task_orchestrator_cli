from functions.get_caller_n import get_caller_n
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_pk_program_language_reset():
    import logging
    import traceback

    from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose
    from functions.ensure_value_completed_advanced import ensure_value_completed_advanced
    from functions.reset_pk_program_language import reset_pk_program_language
    from sources.objects.pk_state_via_database import PkSqlite3DB

    try:
        from functions.get_caller_n import get_caller_n
        func_n = get_caller_n()
        db = PkSqlite3DB()

        reset_pk_program_language(db, func_n)

        key_name = "pk_program_language"
        selected = ensure_value_completed_advanced(key_name=key_name, func_n=func_n, options=["korean", "english"])
        pk_program_language = selected

        db.set_values(db_id=db.get_db_id(key_name, func_n), values=pk_program_language)
        pk_program_language = db.get_values(db_id=db.get_db_id(key_name, func_n))
        logging.debug(f'pk_program_language={pk_program_language}')
    except:
        ensure_debug_loged_verbose(traceback=traceback)
