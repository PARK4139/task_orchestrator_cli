
#     return
# if not is_window_opened_exactly(window_title=window_title):
cmd = f'tasklist /FI "WINDOWTITLE eq {window_title}" /FO CSV'
def pk_kill_process_v2(cmd_exe_title: str):
except Exception as e:
except subprocess.CalledProcessError:
for pid in matched_pids:
for row in reader:
from io import StringIO
if LTA:
if not matched_pids:
if not window_title:
if pid:
import csv
import subprocess
matched_pids = set()
matched_pids.add(pid)
output = subprocess.check_output(cmd, shell=True, encoding='cp949', errors='ignore')
pid = row.get("PID")
pk_print(f"[ERROR] {e}", print_color="red")
pk_print(f"[NO MATCH] '{cmd_exe_title}' 프로세스를 찾지 못했습니다.", print_color="red")
pk_print(f"[NO MATCH] '{cmd_exe_title}'와 일치하는 프로세스를 찾지 못했습니다.", print_color="red")
pk_print(f"[PK KILL] PID={pid} cmd_exe_title={cmd_exe_title}", print_color="green")
pk_print(f'''cmd={cmd} {'%%%FOO%%%' if LTA else ''}''')
pk_print(f'''window_title={window_title} {'%%%FOO%%%' if LTA else ''}''')
reader = csv.DictReader(StringIO(output))
return
stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.run(['taskkill', '/PID', pid, '/T', '/F'],
try:
window_title = get_window_title(window_title_seg=cmd_exe_title)
