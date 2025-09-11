@echo off
title ensure_task_orchestrator_cli_lnk_executed.bat
chcp 65001 >nul
.venv_windows\Scripts\python.exe sources\wrappers\pk_ensure_task_orchestrator_cli_started.py
