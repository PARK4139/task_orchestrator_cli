

def get_values_from_historical_database_routine_v2(db_id, key_hint, values_default, editable):
    from pkg_py.pk_system_object.state_via_database import PkSqlite3DB
    from pkg_py.functions_split.get_value_completed import get_value_completed
    from pkg_py.functions_split.get_list_deduplicated import get_list_deduplicated

    def ensure_list(val):
        if val is None:
            return []
        if isinstance(val, str):
            return [val]
        return list(val)

    # Load from DB
    db = PkSqlite3DB()
    values_loaded = ensure_list(db.get_values(db_id=db_id))
    values_default = ensure_list(values_default)

    if editable == True:
        # TODO dbeaber 로 가능한지 가능하면 열기
        pass

    # Debug
    if LTA:
        print(f"values_default={values_default} {'%%%FOO%%%' if LTA else ''}")
        print(f"type(values_default)={type(values_default)} {'%%%FOO%%%' if LTA else ''}")

    # Merge and ask user
    values_optional = values_default + values_loaded
    user_value = get_value_completed(key_hint=key_hint, values=values_optional)
    user_value = user_value.strip()
    print(f'''type(user_value)={type(user_value)} {'%%%FOO%%%' if LTA else ''}''')
    print(f'''user_value={user_value} {'%%%FOO%%%' if LTA else ''}''')

    # Save and return
    values_to_save = get_list_deduplicated([user_value] + values_loaded)
    print(f'''values_to_save={values_to_save} {'%%%FOO%%%' if LTA else ''}''')
    print(f'''type(values_to_save)={type(values_to_save)} {'%%%FOO%%%' if LTA else ''}''')
    db.set_values(db_id=db_id, values=values_to_save)
    return user_value


