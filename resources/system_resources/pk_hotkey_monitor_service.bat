@echo off
title task_orchestrator_cli Hotkey Monitor
cd /d "%D_TASK_ORCHESTRATOR_CLI%"

REM 백그라운드에서 단축키 모니터링 시작
echo 🎯 task_orchestrator_cli 단축키 모니터링 서비스 시작...
echo 💡 단축키: Ctrl+Alt+P
echo 💡 종료하려면 Ctrl+C를 누르세요
echo.

REM Python virtual environment 활성화 후 모니터링 시작
call .venv_windows\Scripts\activate.bat
python sources\wrappers\functions\ensure_hotkey_monitor_started.py

REM 오류 발생 시 대기
if errorlevel 1 (
    echo ❌ 모니터링 서비스 오류 발생
    pause
) 