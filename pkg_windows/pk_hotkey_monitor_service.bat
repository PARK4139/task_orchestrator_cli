@echo off
title PK System Hotkey Monitor
cd /d "%D_PK_SYSTEM%"

REM 백그라운드에서 단축키 모니터링 시작
echo 🎯 PK System 단축키 모니터링 서비스 시작...
echo 💡 단축키: Ctrl+Alt+P
echo 💡 종료하려면 Ctrl+C를 누르세요
echo.

REM Python 가상환경 활성화 후 모니터링 시작
call .venv\Scripts\activate.bat
python pkg_py\functions_split\ensure_hotkey_monitor_started.py

REM 오류 발생 시 대기
if errorlevel 1 (
    echo ❌ 모니터링 서비스 오류 발생
    pause
) 