from pkg_py.pk_system_object.state_via_database import PkSqlite3DB


def ensure_func_info_loaded(func_n):
    pk_db = PkSqlite3DB()
    db_id = f"values_via_{func_n}"
    func_data = pk_db.get_values(db_id=db_id)
    return func_data
