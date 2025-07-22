import pyaudio
from tkinter import UNDERLINE
from collections import Counter
from pkg_py.functions_split.is_f import is_f
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_windows import is_os_windows

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def ping_v2(ip, timeout_ms=1000):
    # lazy import
    import subprocess

    if not ip:
        pk_print(f'ping {ip}', print_color='red')
        return 0

    # OS별 ping 명령어 및 성공 시그널 정의
    if is_os_windows():
        cmd = f"ping -n 1 -w {timeout_ms} {ip}"
        signatures = ["(0% loss)", "(0% 손실)"]
    else:
        sec = max(1, timeout_ms // 1000)
        cmd = f"ping -c 1 -W {sec} {ip}"
        signatures = [f"{PK_BLANK}0% packet loss"]

    try:
        proc = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,  # universal_newlines=True 와 동일
            encoding='utf-8',  # utf-8로 디코딩 시도
            errors='ignore'  # 디코딩 오류 무시
        )
        stdout, _ = proc.communicate(timeout=(timeout_ms / 1000) + 0.5)
    except subprocess.TimeoutExpired:
        proc.kill()
        stdout = ""
    except Exception:
        stdout = ""

    # None 또는 빈값 방어
    if not stdout:
        stdout = ""

    # 결과 판정
    for line in stdout.splitlines():
        if any(sig in line for sig in signatures):
            if LTA:
                pk_print(f'ping {ip}', print_color='green')
            return 1

    pk_print(f'ping {ip}', print_color='red')
    return 0
