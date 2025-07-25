
"""
# 첫 번째 매칭된 타이틀을 기준으로 process 검색
:param timeout: 종료 대기 시간 (초)
:param window_title_seg: 윈도우 제목 일부 문자열
:return: True (모두 종료됨), False (하나라도 종료 실패)
]
all_killed = False
all_killed = True
and target in " ".join(proc.info.get('cmdline', [])).lower()
continue
def get_pids_by_title_seg(windows_title_seg: str) -> list[int]:
def is_process_killed(window_title_seg: str, timeout: float = 1.0) -> bool:
else:
except Exception as e:
except psutil.NoSuchProcess:
except psutil.TimeoutExpired:
for pid in pids:
for proc in psutil.process_iter(['pid', 'name', 'cmdline'])
if not matches:
if not pids:
if proc.info['name'].lower() == 'cmd.exe'
if proc.is_running():
import os
import psutil
matches = get_window_title(windows_title_seg)
pids = get_pids_by_title_seg(window_title_seg)
pk_print(f"[ERROR] 전체 종료 확인 실패: {e}", print_color="red")
pk_print(f"[SKIP] No matching process found for '{window_title_seg}'", print_color="yellow")
pk_print(f"⚠️ PID={pid} 여전히 실행 중", print_color="yellow")
pk_print(f"✅ PID={pid} 종료 확인됨", print_color="green")
pk_print(f"❌ 예외 발생 PID={pid}, error={e}", print_color="red")
pk_print(f"🛑 PID={pid} 종료 실패 (TIMEOUT)", print_color="red")
proc = psutil.Process(pid)
proc.info['pid']
proc.kill()
proc.terminate()
proc.wait(timeout=timeout)
return False
return True  # 이미 종료된 것으로 간주
return [
return []
return all_killed
target = os.path.splitext(os.path.basename(matches[0]))[0].lower()
try:
주어진 window_title_seg에 해당하는 CMD 프로세스가 종료되었는지 확인하고 종료 시도.
