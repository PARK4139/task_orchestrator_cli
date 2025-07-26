
# ensure_printed(f"[SKIP] 창 제목 세그먼트 '{cmd_exe_title}'로 찾은 창이 없습니다.", print_color="blue")
c = wmi.WMI()
caption_match = "cmd.exe" in (proc.Caption or "").lower()
continue
def kill_process_v3(cmd_exe_title: str):
except Exception as e:
except Exception:
for pid in matched_pids:
for proc in c.Win32_Process():
if LTA:
if not matched_pids:
if not window_title:
if title_match and caption_match:
import subprocess
import wmi
matched_pids = set()
matched_pids.add(proc.ProcessId)
ensure_printed(f"[ERROR] {e}", print_color="red")
ensure_printed(f"[NO MATCH] '{window_title}'와 일치하는 프로세스를 찾지 못했습니다.", print_color="red")
ensure_printed(f"[PK KILL] PID={pid} window_title={window_title}", print_color="green")
ensure_printed(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")
return
stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.run(['taskkill', '/PID', str(pid), '/T', '/F'],
title_match = window_title.lower() in (proc.CommandLine or "").lower()
try:
window_title = get_window_title(window_title_seg=cmd_exe_title)
