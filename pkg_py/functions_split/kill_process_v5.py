
continue
def pk_kill_process_v5(cmd_exe_title: str):
except Exception as e:
except Exception:
except subprocess.TimeoutExpired:
for pid in matched_pids:
for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
if 'cmd.exe' in (proc.info['name'] or '').lower() and window_title.lower() in ' '.join(proc.info['cmdline'] or []).lower():
if LTA:
if not matched_pids:
if not window_title:
import psutil
import subprocess
matched_pids = set()
matched_pids.add(proc.info['pid'])
pk_print(f"[ERROR] {e}", print_color="red")
pk_print(f"[NO MATCH] '{window_title}'와 일치하는 프로세스를 찾지 못했습니다.", print_color="red")
pk_print(f"[PK KILL] PID={pid} window_title={window_title}", print_color="green")
pk_print(f"[TIMEOUT] PID={pid} taskkill took too long", print_color="yellow")
pk_print(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")
return
stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=1)
subprocess.run(['taskkill', '/PID', str(pid), '/T', '/F'],
try:
window_title = get_window_title(window_title_seg=cmd_exe_title)
