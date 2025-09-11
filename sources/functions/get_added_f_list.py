def get_added_f_list(previous_state, current_state):
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    return DataStructureUtil.get_elements_that_list1_only_have(list1=current_state, list2=previous_state)
