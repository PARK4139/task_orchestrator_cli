from pkg_py.system_object.stamps import STAMP_LIST, STAMP_TUPLE, STAMP_DICT, STAMP_SET


def print_iterable_as_vertical(item_iterable, item_iterable_n=None, mode_verbose=1):
    import inspect
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.functions_split.ensure_printed import ensure_printed
    if mode_verbose == 1:
        # 변수 이름 자동 추출 시도
        if item_iterable_n is None:
            frame = inspect.currentframe()
            outer_frames = inspect.getouterframes(frame)
            try:
                call_line = outer_frames[1].code_context[0]
                var_n = call_line.split('(')[1].split(',')[0].strip()
                item_iterable_n = var_n.replace(')', '')
            except Exception:
                item_iterable_n = 'Undefined'  # 실패 시 기본값
            finally:
                del frame

        if isinstance(item_iterable, list):
            STAMP_DATA_TYPE = STAMP_LIST
            open_bracket, kill_bracket = '[', ']'
        elif isinstance(item_iterable, set):
            STAMP_DATA_TYPE = STAMP_SET
            open_bracket, kill_bracket = '{', '}'
        elif isinstance(item_iterable, dict):
            STAMP_DATA_TYPE = STAMP_DICT
            open_bracket, kill_bracket = '{', '}'
        elif isinstance(item_iterable, tuple):
            STAMP_DATA_TYPE = STAMP_TUPLE
            open_bracket, kill_bracket = '(', ')'
        else:
            STAMP_DATA_TYPE = STAMP_LIST  # 기본값 설정
            open_bracket, kill_bracket = '[', ']'

        # todo : dict 일때 key 는 나오는데 value 안나옴. value 나오도록 업그레이드
        # ensure_printed(f'''{STAMP_DATA_TYPE} {item_iterable_n}={open_bracket}''')
        ensure_printed(f'''{STAMP_DATA_TYPE} {open_bracket}''')
        for idx, item in enumerate(item_iterable):
            item_str = str(item).replace("\n", "")
            ensure_printed(
                f'''{STAMP_DATA_TYPE}     {item_iterable_n[:5]}...[{idx}]={item_str}  {'%%%FOO%%%' if LTA else ''}''')
        ensure_printed(f'''{STAMP_DATA_TYPE} {kill_bracket}''')

    elif mode_verbose == 0:
        for idx, item in enumerate(item_iterable):
            print(f'''{idx} {item}  {'%%%FOO%%%' if LTA else ''}''')
