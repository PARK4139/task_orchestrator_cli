

def get_list_replaced_element_from_str_to_upper_case(working_list):
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    if not isinstance(working_list, list):
        raise ValueError("Input must be a list.")
    return [item.upper() if isinstance(item, str) else item for item in working_list]
