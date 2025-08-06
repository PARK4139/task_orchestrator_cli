# PK System Hotkey Monitor Service 등록 스크립트
# Windows 시작 프로그램에 등록하여 부팅 시 자동 실행

param(
    [string]$Hotkey = "ctrl+alt+p",
    [string]$ProjectPath = $env:D_PK_SYSTEM
)

# 프로젝트 경로 설정
if (-not $ProjectPath) {
    $ProjectPath = "C:\Users\wjdgn\Downloads\pk_system"
}

# PowerShell 스크립트 경로
$ScriptPath = Join-Path $ProjectPath "pkg_windows\pk_hotkey_monitor_service.ps1"
$ShortcutPath = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\PK_System_Hotkey_Monitor.lnk"

Write-Host "🔧 PK System 단축키 모니터링 서비스 등록 중..." -ForegroundColor Green

# PowerShell 실행 정책 확인 및 설정
try {
    $ExecutionPolicy = Get-ExecutionPolicy -Scope CurrentUser
    if ($ExecutionPolicy -eq "Restricted") {
        Write-Host "⚠️ PowerShell 실행 정책을 변경합니다..." -ForegroundColor Yellow
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
        Write-Host "✅ 실행 정책 변경 완료" -ForegroundColor Green
    }
}
catch {
    Write-Host "❌ 실행 정책 설정 실패: $_" -ForegroundColor Red
    exit 1
}

# 시작 프로그램 폴더 확인
$StartupFolder = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup"
if (-not (Test-Path $StartupFolder)) {
    New-Item -ItemType Directory -Path $StartupFolder -Force | Out-Null
}

# 단축키 생성
try {
    $WshShell = New-Object -ComObject WScript.Shell
    $Shortcut = $WshShell.CreateShortcut($ShortcutPath)
    
    # PowerShell 실행 명령어 설정
    $Shortcut.TargetPath = "powershell.exe"
    $Shortcut.Arguments = "-ExecutionPolicy Bypass -File `"$ScriptPath`" -Hotkey `"$Hotkey`" -ProjectPath `"$ProjectPath`""
    $Shortcut.WorkingDirectory = $ProjectPath
    $Shortcut.Description = "PK System Hotkey Monitor Service"
    $Shortcut.IconLocation = "powershell.exe,0"
    
    $Shortcut.Save()
    
    Write-Host "✅ 단축키 생성 완료: $ShortcutPath" -ForegroundColor Green
    Write-Host "💡 단축키: $Hotkey" -ForegroundColor Cyan
    Write-Host "🔄 다음 부팅 시 자동으로 시작됩니다." -ForegroundColor Yellow
    
    # 즉시 시작 옵션
    $StartNow = Read-Host "지금 바로 모니터링을 시작하시겠습니까? (y/n)"
    if ($StartNow -eq "y" -or $StartNow -eq "Y") {
        Write-Host "🚀 모니터링 서비스 시작 중..." -ForegroundColor Green
        & $ScriptPath -Hotkey $Hotkey -ProjectPath $ProjectPath
    }
    
}
catch {
    Write-Host "❌ 단축키 생성 실패: $_" -ForegroundColor Red
    exit 1
}

Write-Host "🎉 등록 완료!" -ForegroundColor Green 