from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def get_fzf_command():
    from sources.objects.task_orchestrator_cli_files import F_FZF
    import shutil
    import os

    #  FAST PATH: 로그에서 확인된 작동하는 경로들을 우선순위로 빠르게 체크
    PRIORITIZED_PATHS = [
        F_FZF,
        # r"{D_USERPROFILE}\Downloads\task_orchestrator_cli\system_resources\fzf.EXE",  # 로그에서 확인된 작동 경로
        shutil.which("fzf.exe"),  # PATH에서 fzf.exe 찾기
        shutil.which("fzf"),  # PATH에서 fzf 찾기
    ]

    # 우선순위 경로들을 빠르게 체크 (subprocess 실행 없이 파일 존재 + 실행 권한만 확인)
    for path in PRIORITIZED_PATHS:
        if path and os.path.isfile(path):
            try:
                # 실행 권한 체크 (Windows에서도 작동)
                if os.access(path, os.R_OK):
                    return path
            except (OSError, PermissionError):
                continue

    #  SLOW PATH: 빠른 체크 실패 시에만 기존의 전체 검증 로직 수행
    return get_fzf_command_full_validation()


def get_fzf_command_full_validation():
    """기존의 전체 검증 로직 (subprocess로 --version 실행)"""
    import subprocess
    import shutil
    import os

    # Windows에서 우선적으로 확인할 경로들
    possible_paths = []

    # 1. 시스템 PATH에서 찾기
    fzf_path = shutil.which("fzf")
    if fzf_path:
        possible_paths.append(fzf_path)

    f_fzf = shutil.which("fzf.exe")
    if f_fzf:
        possible_paths.append(f_fzf)

    # 2. 일반적인 설치 경로들 확인
    common_paths = [
        r"C:\Program Files\fzf\fzf.exe",
        r"C:\Program Files (x86)\fzf\fzf.exe",
        r"C:\tools\fzf\fzf.exe",
        r"C:\ProgramData\chocolatey\bin\fzf.exe",
        os.path.expanduser(r"~\AppData\Local\fzf\fzf.exe"),
        os.path.expanduser(r"~\scoop\apps\fzf\current\fzf.exe"),
        os.path.expanduser(r"~\.fzf\bin\fzf.exe"),
    ]

    for path in common_paths:
        if os.path.isfile(path):
            possible_paths.append(path)

    # 3. 각 경로에서 실제 실행 가능한지 테스트
    for fzf_cmd in possible_paths:
        try:
            result = subprocess.run(
                [fzf_cmd, "--version"],
                capture_output=True,
                check=True,
                timeout=5,
                text=True
            )
            # 버전 정보가 있으면 유효한 fzf
            if result.stdout and ("fzf" in result.stdout.lower() or result.returncode == 0):
                return fzf_cmd
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError, FileNotFoundError):
            continue

    # 4. 마지막으로 기본 명령어들 시도
    for name in ["fzf", "fzf.exe"]:
        try:
            result = subprocess.run([name, "--version"], capture_output=True, check=True, timeout=5)
            return name
        except Exception:
            continue

    return None
