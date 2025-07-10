def test_function_window_to_front():
    from pkg_py.pk_core import get_window_title, LTA
    from pkg_py.pk_core import is_window_title_front, ensure_window_to_front
    import time
    test_result_list = []
    test_loop_cnt_limit = 10
    window_title_seg = 'Madou'
    while len(test_result_list) < test_loop_cnt_limit:
        ensure_window_to_front(window_title_seg=window_title_seg)
        time.sleep(0.1)  # 너무 빠르게 루프 돌지 않게 잠시 대기
        test_result_list.append(is_window_title_front(window_title=get_window_title(window_title_seg)))
    from pkg_py.pk_colorful_cli_util import pk_print
    pk_print(f'''test_result_list={test_result_list} {'%%%FOO%%%' if LTA else ''}''')
    assert all(test_result_list), f"failed in [{len(test_result_list)}/{test_loop_cnt_limit}]"
