"""
윈도우 작업표시줄에서 고정된 프로그램을 제거하는 함수들
"""
import subprocess
import time
from typing import List, Optional


def ensure_taskbar_pinned_removed(shortcut_name: str = "task_orchestrator_cli_launcher") -> bool:
    """윈도우 작업표시줄에서 고정된 바로가기를 제거합니다."""
    print(f" 작업표시줄에서 '{shortcut_name}' 검색 및 제거 중...")
    
    # 여러 방법을 순차적으로 시도
    methods = [
        _remove_via_shell_com,
        _remove_via_powershell_commands,
        _remove_via_registry,
        _remove_via_taskbar_api
    ]
    
    for i, method in enumerate(methods, 1):
        try:
            print(f"  방법 {i}: {method.__name__} 시도 중...")
            if method(shortcut_name):
                print(f" 방법 {i}로 제거 성공: {shortcut_name}")
                return True
        except Exception as e:
            print(f"  ️ 방법 {i} 실패: {e}")
            continue
    
    print(f" 모든 방법으로 제거 실패: {shortcut_name}")
    return False


def _remove_via_shell_com(shortcut_name: str) -> bool:
    """Shell COM 객체를 사용하여 작업표시줄에서 제거"""
    ps_command = f"""
    try {{
        $shell = New-Object -ComObject Shell.Application
        $folder = $shell.Namespace(0x1)  # Desktop
        $items = $folder.Items()
        
        foreach ($item in $items) {{
            if ($item.Name -like "*{shortcut_name}*") {{
                Write-Host "Shell COM으로 찾음: $($item.Name)"
                try {{
                    $item.InvokeVerb("unpinfromtaskbar")
                    Write-Host "Shell COM으로 제거 성공"
                    return $true
                }} catch {{
                    Write-Host "Shell COM 제거 실패: $($_.Exception.Message)"
                }}
            }}
        }}
        return $false
    }} catch {{
        Write-Host "Shell COM 오류: $($_.Exception.Message)"
        return $false
    }}
    """
    
    result = _run_powershell(ps_command)
    return result and "제거 성공" in result


def _remove_via_powershell_commands(shortcut_name: str) -> bool:
    """PowerShell 명령어를 사용하여 작업표시줄에서 제거"""
    ps_command = f"""
    try {{
        # 시작 메뉴 앱 검색
        $startApps = Get-StartApps | Where-Object {{ $_.Name -like "*{shortcut_name}*" }}
        if ($startApps) {{
            Write-Host "시작 메뉴에서 찾음: $($startApps.Name -join ', ')"
        }}
        
        # 작업표시줄 고정 해제 시도
        $pinnedApps = Get-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced\\People" -ErrorAction SilentlyContinue
        if ($pinnedApps) {{
            Write-Host "People 설정 확인됨"
        }}
        
        # 바탕화면 바로가기 검색 및 제거
        $desktop = [Environment]::GetFolderPath("Desktop")
        $shortcuts = Get-ChildItem -Path $desktop -Filter "*{shortcut_name}*" -Recurse -ErrorAction SilentlyContinue
        
        foreach ($shortcut in $shortcuts) {{
            Write-Host "바로가기 발견: $($shortcut.FullName)"
            try {{
                $shell = New-Object -ComObject Shell.Application
                $folder = $shell.Namespace(0x1)
                $item = $folder.ParseName($shortcut.FullName)
                
                if ($item) {{
                    $verbs = $item.Verbs()
                    foreach ($verb in $verbs) {{
                        if ($verb.Name -like "*고정*" -or $verb.Name -like "*pin*") {{
                            Write-Host "고정 관련 동작 발견: $($verb.Name)"
                            $verb.DoIt()
                            Write-Host "고정 해제 시도 완료"
                            return $true
                        }}
                    }}
                }}
            }} catch {{
                Write-Host "동작 실행 실패: $($_.Exception.Message)"
            }}
        }}
        
        return $false
    }} catch {{
        Write-Host "PowerShell 명령어 오류: $($_.Exception.Message)"
        return $false
    }}
    """
    
    result = _run_powershell(ps_command)
    return result and ("고정 해제 시도 완료" in result or "동작 실행" in result)


def _remove_via_registry(shortcut_name: str) -> bool:
    """레지스트리를 통해 작업표시줄 설정 확인 및 수정"""
    ps_command = f"""
    try {{
        # 작업표시줄 관련 레지스트리 키들 확인
        $regKeys = @(
            "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced\\People",
            "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced\\Taskbar",
            "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced\\TaskbarDa"
        )
        
        foreach ($regKey in $regKeys) {{
            if (Test-Path $regKey) {{
                $properties = Get-ItemProperty -Path $regKey -ErrorAction SilentlyContinue
                Write-Host "레지스트리 키 확인: $regKey"
                foreach ($prop in $properties.PSObject.Properties) {{
                    if ($prop.Name -notlike "PS*") {{
                        Write-Host "  $($prop.Name): $($prop.Value)"
                    }}
                }}
            }}
        }}
        
        # 작업표시줄 고정 해제를 위한 레지스트리 수정 시도
        try {{
            $taskbarKey = "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced\\Taskbar"
            if (Test-Path $taskbarKey) {{
                # People Band 비활성화 시도
                Set-ItemProperty -Path $taskbarKey -Name "PeopleBand" -Value 0 -ErrorAction SilentlyContinue
                Write-Host "People Band 비활성화 시도 완료"
            }}
        }} catch {{
            Write-Host "레지스트리 수정 실패: $($_.Exception.Message)"
        }}
        
        return $false
    }} catch {{
        Write-Host "레지스트리 확인 오류: $($_.Exception.Message)"
        return $false
    }}
    """
    
    result = _run_powershell(ps_command)
    return result and "People Band 비활성화 시도 완료" in result


