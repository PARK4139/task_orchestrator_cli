from sources.objects.pk_state_via_database import PkSqlite3DB


def ensure_func_info_saved(func_n, func_data):
    pk_db = PkSqlite3DB()
    db_id = f"values_via_{func_n}"
    pk_db.reset_values(db_id=db_id)
    pk_db.set_values(db_id=db_id, values=func_data)
    return func_data
