def get_window_title_temp_identified():
    from functions.get_hash import get_hash
    from functions.get_nx import get_nx
    hash = get_hash(get_nx(__file__))
    return f"temp window {hash}"
