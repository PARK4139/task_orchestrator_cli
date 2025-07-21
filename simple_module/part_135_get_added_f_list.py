def get_added_f_list(previous_state, current_state):
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    return DataStructureUtil.get_elements_that_list1_only_have(list1=current_state, list2=previous_state)
