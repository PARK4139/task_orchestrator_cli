@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion
@REM setlocal EnableExtensions EnableDelayedExpansion

set "D_TASK_ORCHESTRATOR_CLI=%USERPROFILE%\Downloads\task_orchestrator_cli"
set "D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES=%USERPROFILE%\Downloads\task_orchestrator_cli\system_resources"
set "D_VENV=%D_TASK_ORCHESTRATOR_CLI%\.venv_windows"
set "F_VENV_PYTHON=%D_VENV%\Scripts\python.exe"
set "F_VENV_ACTIVATE=%D_VENV%\Scripts\activate"
set "F_ENSURE_UV_ENABLED_CMD=%D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES%\ensure_uv_enabled.cmd"
set "F_UV=%D_TASK_ORCHESTRATOR_CLI%\uv.exe"


@REM     echo ℹ️ uv 미설치, uv 를 설치해야 합니다.
@REM    call "%F_ENSURE_UV_ENABLED_CMD%"

REM === virtual environment 확인/생성 ===
if exist "%F_VENV_PYTHON%" (
    echo task_orchestrator_cli virtual environment python detected: "%F_VENV_PYTHON%"
    call "%F_VENV_ACTIVATE%"
    goto :run_script
) else (
    if exist "%D_VENV%" (
        echo .venv_windows virtual environment 경로 발견 %D_VENV%
    ) else (
        cd /d %D_TASK_ORCHESTRATOR_CLI%
        %F_UV% venv ".venv_windows" || (echo ❌ uv venv 생성 실패 & popd & exit /b 1)
        call "%F_VENV_ACTIVATE%"
@REM         %F_UV% sync --active -vvv
        %F_UV% sync --active
    )

    popd
    if exist "%F_VENV_PYTHON%" (
        echo task_orchestrator_cli virtual environment python detected: "%F_VENV_PYTHON%"
        goto :run_script
    ) else (
        echo ❌ virtual environment Python 경로가 없습니다: "%F_VENV_PYTHON%"
        exit /b 1
        pause
    )
)


@REM TODO : ensure_python_installed.cmd
@REM @REM Python을 찾을 수 없는 경우
@REM echo ❌ Python을 찾을 수 없습니다.
@REM echo ✅ Python 설치를 시도합니다...
@REM echo.
@REM echo 다음 중 하나를 선택하세요:
@REM echo 1. Microsoft Store에서 Python 설치 (권장)
@REM echo 2. python.org에서 수동 설치
@REM echo 3. 취소
@REM echo.
@REM set /p choice="선택 (1-3): "
@REM if "%choice%"=="1" (
@REM     echo 🛒 Microsoft Store에서 Python 설치 중...
@REM     start ms-windows-store://pdp/?ProductId=9PNRBTZXMB4Z
@REM     echo 설치 완료 후 이 스크립트를 다시 실행하세요.
@REM     pause
@REM     exit /b 1
@REM ) else if "%choice%"=="2" (
@REM     echo 🌐 python.org로 이동 중...
@REM     start https://www.python.org/downloads/
@REM     echo 설치 완료 후 이 스크립트를 다시 실행하세요.
@REM     pause
@REM     exit /b 1
@REM ) else (
@REM     echo 취소되었습니다.
@REM     pause
@REM     exit /b 1
@REM )

:run_script
echo 실행 중: %F_VENV_PYTHON% %D_TASK_ORCHESTRATOR_CLI%\sources\wrappers\pk_ensure_task_orchestrator_cli_enabled.py
if exist "%F_VENV_ACTIVATE%" (
    cd /d "%D_TASK_ORCHESTRATOR_CLI%"
    @REM     call "%D_TASK_ORCHESTRATOR_CLI%\.venv_windows\Scripts\activate"   (이거 잘 동작함)
    call "%F_VENV_ACTIVATE%"
    uv run --active -m sources.wrappers.pk_ensure_task_orchestrator_cli_enabled
)