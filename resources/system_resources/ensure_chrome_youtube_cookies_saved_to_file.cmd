:: @echo off
chcp 65001 >nul
title %~nx0
cls

net session >nul 2>&1
if %errorLevel% neq 0 (
powershell -Command "Start-Process python -ArgumentList '\"%~dp0myscript.py\"' -Verb RunAs"
exit /b
)
cls

call "%USERPROFILE%\Downloads\task_orchestrator_cli\.venv_windows\Scripts\activate.bat"
