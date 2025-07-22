from pkg_py.functions_split.get_values_from_historical_database_routine import get_values_from_historical_database_routine
from pkg_py.functions_split.pk_print import pk_print


def get_pk_program_language_v2():
    import inspect
    from pkg_py.pk_system_object.Local_test_activate import LTA
    from pkg_py.pk_system_object.state_via_database import PkSqlite3DB

    func_n = inspect.currentframe().f_code.co_name
    db = PkSqlite3DB()

    # reset_pk_program_language(db, func_n)

    key_hint2 = "is_initial_launch"
    key_hint1 = "pk_program_language"

    is_initial_launch = db.get_values(db_id=db.get_id(key_hint2, func_n))
    if is_initial_launch is None:
        is_initial_launch = True

    if LTA:
        pk_print(f"is_initial_launch={is_initial_launch} %%%FOO%%%")
        pk_print(f"type={type(is_initial_launch)} %%%FOO%%%")
        pk_print(f"is_initial_launch is True={is_initial_launch is True} %%%FOO%%%")

    if is_initial_launch is True:
        pk_print("🎯 First launch detected")

        pk_program_language = get_values_from_historical_database_routine(
            db_id=db.get_id(key_hint1, func_n),
            key_hint=f"{key_hint1}=",
            values_default=["kr", "en"]
        )
        db.set_values(db_id=db.get_id(key_hint1, func_n), values=pk_program_language)

        db.set_values(db_id=db.get_id(key_hint2, func_n), values=False)
    else:
        pk_print("Subsequent launch")
        pk_program_language = db.get_values(db_id=db.get_id(key_hint1, func_n))

        if pk_program_language is None:
            pk_print(f"{key_hint1} is missing. Re-configuring... %%%FOO%%%")
            pk_program_language = get_values_from_historical_database_routine(
                db_id=db.get_id(key_hint1, func_n),
                key_hint=f"{key_hint1}=",
                values_default=["kr", "en"]
            )
            db.set_values(db_id=db.get_id(key_hint1, func_n), values=pk_program_language)
    pk_print(f"[{func_n}] {key_hint1} = {pk_program_language} %%%FOO%%%")
    return pk_program_language
