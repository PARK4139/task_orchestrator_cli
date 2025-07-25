
cmd = "wsl --shutdown"
cmd_to_os(cmd=cmd, mode="a")
def kill_wsl_exe():
for pid in pids:
func_n = inspect.currentframe().f_code.co_name
if pid is not None:
if pids is not None:
import inspect
kill_process_via_taskkill(pid=pid)
pids = get_pids("wsl.exe")
pk_press("enter")
process_name = "wsl.exe"
write_like_person("exit")
