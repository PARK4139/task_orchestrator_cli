def get_list_deduplicated(working_list):
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    items_removed_duplication: [str] = []
    for item in working_list:
        if item not in items_removed_duplication:
            # if item is not None:
            items_removed_duplication.append(item)
    working_list = items_removed_duplication
    return working_list
