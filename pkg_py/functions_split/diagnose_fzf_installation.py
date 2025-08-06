from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured
from pathlib import Path
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.map_massages import PK_ANSI_COLOR_MAP


@ensure_seconds_measured
def diagnose_fzf_installation():
    """fzf 설치 상태를 진단합니다."""
    try:
        # Lazy import to avoid circular dependency
        try:
            from pkg_py.functions_split.ensure_printed import ensure_printed
            from pkg_py.system_object.map_massages import PkMessages2025
        except ImportError:
            print = lambda msg, **kwargs: print(msg)
            PkMessages2025 = type('PkMessages2025', (), {
                'FZF_DIAGNOSIS_START': 'fzf 설치 상태를 진단합니다',
                'FZF_FOUND': 'fzf 발견',
                'FZF_NOT_FOUND': 'fzf를 찾을 수 없음',
                'FZF_EXE_FOUND': 'fzf.exe 발견',
                'FZF_EXE_NOT_FOUND': 'fzf.exe를 찾을 수 없음',
                'FZF_PATH_FOUND': '발견',
                'FZF_PATH_NOT_FOUND': '없음',
                'FZF_EXECUTION_SUCCESS': '실행 성공',
                'FZF_EXECUTION_FAILED': '실행 실패',
                'FZF_CORRUPTED_FILE': '손상된 파일',
                'FZF_OS_ERROR': 'OS 오류',
                'FZF_FILE_NOT_FOUND': '파일 없음',
                'FZF_OTHER_ERROR': '기타 오류',
                'FZF_AVAILABLE': '사용 가능한 fzf',
                'FZF_NOT_AVAILABLE': '사용 가능한 fzf가 없습니다'
            })()

        print(" fzf 설치 상태를 진단합니다...")
        
        # 1. 시스템 PATH에서 fzf 검색
        import shutil
        fzf_path = shutil.which("fzf")
        if fzf_path:
            ensure_printed(f"   [{PkMessages2025.FZF_FOUND}] {PK_ANSI_COLOR_MAP['GREEN']}경로={fzf_path} {PK_ANSI_COLOR_MAP['RESET']}", print_color='green')
        else:
            ensure_printed(f"   [{PkMessages2025.FZF_NOT_FOUND}]", print_color='red')
        
        # 2. Windows에서 fzf.exe 검색
        from pkg_py.system_object.files import F_FZF_EXE
        fzf_exe_path = Path(F_FZF_EXE)
        if fzf_exe_path.exists():
            ensure_printed(f"   [{PkMessages2025.FZF_EXE_FOUND}] {PK_ANSI_COLOR_MAP['GREEN']}경로={fzf_exe_path} {PK_ANSI_COLOR_MAP['RESET']}", print_color='green')
        else:
            ensure_printed(f"   [{PkMessages2025.FZF_EXE_NOT_FOUND}]", print_color='red')
        
        # 3. 일반적인 설치 경로 확인
        common_paths = [
            "/usr/bin/fzf",
            "/usr/local/bin/fzf",
            "/opt/homebrew/bin/fzf",
            str(Path.home() / "fzf.exe"),
            str(Path.home() / ".local/bin/fzf"),
            str(Path.home() / "AppData/Local/Microsoft/WinGet/Packages/Junegunn.fzf_Microsoft.Winget.Source_8wekyb3d8bbwe/fzf.exe")
        ]
        
        found_paths = []
        for path in common_paths:
            if Path(path).exists():
                found_paths.append(path)
                ensure_printed(f"   [{PkMessages2025.FZF_PATH_FOUND}] {PK_ANSI_COLOR_MAP['GREEN']}경로={path} {PK_ANSI_COLOR_MAP['RESET']}", print_color='green')
            else:
                ensure_printed(f"   [{PkMessages2025.FZF_PATH_NOT_FOUND}] {PK_ANSI_COLOR_MAP['GRAY']}경로={path} {PK_ANSI_COLOR_MAP['RESET']}", print_color='gray')
        
        # 4. 실행 테스트
        working_fzf = None
        test_paths = [fzf_path] + found_paths if fzf_path else found_paths
        
        for path in test_paths:
            if not path:
                continue
                
            try:
                import subprocess
                result = subprocess.run([path, "--version"], 
                                      capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    ensure_printed(f"   [{PkMessages2025.FZF_EXECUTION_SUCCESS}] {PK_ANSI_COLOR_MAP['GREEN']}경로={path} {PK_ANSI_COLOR_MAP['RESET']}", print_color='green')
                    working_fzf = path
                    break
                else:
                    ensure_printed(f"   [{PkMessages2025.FZF_EXECUTION_FAILED}] {PK_ANSI_COLOR_MAP['RED']}경로={path} 오류코드={result.returncode} {PK_ANSI_COLOR_MAP['RESET']}", print_color='red')
                    
            except subprocess.TimeoutExpired:
                ensure_printed(f"   [{PkMessages2025.FZF_EXECUTION_FAILED}] {PK_ANSI_COLOR_MAP['RED']}경로={path} 타임아웃 {PK_ANSI_COLOR_MAP['RESET']}", print_color='red')
            except FileNotFoundError:
                ensure_printed(f"   [{PkMessages2025.FZF_FILE_NOT_FOUND}] {PK_ANSI_COLOR_MAP['RED']}경로={path} {PK_ANSI_COLOR_MAP['RESET']}", print_color='red')
            except PermissionError:
                ensure_printed(f"   [{PkMessages2025.FZF_OS_ERROR}] {PK_ANSI_COLOR_MAP['RED']}경로={path} 권한오류 {PK_ANSI_COLOR_MAP['RESET']}", print_color='red')
            except Exception as e:
                ensure_printed(f"   [{PkMessages2025.FZF_OTHER_ERROR}] {PK_ANSI_COLOR_MAP['RED']}경로={path} 오류={e} {PK_ANSI_COLOR_MAP['RESET']}", print_color='red')
        
        # 5. 결과 요약
        if working_fzf:
            ensure_printed(f"   [{PkMessages2025.FZF_AVAILABLE}] {PK_ANSI_COLOR_MAP['GREEN']}경로={working_fzf} {PK_ANSI_COLOR_MAP['RESET']}", print_color='green')
            return working_fzf
        else:
            ensure_printed(f"   [{PkMessages2025.FZF_NOT_AVAILABLE}]", print_color='red')
            return None
            
    except Exception as e:
        ensure_printed(f"[{PkMessages2025.FZF_OTHER_ERROR}] {PK_ANSI_COLOR_MAP['RED']}오류={e} {PK_ANSI_COLOR_MAP['RESET']}", print_color='red')
        return None


if __name__ == "__main__":
    diagnose_fzf_installation()