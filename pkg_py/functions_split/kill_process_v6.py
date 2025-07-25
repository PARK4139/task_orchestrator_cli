
)
['taskkill', '/PID', str(pid), '/T', '/F'],
cmdline = ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else ''
continue
def pk_kill_process_v6(cmd_exe_title: str):
except (psutil.AccessDenied, psutil.ZombieProcess, psutil.NoSuchProcess):
except Exception as e:
except subprocess.TimeoutExpired:
for pid in matched_pids:
for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
if 'cmd.exe' in (proc.info['name'] or '').lower() and cmd_exe_title.lower() in cmdline.lower():
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
pk_print(f"[TASKKILL ERROR] PID={pid}, {e}", print_color="red")
pk_print(f"[TIMEOUT] taskkill for PID={pid} timed out", print_color="yellow")
pk_print(f"[WARN] psutil error: {e}", print_color="yellow")
pk_print(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")
return
stderr=subprocess.DEVNULL,
stdout=subprocess.DEVNULL,
subprocess.run(
timeout=1
try:
window_title = get_window_title(window_title_seg=cmd_exe_title)
