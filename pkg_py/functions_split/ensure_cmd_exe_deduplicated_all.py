

def ensure_cmd_exe_deduplicated_all():
    from collections import defaultdict
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.ensure_process_deduplicated import ensure_process_deduplicated
    from pkg_py.functions_split.ensure_slept import ensure_slept
    from pkg_py.functions_split.get_values_sanitize_for_cp949 import get_values_sanitize_for_cp949
    from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
    from pkg_py.system_object.gui_util import get_windows_opened

    # ① 열린 창 목록 확보 및 CP949 대응 처리
    values = get_windows_opened()
    values = [get_values_sanitize_for_cp949(v) for v in values]

    # ② 제목별로 그룹핑 (윈도우 제목 기준)
    grouped = defaultdict(list)
    for title in values:
        grouped[title].append(title)

    ensure_iterable_printed_as_vertical(item_iterable=sorted(grouped), item_iterable_n="중복 확인 대상 창 제목들")

    # ③ 각 제목에 대해 1개만 남기고 닫기 시도
    for window_title in grouped:
        ensure_printed(f"[처리 중] 창 제목='{window_title}' 중복 제거", print_color="cyan")
        ensure_process_deduplicated(window_title_seg=window_title, exact=True)
        # ensure_slept(seconds=1000)
        # ensure_slept(seconds=500)
        ensure_slept(milliseconds=200)  # 너무 빠르게 반복되지 않도록 약간 대기


