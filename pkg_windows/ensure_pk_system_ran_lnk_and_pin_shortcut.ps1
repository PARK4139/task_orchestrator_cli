# PowerShell 스크립트: 바탕화면과 현재 위치에 .lnk 바로가기 생성
# 저장 인코딩은 반드시 UTF-8 with BOM

# 사용자 설정
$TargetCmd = "$PSScriptRoot\ensure_pk_system_ran.cmd"
$ShortcutName = "PK System Launcher"
$IconPath = "$env:SystemRoot\System32\shell32.dll,40"  # 예: 폴더 아이콘

# 생성 위치 목록: 바탕화면 + 현재 스크립트 위치
$ShortcutPaths = @(
    "$env:USERPROFILE\Desktop\$ShortcutName.lnk",
    "$PSScriptRoot\$ShortcutName.lnk"
)

foreach ($ShortcutPath in $ShortcutPaths) {
    $WshShell = New-Object -ComObject WScript.Shell
    $Shortcut = $WshShell.CreateShortcut($ShortcutPath)
    $Shortcut.TargetPath = "cmd.exe"
    $Shortcut.Arguments = "/c `"$TargetCmd`""
    $Shortcut.IconLocation = $IconPath
    $Shortcut.WindowStyle = 1
    $Shortcut.Save()
    Write-Host "[✓] 바로가기 생성됨: $ShortcutPath"
}

Write-Host ""
Write-Host ""
Write-Host "⚠ [작업표시줄 고정]은 수동으로 진행해 주세요:"
Write-Host "1. 바탕화면 바로가기 우클릭 → [작업 표시줄에 고정]"
Write-Host "2. 작업표시줄 왼쪽에 둘 경우 → Win + 1 단축키 가능"
Write-Host ""
Write-Host ""
[void][System.Console]::ReadLine()