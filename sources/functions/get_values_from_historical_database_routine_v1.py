

def get_values_from_historical_database_routine_v1(db_id, key_hint, values_default):
    from sources.objects.pk_state_via_database import PkSqlite3DB
    from sources.functions.ensure_value_completed import ensure_value_completed
    from sources.functions.get_list_deduplicated import get_list_deduplicated
    db = PkSqlite3DB()
    values_loaded = db.get_values(db_id=db_id)
    if LTA:
        print(f'''values_default={values_default} {'%%%FOO%%%' if LTA else ''}''')
        print(f'''type(values_default)={type(values_default)} {'%%%FOO%%%' if LTA else ''}''')
    if isinstance(values_loaded, str):
        values_loaded = [values_loaded]
    if isinstance(values_default, str):
        values_default = [values_default]
    if values_default is None:
        values_default = []
    if values_loaded is None:
        values_loaded = []
    values_optional = values_default + values_loaded
    user_value = ensure_value_completed(key_hint=key_hint, options=values_optional)
    user_value = user_value.strip()
    values_to_save = get_list_deduplicated([user_value] + values_loaded)
    db.set_values(db_id=db_id, values=values_to_save)
    return user_value


