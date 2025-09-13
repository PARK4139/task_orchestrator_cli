from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
# @ensure_function_return_ttl_cached(ttl_seconds=60, maxsize=64)
def get_pk_program_language_v2():
    from sources.functions.get_file_id import get_file_id
    from sources.functions.get_values_from_historical_file_routine import get_values_from_historical_file_routine

    from sources.functions.get_values_from_historical_database_routine import get_values_from_historical_database_routine
    # import logging

    import inspect
    from sources.objects.pk_local_test_activate import LTA
    from sources.objects.pk_state_via_database import PkSqlite3DB

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    db = PkSqlite3DB()

    # reset_pk_program_language(db, func_n)

    key_hint1 = "is_initial_launch"
    is_initial_launch = db.get_values(db_id=db.get_db_id(key_hint1, func_n))
    if is_initial_launch is None:
        is_initial_launch = True
        print(f"is_initial_launch={is_initial_launch} %%%FOO%%%")
        if LTA:
            print(f"type={type(is_initial_launch)} %%%FOO%%%")
            print(f"is_initial_launch is True={is_initial_launch is True} %%%FOO%%%")

    key_name = "pk_program_language"
    if is_initial_launch is True:
        print("First launch detected")
        pk_program_language = None
        if LTA:
            pk_program_language = get_values_from_historical_file_routine(file_id=get_file_id(key_name, func_n), key_hint=f'{key_name}', options_default=["kr", "en"], editable=True)  # pk_option
        else:
            pk_program_language = get_values_from_historical_file_routine(file_id=get_file_id(key_name, func_n), key_hint=f'{key_name}', options_default=["kr", "en"], editable=True)
        db.set_values(db_id=db.get_db_id(key_name, func_n), values=pk_program_language)
        db.set_values(db_id=db.get_db_id(key_hint1, func_n), values=False)  # pk_option
    else:
        print("Subsequent launch")
        pk_program_language = db.get_values(db_id=db.get_db_id(key_name, func_n))

        if pk_program_language is None:
            print(f"{key_name} is missing. Re-configuring... %%%FOO%%%")
            pk_program_language = get_values_from_historical_database_routine(db_id=db.get_db_id(key_name, func_n), key_hint=f"{key_name}=", values_default=["kr", "en"]
                                                                              )
            db.set_values(db_id=db.get_db_id(key_name, func_n), values=pk_program_language)

    # reset_is_initial_launch(db,key_hint1,func_n)  # pk_option

    print(f"[{func_n}] {key_name} = {pk_program_language} %%%FOO%%%")

    # return pk_program_language # pk_option
    # return "kr"  # pk_option
    return "en"  # pk_option


def reset_is_initial_launch(db, key_hint1, func_n):
    db.set_values(db_id=db.get_db_id(key_hint1, func_n), values=True)  # pk_option
