from pkg_py.functions_split.ensure_printed import ensure_printed


def get_db_conn():
    #
    from mysql.connector import connect, Error

    import time
    host = get_pk_config("db_host", "127.0.0.1")
    user = get_pk_config("db_user", "root")
    pwd = get_pk_config("db_password", "example")
    db = get_pk_config("db_name", "nyaa_db")
    port = int(get_pk_config("db_port", "3306"))
    for attempt in range(1, 6):
        try:
            ensure_printed(f"Connecting to DB (attempt {attempt})...")
            conn = connect(host=host, user=user, password=pwd, database=db, port=port, charset="utf8mb4")
            ensure_printed("DB connected")
            return conn
        except Error as e:
            ensure_printed(f"Connection failed: {e}", print_color="yellow")
            time.sleep(5)
    raise RuntimeError("Could not connect to MariaDB after several attempts")
