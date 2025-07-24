def get_list_removed_by_removing_runtine(working_list):
    from pkg_py.functions_split.get_list_deduplicated import get_list_deduplicated
    from pkg_py.functions_split.get_list_removed_element_empty import get_list_removed_empty
    from pkg_py.functions_split.get_list_replaced_element_from_str_to_str import get_list_replaced_element_from_str_to_str
    from pkg_py.functions_split.get_list_striped_element import get_list_striped_element
    from pkg_py.functions_split.get_list_without_none import get_list_without_none

    import inspect
    func_n = inspect.currentframe().f_code.co_name
    if working_list is None:
        return None
    working_list = get_list_deduplicated(working_list)
    working_list = get_list_without_none(working_list)
    working_list = get_list_removed_empty(working_list)
    working_list = get_list_replaced_element_from_str_to_str(working_list, "\n", "")
    working_list = get_list_striped_element(working_list)
    return working_list
