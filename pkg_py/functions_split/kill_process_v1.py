
"""
# cmd_exe_title이 프로세스 cmdline에 포함되어 있는지 확인
# ensure_printed(f"[PROCESS TERMINATED] PID={pid}, Name={process.info['name']}")
def kill_process_v1(cmd_exe_title):
except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
except psutil.TimeoutExpired:
for process in psutil.process_iter(['pid', 'name', 'cmdline']):
if process.info['cmdline'] and any(cmd_exe_title in cmd for cmd in process.info['cmdline']):
import psutil
pass
pid = process.info['pid']
ensure_printed(f"[PROCESS TERMINATED] PID={pid}, Name={process.info['name']}", print_color="green")
ensure_printed(f"[PROCESS TERMINATED] 시간 초과 ", print_color='red')
ensure_printed(f'''cmd_exe_title={cmd_exe_title}  {'%%%FOO%%%' if LTA else ''}''', print_color="blue")
proc = psutil.Process(pid)
proc.terminate()  # 프로세스 종료 요청
proc.wait(timeout=5)  # 종료 완료를 대기, 최대 5초 대기
try:
주어진 cmd_exe_title과 일치하는 프로세스를 찾아 동기적으로 종료하는 함수
