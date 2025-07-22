def get_str_removed_last_digit(string, debug_mode=True):
    import inspect
    import re
    func_n = inspect.currentframe().f_code.co_name
    return re.sub(r'\d+\s*$', '', string)
