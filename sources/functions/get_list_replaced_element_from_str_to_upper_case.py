

def get_list_replaced_element_from_str_to_upper_case(working_list):
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    if not isinstance(working_list, list):
        raise ValueError("Input must be a list.")
    return [item.upper() if isinstance(item, str) else item for item in working_list]
