def get_count_none_of_list(list):
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    # count=sum(element is None for element in list)
    Nones = list
    None_count = Nones.count(None)
    return None_count
