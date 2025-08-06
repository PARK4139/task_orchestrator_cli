# PowerShell PK System 별칭 테스트
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "PowerShell PK System 별칭 테스트" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

Write-Host ""

# 1. 현재 doskey 별칭 확인
Write-Host "1. 현재 doskey 별칭 확인:" -ForegroundColor Yellow
try {
    $macros = cmd /c "doskey /macros" 2>$null
    if ($macros) {
        Write-Host $macros -ForegroundColor Green
    } else {
        Write-Host "등록된 별칭이 없습니다." -ForegroundColor Red
    }
} catch {
    Write-Host "별칭 확인 실패: $_" -ForegroundColor Red
}

Write-Host ""

# 2. PK System 별칭 테스트
Write-Host "2. PK System 별칭 테스트:" -ForegroundColor Yellow

# '0' 명령어 테스트 (pk_system으로 이동)
Write-Host "- '0' 명령어 테스트 (pk_system으로 이동):" -ForegroundColor Yellow
$currentDir = Get-Location
Write-Host "현재 디렉토리: $currentDir" -ForegroundColor Gray

try {
    cmd /c "0"
    $newDir = Get-Location
    Write-Host "이동 후 디렉토리: $newDir" -ForegroundColor Gray
} catch {
    Write-Host "❌ '0' 명령어 실패: $_" -ForegroundColor Red
}

Write-Host ""

# 'pk' 명령어 테스트
Write-Host "- 'pk' 명령어 테스트:" -ForegroundColor Yellow
try {
    cmd /c "pk"
    Write-Host "✅ 'pk' 명령어 실행됨" -ForegroundColor Green
} catch {
    Write-Host "❌ 'pk' 명령어 실패: $_" -ForegroundColor Red
}

Write-Host ""

# 'venv' 명령어 테스트
Write-Host "- 'venv' 명령어 테스트:" -ForegroundColor Yellow
try {
    cmd /c "venv"
    Write-Host "✅ 'venv' 명령어 실행됨" -ForegroundColor Green
} catch {
    Write-Host "❌ 'venv' 명령어 실패: $_" -ForegroundColor Red
}

Write-Host ""

# 'ls' 명령어 테스트
Write-Host "- 'ls' 명령어 테스트 (dir 대신):" -ForegroundColor Yellow
try {
    cmd /c "ls"
    Write-Host "✅ 'ls' 명령어 실행됨" -ForegroundColor Green
} catch {
    Write-Host "❌ 'ls' 명령어 실패: $_" -ForegroundColor Red
}

Write-Host ""

# 'gpt' 명령어 테스트
Write-Host "- 'gpt' 명령어 테스트:" -ForegroundColor Yellow
try {
    cmd /c "gpt"
    Write-Host "✅ 'gpt' 명령어 실행됨" -ForegroundColor Green
} catch {
    Write-Host "❌ 'gpt' 명령어 실패: $_" -ForegroundColor Red
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "테스트 완료!" -ForegroundColor Green
Write-Host "별칭이 제대로 작동하지 않으면 새 CMD 창을 열어서 테스트해보세요." -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan

Read-Host "엔터 키를 눌러 종료하세요" 