@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

@REM 현재 디렉토리 설정
set "SCRIPT_DIR=%USERPROFILE%\Downloads\pk_system"
set "PKG_WINDOWS=%SCRIPT_DIR%\pkg_windows"

@REM Python 찾기 함수
:find_python
@REM 먼저 시스템 python 확인
python --version >nul 2>&1
if %errorlevel%==0 (
    echo ✅ 시스템 Python 발견: python
    set "PYTHON_CMD=python"
    goto :run_script
)

@REM 가상환경 python.exe 확인
if exist "%SCRIPT_DIR%\.venv\Scripts\python.exe" (
    echo ✅ 가상환경 Python 발견: %SCRIPT_DIR%\.venv\Scripts\python.exe
    set "PYTHON_CMD=%SCRIPT_DIR%\.venv\Scripts\python.exe"
    goto :run_script
)

@REM pkg_windows 하위에서 python.exe 찾기
for /r "%PKG_WINDOWS%" %%i in (python.exe) do (
    if exist "%%i" (
        echo ✅ Python.exe 발견: %%i
        set "PYTHON_CMD=%%i"
        goto :run_script
    )
)

@REM 전체 pk_system 하위에서 python.exe 찾기
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
echo 🚀 Python 스크립트 실행 중: %PYTHON_CMD% ensure_pk_system_enabled.py
"%PYTHON_CMD%" ensure_pk_system_enabled.py

@REM 실행 결과 확인
if %errorlevel%==0 (
    echo ✅ 스크립트 실행 완료
) else (
    echo ❌ 스크립트 실행 실패 (오류 코드: %errorlevel%)
    pause
)

endlocal