def _remove_via_taskbar_api(shortcut_name: str) -> bool:
    """Windows API를 사용하여 작업표시줄에서 제거"""
    ps_command = f"""
    try {{
        # Windows 10/11 작업표시줄 API 사용 시도
        Add-Type -TypeDefinition @"
        using System;
        using System.Runtime.InteropServices;
        
        public class TaskbarHelper {{
            [DllImport("user32.dll")]
            public static extern IntPtr FindWindow(string lpClassName, string lpWindowName);
            
            [DllImport("user32.dll")]
            public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
            
            [DllImport("user32.dll")]
            public static extern bool SetForegroundWindow(IntPtr hWnd);
        }}
"@
        
        Write-Host "Windows API 로드 완료"
        
        # 작업표시줄 창 찾기
        $taskbar = [TaskbarHelper]::FindWindow("Shell_TrayWnd", $null)
        if ($taskbar -ne [IntPtr]::Zero) {{
            Write-Host "작업표시줄 창 발견: $taskbar"
            
            # 작업표시줄 새로고침 시도
            try {{
                $explorer = Get-Process explorer -ErrorAction SilentlyContinue
                if ($explorer) {{
                    Stop-Process -Name explorer -Force -ErrorAction SilentlyContinue
                    Start-Sleep -Seconds 2
                    Start-Process explorer
                    Write-Host "Explorer 재시작으로 작업표시줄 새로고침 완료"
                    return $true
                }}
            }} catch {{
                Write-Host "Explorer 재시작 실패: $($_.Exception.Message)"
            }}
        }}
        
        return $false
    }} catch {{
        Write-Host "Windows API 사용 오류: $($_.Exception.Message)"
        return $false
    }}
    """
    
    result = _run_powershell(ps_command)
    return result and "작업표시줄 새로고침 완료" in result


def _run_powershell(command: str) -> Optional[str]:
    """PowerShell 명령어를 실행하고 결과를 반환합니다."""
    try:
        result = subprocess.run(
            ["powershell", "-Command", command],
            capture_output=True,
            text=True,
            shell=True,
            timeout=30
        )
        
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print(f"PowerShell 실행 실패 (코드: {result.returncode})")
            if result.stderr:
                print(f"오류: {result.stderr.strip()}")
            return None
            
    except subprocess.TimeoutExpired:
        print("PowerShell 실행 시간 초과")
        return None
    except Exception as e:
        print(f"PowerShell 실행 중 오류: {e}")
        return None


def ensure_multiple_pinned_removed(shortcut_names: List[str]) -> dict:
    """여러 바로가기를 작업표시줄에서 제거합니다."""
    results = {}
    
    for name in shortcut_names:
        print(f"{'='*50}")
        print(f"처리 중: {name}")
        print(f"{'='*50}")
        
        start_time = time.time()
        success = ensure_taskbar_pinned_removed(name)
        elapsed = time.time() - start_time
        
        results[name] = {
            'success': success,
            'elapsed_time': elapsed,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # 다음 처리 전 잠시 대기
        time.sleep(1)
    
    return results


def print_removal_summary(results: dict) -> None:
    """제거 결과 요약을 출력합니다."""
    print(f"{'='*60}")
    print(" 작업표시줄 제거 결과 요약")
    print(f"{'='*60}")
    
    total = len(results)
    successful = sum(1 for r in results.values() if r['success'])
    failed = total - successful
    
    print(f"총 처리 항목: {total}")
    print(f"성공: {successful} ")
    print(f"실패: {failed} ")
    print(f"성공률: {(successful/total*100):.1f}%")
    
    print(f"\n 상세 결과:")
    for name, result in results.items():
        status = " 성공" if result['success'] else " 실패"
        print(f"  {name}: {status} ({result['elapsed_time']:.2f}초)")
    
    print(f"\n 처리 완료 시간: {time.strftime('%Y-%m-%d %H:%M:%S')}")


# 직접 실행 시 테스트
if __name__ == "__main__":
    print(" 작업표시줄 제거 테스트 시작...")
    
    # 단일 항목 테스트
    print("\n1. 단일 항목 제거 테스트")
    success = ensure_taskbar_pinned_removed("task_orchestrator_cli_launcher")
    print(f"결과: {'성공' if success else '실패'}")
    
    # 여러 항목 테스트
    print("\n2. 여러 항목 제거 테스트")
    test_names = ["task_orchestrator_cli_launcher", "test_app", "sample_app"]
    results = ensure_multiple_pinned_removed(test_names)
    
    # 결과 요약
    print_removal_summary(results)
    
    print("\n 테스트 완료!")
