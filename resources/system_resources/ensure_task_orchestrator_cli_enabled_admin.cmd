@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

@REM 관리자 권한 확인
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️ 관리자 권한이 필요합니다.
    echo 🔄 관리자 권한으로 다시 실행합니다...
    echo.
    echo 💡 권한 문제 해결 방법:
    echo    1. 이 파일을 우클릭 → "관리자 권한으로 실행"
    echo    2. 또는 PowerShell을 관리자 권한으로 실행 후 직접 실행
    echo.
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

echo ✅ 관리자 권한으로 실행 중입니다.
echo.

@REM 현재 디렉토리 설정
set "SCRIPT_DIR=%USERPROFILE%\Downloads\task_orchestrator_cli"
set "TASK_ORCHESTRATOR_CLI_OS_LAYER=%SCRIPT_DIR%\system_resources"

@REM Python 찾기 함수
:find_python
@REM 먼저 시스템 python 확인
python --version >nul 2>&1
if %errorlevel%==0 (
    echo ✅ 시스템 Python 발견: python
    set "PYTHON_CMD=python"
    goto :run_script
)

@REM virtual environment python.exe 확인
if exist "%SCRIPT_DIR%\.venv_windows\Scripts\python.exe" (
echo task_orchestrator_cli virtual environment python detected: %SCRIPT_DIR%\.venv_windows\Scripts\python.exe
set "PYTHON_CMD=%SCRIPT_DIR%\.venv_windows\Scripts\python.exe"
    goto :run_script
)

@REM system_resources 하위에서 python.exe 찾기
for /r "%TASK_ORCHESTRATOR_CLI_OS_LAYER%" %%i in (python.exe) do (
    if exist "%%i" (
        echo ✅ Python.exe 발견: %%i
        set "PYTHON_CMD=%%i"
        goto :run_script
    )
)

@REM 전체 task_orchestrator_cli 하위에서 python.exe 찾기
for /r "%SCRIPT_DIR%" %%i in (python.exe) do (
    if exist "%%i" (
        echo ✅ Python.exe 발견: %%i
        set "PYTHON_CMD=%%i"
        goto :run_script
    )
)

@REM Python을 찾을 수 없는 경우
echo ❌ Python을 찾을 수 없습니다.
echo 📥 Python 설치를 시도합니다...
echo.
echo 다음 중 하나를 선택하세요:
echo 1. Microsoft Store에서 Python 설치 (권장)
echo 2. python.org에서 수동 설치
echo 3. 취소
echo.
set /p choice="선택 (1-3): "

if "%choice%"=="1" (
    echo 🛒 Microsoft Store에서 Python 설치 중...
    start ms-windows-store://pdp/?ProductId=9NRWMJP3717K
    echo 설치 완료 후 이 스크립트를 다시 실행하세요.
    pause
    exit /b 1
) else if "%choice%"=="2" (
    echo 🌐 python.org로 이동 중...
    start https://www.python.org/downloads/
    echo 설치 완료 후 이 스크립트를 다시 실행하세요.
    pause
    exit /b 1
) else (
    echo 취소되었습니다.
    pause
    exit /b 1
)

:run_script
@REM Python으로 스크립트 실행
echo 🚀 Python 스크립트 실행 중 (관리자 권한): %PYTHON_CMD% %SCRIPT_DIR%\sources\wrappers\functions\ensure_task_orchestrator_cli_enabled.py
echo.
echo 💡 권한 문제가 발생하면 다음을 확인하세요:
echo    1. Windows Defender 예외 목록에 추가
echo    2. 바이러스 백신 일시 비활성화
echo    3. 사용자 계정 제어(UAC) 설정 확인
echo.
"%PYTHON_CMD%" "%SCRIPT_DIR%\sources\wrappers\functions\ensure_task_orchestrator_cli_enabled.py"

@REM 실행 결과 확인
if %errorlevel%==0 (
    echo ✅ 스크립트 실행 완료
) else (
    echo ❌ 스크립트 실행 실패 (오류 코드: %errorlevel%)
    echo.
    echo 💡 추가 해결 방법:
    echo    1. README_WINDOWS_PERMISSIONS.md 파일 참조
    echo    2. 대안 위치에 설치된 파일 확인: %USERPROFILE%\Downloads\
    echo    3. 시스템 재부팅 후 재시도
    pause
)

endlocal 