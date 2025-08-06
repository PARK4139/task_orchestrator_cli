@echo off
echo ========================================
echo Windows PK System 별칭 문제 해결 도구
echo ========================================

echo.
echo 1. 현재 레지스트리 AutoRun 설정 확인:
reg query "HKCU\Software\Microsoft\Command Processor" /v AutoRun

echo.
echo 2. 기존 AutoRun 설정 제거:
reg delete "HKCU\Software\Microsoft\Command Processor" /v AutoRun /f

echo.
echo 3. 새로운 배치 파일 기반 AutoRun 설정:
set "PK_SYSTEM_PATH=C:\Users\wjdgn\Downloads\pk_system"
set "BATCH_FILE=%PK_SYSTEM_PATH%\pkg_cache_private\ensure_pk_alias_enabled.bat"

if exist "%BATCH_FILE%" (
    reg add "HKCU\Software\Microsoft\Command Processor" /v AutoRun /t REG_SZ /d "\"%BATCH_FILE%\"" /f
    echo ✅ 새로운 AutoRun 설정 완료: %BATCH_FILE%
) else (
    echo ❌ 배치 파일을 찾을 수 없습니다: %BATCH_FILE%
)

echo.
echo 4. 수동으로 별칭 등록:
doskey 0=cd "%PK_SYSTEM_PATH%"
doskey 1=cd "%PK_SYSTEM_PATH%\pkg_py"
doskey 2=cd "%PK_SYSTEM_PATH%\pkg_windows"
doskey 3=cd "%USERPROFILE%\pk_working"
doskey 4=cd "%USERPROFILE%\pk_memo"
doskey 5=cd "%USERPROFILE%\business_demo"
doskey pk=python "%PK_SYSTEM_PATH%\pkg_py\pk_ensure_pk_system_enabled.py"
doskey venv="%PK_SYSTEM_PATH%\.venv\Scripts\activate"
doskey ls=dir
doskey cat=type
doskey which=where
doskey pwd=cd
doskey gpt=start https://chat.openai.com
doskey x=exit

echo.
echo 5. 등록된 별칭 확인:
doskey /macros

echo.
echo ========================================
echo 문제 해결 완료!
echo 새 CMD 창을 열어서 별칭이 작동하는지 확인하세요.
echo ========================================
pause 