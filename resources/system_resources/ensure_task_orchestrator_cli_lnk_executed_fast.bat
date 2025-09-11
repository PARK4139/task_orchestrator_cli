@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

REM task_orchestrator_cli 루트 디렉토리로 이동
set "TASK_ORCHESTRATOR_CLI_ROOT=C:\Users\pk_system_security_literal\Downloads\task_orchestrator_cli"
cd /d "%TASK_ORCHESTRATOR_CLI_ROOT%" 2>nul || (
    echo ⚠️ task_orchestrator_cli 디렉토리를 찾을 수 없습니다: %TASK_ORCHESTRATOR_CLI_ROOT%
    pause
    exit /b 1
)

REM virtual environment Python 직접 사용 (활성화 과정 생략)
set "PYTHON_EXE=%TASK_ORCHESTRATOR_CLI_ROOT%\.venv_windows\Scripts\python.exe"
if not exist "%PYTHON_EXE%" (
    echo ⚠️ virtual environment Python을 찾을 수 없습니다: %PYTHON_EXE%
    pause
    exit /b 1
)

REM Python 스크립트 실행 (최소한의 출력)
echo [🚀실행] task_orchestrator_cli 시작 중...
"%PYTHON_EXE%" "sources\wrappers\pk_ensure_task_orchestrator_cli_started.py"

REM 실행 완료 후 창 유지 (한 번만 대기)
echo.
echo [✅완료] task_orchestrator_cli 실행 완료. 창을 닫으려면 아무 키나 누르세요...
pause >nul
