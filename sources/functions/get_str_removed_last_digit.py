def get_str_removed_last_digit(string, debug_mode=True):
    import inspect
    import re
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    return re.sub(r'\d+\s*$', '', string)
