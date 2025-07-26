def ping_v3(ip, timeout_ms=1000):
    import subprocess
    from pkg_py.functions_split.is_os_windows import is_os_windows
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.etc import PK_BLANK

    if not ip:
        ensure_printed(f'ping {ip}', print_color='red')
        return 0

    # OS별 명령어 및 성공 시그널 정의
    if is_os_windows():
        cmd = f"ping -n 1 -w {timeout_ms} {ip}"
        signatures = ["(0% loss)", "(0% 손실)"]
        encoding = 'mbcs'  # ANSI 코드 페이지(한국어 Windows: CP949)
    else:
        sec = max(1, timeout_ms // 1000)
        cmd = f"ping -c 1 -W {sec} {ip}"
        signatures = [f"{PK_BLANK}0% packet loss"]
        encoding = 'utf-8'

    try:
        proc = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            encoding=encoding,
            errors='ignore'
        )
        stdout, _ = proc.communicate(timeout=(timeout_ms / 1000) + 0.5)
    except subprocess.TimeoutExpired:
        proc.kill()
        stdout = ""
    except Exception:
        stdout = ""

    # stdout이 None이거나 빈값 방어
    if not stdout:
        stdout = ""

    # **리턴코드 우선 검사** (0이면 성공)
    if proc.returncode == 0:
        if LTA:
            ensure_printed(f'ping {ip}', print_color='green')
        return 1

    # 리턴코드로도 판단 안 될 때만 시그니처 검사
    for line in stdout.splitlines():
        if any(sig in line for sig in signatures):
            if LTA:
                ensure_printed(f'ping {ip}', print_color='green')
            return 1

    ensure_printed(f'ping {ip}', print_color='red')
    return 0
