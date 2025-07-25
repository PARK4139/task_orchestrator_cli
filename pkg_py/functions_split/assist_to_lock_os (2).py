
"""sample: ["12:00-13:00", "15:00-15:10"] -> [(time(12,0), time(13,0)), (time(15,0), time(15,10))]"""
# 1 시간 마다 콘솔 클리어
# 샘플 설정 시간
# 시간 블럭에 해당하면 잠금
# 파싱
)
+ parse_time_ranges(break_time_ranges_text)
+ parse_time_ranges(exercise_time_ranges_text)
+ parse_time_ranges(lunch_time_ranges_text)
all_time_blocks = (
break_time_ranges_text = ["15:00-15:15"]
continue
def is_now_in_time_ranges(now_time, time_ranges):
def parse_time_ranges(text_list):
def pk_assist_to_lock_os():
ensure_console_cleared()
except:
exercise_time_ranges_text = ["18:30-18:50"]
for start, end in time_ranges:
for txt in text_list:
from datetime import datetime, time
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
h1, m1 = map(int, start_str.strip().split(":"))
h2, m2 = map(int, end_str.strip().split(":"))
if is_now_in_time_ranges(now_time, all_time_blocks):
if now.hour != last_cleared_hour:
if start <= now_time <= end:
last_cleared_hour = -1  # 아직 클리어된 적 없음을 의미
last_cleared_hour = now.hour
lunch_time_ranges_text = ["12:00-13:00"]
now = datetime.now()
now_time = now.time()
parse_time_ranges(sleep_time_ranges_text)
pk_lock_os()
pk_sleep(milliseconds=10000)
ranges = []
ranges.append((time(h1, m1), time(h2, m2)))
return False
return True
return ranges
sleep_time_ranges_text = ["00:12-05:30"]
start_str, end_str = txt.split("-")
try:
while True:
