def ensure_copied(str_working):
    from pkg_py.functions_split.is_os_linux import is_os_linux
    from pkg_py.functions_split.is_os_windows import is_os_windows
    
    if is_os_windows():
        # Windows에서는 clipboard 라이브러리 사용
        import clipboard
        clipboard.copy(str_working)
    elif is_os_linux():
        # Linux에서는 xclip 또는 xsel 사용
        try:
            import subprocess
            subprocess.run(['xclip', '-selection', 'clipboard'], input=str_working.encode(), check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            try:
                subprocess.run(['xsel', '--clipboard'], input=str_working.encode(), check=True)
            except (subprocess.CalledProcessError, FileNotFoundError):
                # 클립보드 도구가 없으면 출력만
                print(f"클립보드 복사 실패. 텍스트: {str_working}")
    else:
        # macOS에서는 pbcopy 사용
        try:
            import subprocess
            subprocess.run(['pbcopy'], input=str_working.encode(), check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print(f"클립보드 복사 실패. 텍스트: {str_working}")
    
    return str_working
