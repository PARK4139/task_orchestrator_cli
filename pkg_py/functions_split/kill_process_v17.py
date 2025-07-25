
c = wmi.WMI()
continue
def pk_kill_process_v17(window_title_seg: str):
except Exception as e:
except Exception:
for pid in matched_pids:
for proc in c.query("SELECT ProcessId, CommandLine, Caption FROM Win32_Process"):
if "cmd.exe" in (proc.Caption or "").lower() and get_nx(window_title).lower() in (proc.CommandLine or "").lower():
if LTA:
if not matched_pids:
if not window_title:
import subprocess
import wmi
matched_pids = set()
matched_pids.add(proc.ProcessId)
pk_print(f"PK KILL '{window_title}' not found", print_color="red")
pk_print(f"PK KILL PID={pid} window_title={window_title}", print_color="green")
pk_print(f"[ERROR] {e}", print_color="red")
pk_print(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")
return
stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.run(['taskkill', '/PID', str(pid), '/T', '/F'],
try:
window_title = get_window_title(window_title_seg=window_title_seg)
