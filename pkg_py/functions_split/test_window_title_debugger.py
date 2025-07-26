
def test_window_title_debugger():
ensure_iterable_printed_as_vertical(item_iterable=window_opened_list, item_iterable_n="window_opened_list")
ensure_iterable_printed_as_vertical(item_iterable=window_title_list, item_iterable_n="window_title_list")
window_opened_list = get_list_sorted(working_list=window_opened_list, mode_asc=1)
window_opened_list = get_windows_opened()
window_title_list = get_list_sorted(working_list=window_title_list, mode_asc=1)
window_title_list = get_window_title_list()
window_title_to_kill = "pk_test.py"  # was..blank problem..
