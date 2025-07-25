
# OS별 실행
# WSL 환경
# title 명령어로 창 제목 지정 (pk_ 접두사 제거된 제목)
# 기타 리눅스/유닉스
cmd = f'python3 {file_to_excute}'
cmd = f'start "" cmd.exe /k "title {file_title}&& python {file_to_excute}"'
cmd_to_os(cmd=cmd)
cmd_to_os(cmd=cmd, mode='a', mode_with_window=1)
def pk_run_py_system_process_by_pnx(file_to_excute, file_title):
elif is_os_wsl_linux():
else:
file_title = file_title.strip()
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
if is_os_windows():
import subprocess
print(f"[실행 중 - Linux/Unix] {cmd}")
print(f"[실행 중 - WSL] {cmd}")
print(f"[실행 중 - Windows] {cmd}")
subprocess.run(cmd, shell=True)
