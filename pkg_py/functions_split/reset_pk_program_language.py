

def reset_pk_program_language(db, func_n):
    key_name = "is_initial_launch"
    db.reset_values(db_id=db.get_id(key_name, func_n))
    key_name = "pk_program_language"
    db.reset_values(db_id=db.get_id(key_name, func_n))


