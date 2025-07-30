def ensure_everything_ssd_diagnosis():
    """SSD에서 Everything 성능 문제 진단"""
    import os
    import subprocess
    from pkg_py.functions_split.ensure_printed import ensure_printed
    
    def diagnose_ssd_performance():
        """SSD 성능 진단"""
        ensure_printed("=== SSD에서 Everything 성능 진단 시작 ===", print_color='cyan')
        
        # 1. Windows Search 서비스 상태
        try:
            result = subprocess.run(
                ['sc', 'query', 'WSearch'],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0 and "RUNNING" in result.stdout:
                ensure_printed("✓ Windows Search 서비스: 정상 실행", print_color='green')
            else:
                ensure_printed("✗ Windows Search 서비스: 비활성화", print_color='red')
                return False
        except Exception as e:
            ensure_printed(f"✗ Windows Search 서비스 확인 실패: {e}", print_color='red')
            return False
        
        # 2. Windows Search Index 상태
        try:
            index_result = subprocess.run(
                ['powershell', '-Command', 'Get-WmiObject -Class "Win32_Volume" | Where-Object {$_.DriveLetter -eq "C:"} | Select-Object IndexingEnabled'],
                capture_output=True,
                text=True,
                timeout=10
            )
            if "True" in index_result.stdout:
                ensure_printed("✓ Windows Search Index: 활성화", print_color='green')
            else:
                ensure_printed("✗ Windows Search Index: 비활성화", print_color='red')
                return False
        except Exception as e:
            ensure_printed(f"✗ Windows Search Index 확인 실패: {e}", print_color='red')
            return False
        
        # 3. NTFS USN Journal 상태
        try:
            usn_result = subprocess.run([
                'fsutil', 'usn', 'queryjournal', 'C:'
            ], capture_output=True, text=True, timeout=10)
            
            if usn_result.returncode == 0:
                ensure_printed("✓ NTFS USN Journal: 정상 작동", print_color='green')
            else:
                ensure_printed("✗ NTFS USN Journal: 문제 있음", print_color='red')
                return False
        except Exception as e:
            ensure_printed(f"✗ NTFS USN Journal 확인 실패: {e}", print_color='red')
            return False
        
        # 4. Everything 설정 파일 확인
        everything_ini = os.path.expanduser(r"~\AppData\Roaming\Everything\Everything.ini")
        if os.path.exists(everything_ini):
            with open(everything_ini, 'r', encoding='utf-8') as f:
                content = f.read()
                
                required_settings = [
                    "index_folders=1",
                    "index_files=1",
                    "usn_log=1",
                    "ntfs_volume_guid=1"
                ]
                
                missing_settings = []
                for setting in required_settings:
                    if setting not in content:
                        missing_settings.append(setting)
                
                if missing_settings:
                    ensure_printed(f"✗ Everything 설정 누락: {', '.join(missing_settings)}", print_color='red')
                    return False
                else:
                    ensure_printed("✓ Everything 설정: 완료", print_color='green')
        else:
            ensure_printed("✗ Everything 설정 파일 없음", print_color='red')
            return False
        
        # 5. Everything 실행 테스트
        try:
            everything_paths = [
                r"C:\Program Files\Everything\Everything.exe",
                r"C:\Program Files (x86)\Everything\Everything.exe"
            ]
            
            everything_exe = None
            for path in everything_paths:
                if os.path.exists(path):
                    everything_exe = path
                    break
            
            if everything_exe:
                # 빠른 테스트 실행 (더 짧은 타임아웃과 더 적은 결과)
                test_cmd = f'"{everything_exe}" -startup -a -f -sort -no-gui -no-details -max-results 1'
                test_result = subprocess.run(
                    test_cmd,
                    capture_output=True,
                    text=True,
                    encoding='utf-8',
                    timeout=5,  # 5초로 단축
                    creationflags=subprocess.CREATE_NO_WINDOW
                )
                
                if test_result.returncode == 0:
                    ensure_printed("✓ Everything 실행 테스트: 성공", print_color='green')
                else:
                    ensure_printed("✗ Everything 실행 테스트: 실패", print_color='red')
                    return False
            else:
                ensure_printed("✗ Everything 실행 파일 없음", print_color='red')
                return False
                
        except Exception as e:
            ensure_printed(f"✗ Everything 실행 테스트 실패: {e}", print_color='red')
            return False
        
        ensure_printed("=== SSD 진단 완료: 모든 항목 정상 ===", print_color='green')
        return True
    
    # 진단 실행
    return diagnose_ssd_performance() 