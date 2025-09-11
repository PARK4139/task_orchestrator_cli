def get_current_interval():
    pass


def ensure_interval_based_on_state_updated(pk_db,func_n,INTERVAL_ORIGIN, INTERVAL_DELTA, INTERVAL_MAX,state_current: dict):
    from sources.functions.get_db_id import get_db_id
    import time
    state_prev = None
    values = pk_db.get_values(db_id=get_db_id(key_name="speed_control_state_prev", func_n=func_n))
    if values:
        try:
            state_prev = eval(values[0])
        except:
            pass

    now = time.time()
    if state_prev != state_current:
        pk_db.set_values(values=[str(state_current)], db_id=get_db_id(key_name="speed_control_state_prev", func_n=func_n))
        pk_db.set_values(values=[str(now)], db_id=get_db_id(key_name="speed_control_timestamp", func_n=func_n))
        pk_db.set_values(values=[str(INTERVAL_ORIGIN)], db_id=get_db_id(key_name="speed_control_interval_ms", func_n=func_n))
    else:
        values_ts = pk_db.get_values(db_id=get_db_id(key_name="speed_control_timestamp", func_n=func_n))
        if values_ts:
            try:
                elapsed = now - float(values_ts[0])
                if elapsed >= 2:
                    interval = get_current_interval()
                    interval = min(interval + INTERVAL_DELTA, INTERVAL_MAX)
                    pk_db.set_values(values=[str(interval)], db_id=get_db_id(key_name="speed_control_interval_ms", func_n=func_n))
            except:
                pass


