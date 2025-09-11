@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

REM Get the directory of the batch script
set "SCRIPT_DIR=%~dp0"

REM Define paths
set "F_VENV_PYTHON=%SCRIPT_DIR%.venv_windows\Scripts\python.exe"
set "D_VENV_DIR=%SCRIPT_DIR%.venv_windows"
set "D_VENV_DIR_REGACY=%SCRIPT_DIR%.venv"

echo Starting task_orchestrator_cli Uninstallation...

REM --- Step 1: Run Python script for registry and alias cleanup ---
if exist "%F_VENV_PYTHON%" (
    echo Found virtual environment Python. Running cleanup script...
    "%F_VENV_PYTHON%" "%F_UNINSTALL_SCRIPT%"
    if !errorlevel! neq 0 (
        echo WARNING: Python cleanup script failed. Continuing with file deletion...
    ) else (
        echo Python cleanup script completed successfully.
    )
) else (
    echo WARNING: Virtual environment Python not found. Skipping Python cleanup script.
    echo You may need to clean up registry entries and aliases manually.
)
REM Delete D_VENV_DIR
if exist "%D_VENV_DIR%" (
    echo Deleting virtual environment directory: %D_VENV_DIR%
    rd /s /q "%D_VENV_DIR%"
)

REM Delete D_VENV_DIR_REGACY
if exist "%D_VENV_DIR_REGACY%" (
    echo Deleting virtual environment directory: %D_VENV_DIR_REGACY%
    rd /s /q "%D_VENV_DIR_REGACY%"
)


echo --- Uninstallation Complete ---

REM Self-deletion
@REM (goto) 2>nul & del "%~f0" & exit
