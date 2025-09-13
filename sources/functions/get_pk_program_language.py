def get_pk_program_language():
    from sources.objects.pk_local_test_activate import LTA
    try:
        if LTA:
            # return "english"  # pk_option
            return "korean"  # pk_option
        else:
            from sources.functions.get_file_id import get_file_id
            from sources.functions.get_values_from_historical_file_routine import get_values_from_historical_file_routine

            from sources.functions.get_values_from_historical_database_routine import get_values_from_historical_database_routine

            import inspect
            from sources.objects.pk_local_test_activate import LTA
            from sources.objects.pk_state_via_database import PkSqlite3DB
            from functions.get_caller_n import get_caller_n
            func_n = get_caller_n()
            db = PkSqlite3DB()

            key_hint1 = "is_initial_launch"
            is_initial_launch = db.get_values(db_id=db.get_db_id(key_hint1, func_n))
            if is_initial_launch is None:
                is_initial_launch = True
                print(f"is_initial_launch={is_initial_launch} %%%FOO%%%")
                if LTA:
                    print(f"type={type(is_initial_launch)} %%%FOO%%%")
                    print(f"is_initial_launch is True={is_initial_launch is True} %%%FOO%%%")

            pk_program_language = None
            key_name = "pk_program_language"
            if is_initial_launch is True:
                print("First launch detected")
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

            print(f"[{func_n}] {key_name} = {pk_program_language} %%%FOO%%%")

            # reset_is_initial_launch(db,key_hint1,func_n)  # pk_option

            return pk_program_language  # pk_option
    except:
        return "english"
