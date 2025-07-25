
"""sample: ["12:00-13:00", "15:00-15:10"] -> [(time(12,0), time(13,0)), (time(15,0), time(15,10))]"""
"""알림 함수: 현재 시간을 출력하고, OS에 따라 알림 표시"""
# 1시간마다 콘솔 클리어
# 파싱
)
+ parse_time_ranges(break_time_ranges_text)
+ parse_time_ranges(exercise_time_ranges_text)
+ parse_time_ranges(lunch_time_ranges_text)
alert(now_time)
alerted_blocks = set()  # 이미 알림을 한 시간 구간 저장
alerted_blocks.add(idx)
alerted_blocks.clear()  # 새로운 시간 진입 시, 알림 상태 초기화
all_time_blocks = (
break  # 현재 속한 구간 하나만 처리
break_time_ranges_text = ["15:00-15:15"]
continue
def alert(now_time):
def is_now_in_time_range(now_time, time_range):
def parse_time_ranges(text_list):
def pk_jarvis():
ensure_console_cleared()
except:
exercise_time_ranges_text = ["18:30-18:50"]
for idx, block in enumerate(all_time_blocks):
for txt in text_list:
from datetime import datetime, time
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.functions_split.print import pk_print
from pkg_py.functions_split.sleep import pk_sleep
from pkg_py.functions_split.speak import pk_speak
from pkg_py.workspace.pk_workspace import pk_speak_v3
h1, m1 = map(int, start_str.strip().split(":"))
h2, m2 = map(int, end_str.strip().split(":"))
if idx not in alerted_blocks:
if is_now_in_time_range(now_time, block):
if now.hour != last_cleared_hour:
last_cleared_hour = -1  # 아직 클리어된 적 없음을 의미
last_cleared_hour = now.hour
lunch_time_ranges_text = ["12:00-13:00"]
now = datetime.now()
now_time = now.time()
parse_time_ranges(sleep_time_ranges_text)
pk_print(f"alerted_blocks=({alerted_blocks})", print_color='yellow')
pk_print(f"현재 시간은 {now_time.hour}시 {now_time.minute}분입니다.", print_color='yellow')
pk_sleep(milliseconds=10000)
pk_speak(f"현재 시간은 {now_time.hour}시 {now_time.minute}분입니다.")
pk_speak_v3("샘플 설정 시간을 입력해주세요")
ranges = []
ranges.append((time(h1, m1), time(h2, m2)))
return ranges
return start <= now_time <= end
sleep_time_ranges_text = ["00:12-05:30"]
start, end = time_range
start_str, end_str = txt.split("-")
try:
while True:
