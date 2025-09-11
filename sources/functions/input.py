from sources.functions.ensure_value_completed import ensure_value_completed
def input(str_working, limit_seconds, return_default, get_input_validated=None):
    return ensure_value_completed(key_hint=str_working, options=[return_default] if return_default else [])
