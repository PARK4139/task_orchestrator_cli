def get_list_without_none(working_list):
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    if working_list is not None:
        return [x for x in working_list if x is not None]
    return None
