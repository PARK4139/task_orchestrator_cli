import logging


def ensure_text_saved_to_clipboard(str_working):
    """
    클립보드에 텍스트를 복사하는 함수
    - WSL 환경에서는 PowerShell Set-Clipboard 사용
    - Windows 환경에서는 clipboard 라이브러리 사용
    - Linux 환경에서는 xclip 또는 xsel 사용
    """
    from sources.functions.is_os_wsl_linux import is_os_wsl_linux
    from sources.functions.is_os_windows import is_os_windows
    from sources.functions.is_os_linux import is_os_linux
    
    if is_os_wsl_linux():
        # WSL 환경에서는 PowerShell Set-Clipboard 사용
        try:
            import subprocess
            # PowerShell 명령어로 클립보드에 복사
            cmd = f'Set-Clipboard -Value "{str_working}"'
            subprocess.run(['powershell.exe', '-Command', cmd], check=True)
            return str_working
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            logging.debug(f"WSL 클립보드 복사 실패: {str(e)}")
            return str_working
    elif is_os_windows():
        # Windows에서는 clipboard 라이브러리 사용
        try:
            import clipboard
            clipboard.copy(str_working)
            return str_working
        except ImportError:
            logging.debug(f"Windows 클립보드 복사 실패. clipboard 모듈이 없습니다.")
            return str_working
    elif is_os_linux():
        # Linux에서는 xclip 또는 xsel 사용
        try:
            import subprocess
            subprocess.run(['xclip', '-selection', 'clipboard'], input=str_working.encode(), check=True)
            return str_working
        except (subprocess.CalledProcessError, FileNotFoundError):
            try:
                subprocess.run(['xsel', '--clipboard'], input=str_working.encode(), check=True)
                return str_working
            except (subprocess.CalledProcessError, FileNotFoundError):
                # 클립보드 도구가 없으면 출력만
                logging.debug(f"Linux 클립보드 복사 실패. 텍스트: {str_working}")
                return str_working
    else:
        # macOS에서는 pbcopy 사용
        try:
            import subprocess
            subprocess.run(['pbcopy'], input=str_working.encode(), check=True)
            return str_working
        except (subprocess.CalledProcessError, FileNotFoundError):
            logging.debug(f"macOS 클립보드 복사 실패. 텍스트: {str_working}")
            return str_working
    
    return str_working
