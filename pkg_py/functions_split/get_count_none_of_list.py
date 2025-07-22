def get_count_none_of_list(list):
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    # count=sum(element is None for element in list)
    Nones = list
    None_count = Nones.count(None)
    return None_count
