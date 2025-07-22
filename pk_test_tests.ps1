
# 한글 깨짐 해소
# .ps1 파일은 반드시 UTF-8 with BOM으로 저장


# PowerShell 스크립트: pk_test_tests.ps1

$pythonCandidates = @("python3", "python", "py")
$pythonExe = $null

# 가능한 파이썬 실행기 중 첫 번째 사용 가능한 것 찾기
foreach ($candidate in $pythonCandidates) {
    if (Get-Command $candidate -ErrorAction SilentlyContinue) {
        $pythonExe = $candidate
        break
    }
}
# 실행기 없을 경우 오류 메시지
if (-not $pythonExe) {
    Write-Host "❌ Python 실행기를 찾을 수 없습니다 (python3, python, py)." -ForegroundColor Red
    Write-Host "   https://www.python.org/downloads 에서 설치하세요."
    exit 1
}

Write-Host "✅ 선택된 Python 인터프리터: $pythonExe" -ForegroundColor Green

# 테스트 실행
& $pythonExe pk_test_tests.py
