@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion


@REM v1 : demo
@REM echo [🔧시작] task_orchestrator_cli launcher 실행 중...
@REM
@REM echo [🔧이동] task_orchestrator_cli 루트 디렉토리로 이동 중...
@REM set "D_TASK_ORCHESTRATOR_CLI=%USERPROFILE%\Downloads\task_orchestrator_cli"
@REM cd /d "%D_TASK_ORCHESTRATOR_CLI%"
@REM
@REM echo [🔧활성화] Windows virtual environment 활성화 중...
@REM call ".venv_windows\Scripts\activate.bat"
@REM
@REM echo [🔧실행] task_orchestrator_cli 실행 중...
@REM set "SCRIPT_PATH=sources\wrappers\pk_ensure_task_orchestrator_cli_started.py"
@REM python "%SCRIPT_PATH%"



@REM v2 : 속도개선버전
echo [🔧시작] task_orchestrator_cli launcher 실행 중...
set "D_TASK_ORCHESTRATOR_CLI=%USERPROFILE%\Downloads\task_orchestrator_cli"
set "F_VENV_PYTHON=%D_TASK_ORCHESTRATOR_CLI%\.venv_windows\Scripts\python.exe"

echo [🔧이동] task_orchestrator_cli 루트 디렉토리로 이동 중...
cd /d "%D_TASK_ORCHESTRATOR_CLI%"

echo [🔧실행] task_orchestrator_cli 실행 중...
"%F_VENV_PYTHON%" "sources\wrappers\pk_ensure_task_orchestrator_cli_started.py"



if !ERRORLEVEL! equ 1 (
    echo [테스트 시도가이드 ]
    echo "uninstall.cmd && install.cmd"
    echo "git reset --hard HEAD^^ && git pull && install.cmd"
    pause >nul
)