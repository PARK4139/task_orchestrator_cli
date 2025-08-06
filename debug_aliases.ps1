chcp 65001

# 별칭 등록 문제 진단 및 해결 도구
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "별칭 등록 문제 진단 및 해결 도구" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

Write-Host ""

# 1. 현재 doskey 별칭 확인
Write-Host "1. 현재 doskey 별칭 확인:" -ForegroundColor Yellow
try {
    $macros = cmd /c "doskey /macros" 2>$null
    if ($macros) {
        Write-Host "현재 등록된 별칭:" -ForegroundColor Green
        Write-Host $macros -ForegroundColor Green
    } else {
        Write-Host "등록된 별칭이 없습니다." -ForegroundColor Red
    }
} catch {
    Write-Host "별칭 확인 실패: $_" -ForegroundColor Red
}

Write-Host ""

# 2. doskey 명령어 테스트
Write-Host "2. doskey 명령어 테스트:" -ForegroundColor Yellow
try {
    $testResult = cmd /c "doskey test=echo test_alias" 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ doskey 명령어 정상 작동" -ForegroundColor Green
    } else {
        Write-Host "❌ doskey 명령어 실패" -ForegroundColor Red
    }
} catch {
    Write-Host "❌ doskey 명령어 테스트 실패: $_" -ForegroundColor Red
}

Write-Host ""

# 3. 수동으로 별칭 등록 (상세 로그)
Write-Host "3. 수동으로 별칭 등록 (상세 로그):" -ForegroundColor Yellow
$PK_SYSTEM_PATH = "C:\Users\wjdgn\Downloads\pk_system"

$aliases = @{
    "0" = "cd `"$PK_SYSTEM_PATH`""
    "1" = "cd `"$PK_SYSTEM_PATH\pkg_py`""
    "2" = "cd `"$PK_SYSTEM_PATH\pkg_windows`""
    "3" = "cd `"$env:USERPROFILE\pk_working`""
    "4" = "cd `"$env:USERPROFILE\pk_memo`""
    "5" = "cd `"$env:USERPROFILE\business_demo`""
    "pk" = "python `"$PK_SYSTEM_PATH\pkg_py\pk_ensure_pk_system_enabled.py`""
    "venv" = "`"$PK_SYSTEM_PATH\.venv\Scripts\activate`""
    "ls" = "dir"
    "cat" = "type"
    "which" = "where"
    "pwd" = "cd"
    "gpt" = "start https://chat.openai.com"
    "x" = "exit"
}

$successCount = 0
foreach ($alias in $aliases.GetEnumerator()) {
    Write-Host "등록 시도: $($alias.Key) = $($alias.Value)" -ForegroundColor Gray
    try {
        $doskeyCmd = "doskey $($alias.Key)=$($alias.Value)"
        Write-Host "실행 명령어: $doskeyCmd" -ForegroundColor Gray
        
        $result = cmd /c $doskeyCmd 2>&1
        $exitCode = $LASTEXITCODE
        
        Write-Host "종료 코드: $exitCode" -ForegroundColor Gray
        if ($result) {
            Write-Host "출력: $result" -ForegroundColor Gray
        }
        
        if ($exitCode -eq 0) {
            Write-Host "✅ $($alias.Key) 등록 성공" -ForegroundColor Green
            $successCount++
        } else {
            Write-Host "❌ $($alias.Key) 등록 실패 (코드: $exitCode)" -ForegroundColor Red
        }
    } catch {
        Write-Host "❌ $($alias.Key) 등록 중 예외: $_" -ForegroundColor Red
    }
    Write-Host ""
}

Write-Host "📊 성공한 별칭: $successCount개" -ForegroundColor Cyan

Write-Host ""

# 4. 등록된 별칭 재확인
Write-Host "4. 등록된 별칭 재확인:" -ForegroundColor Yellow
try {
    $macros = cmd /c "doskey /macros" 2>$null
    if ($macros) {
        Write-Host "등록된 별칭:" -ForegroundColor Green
        Write-Host $macros -ForegroundColor Green
    } else {
        Write-Host "등록된 별칭이 없습니다." -ForegroundColor Red
    }
} catch {
    Write-Host "별칭 확인 실패: $_" -ForegroundColor Red
}

Write-Host ""

# 5. 별칭 테스트
Write-Host "5. 별칭 테스트:" -ForegroundColor Yellow
Write-Host "다음 명령어들을 새 CMD 창에서 테스트해보세요:" -ForegroundColor Yellow
Write-Host "   0  # pk_system으로 이동" -ForegroundColor Gray
Write-Host "   1  # pkg_py로 이동" -ForegroundColor Gray
Write-Host "   pk # PK System 재실행" -ForegroundColor Gray
Write-Host "   ls # dir 명령어" -ForegroundColor Gray

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "진단 완료!" -ForegroundColor Green
Write-Host "새 CMD 창을 열어서 별칭을 테스트하세요." -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan

pause