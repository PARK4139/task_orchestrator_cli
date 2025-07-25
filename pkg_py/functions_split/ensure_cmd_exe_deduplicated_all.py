
# pk_sleep(seconds=1000)
# pk_sleep(seconds=500)
# ① 열린 창 목록 확보 및 CP949 대응 처리
# ② 제목별로 그룹핑 (윈도우 제목 기준)
# ③ 각 제목에 대해 1개만 남기고 닫기 시도
def ensure_cmd_exe_deduplicated_all():
for title in values:
for window_title in grouped:
from collections import defaultdict
grouped = defaultdict(list)
grouped[title].append(title)
pk_ensure_process_deduplicated(window_title_seg=window_title, exact=True)
pk_print(f"[처리 중] 창 제목='{window_title}' 중복 제거", print_color="cyan")
pk_sleep(milliseconds=200)  # 너무 빠르게 반복되지 않도록 약간 대기
print_iterable_as_vertical(item_iterable=sorted(grouped), item_iterable_n="중복 확인 대상 창 제목들")
values = [get_values_sanitize_for_cp949(v) for v in values]
values = get_windows_opened()
