chcp 65001 >nul
@echo off
setlocal

set "BASE_DIR=%~dp0"
set "BASE_DIR=%BASE_DIR:~0,-1%"

cls

call "%BASE_DIR%\.venv\Scripts\activate.bat"
python "%BASE_DIR%\copy_to_auto_utility.py"
