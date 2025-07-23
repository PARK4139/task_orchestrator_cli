chcp 65001 >nul
@echo off
setlocal

set "BASE_DIR=%~dp0"
set "BASE_DIR=%BASE_DIR:~0,-1%"


call "%BASE_DIR%\.venv\Scripts\activate.bat"

@REM chcp 65001 >nul
@REM setlocal enabledelayedexpansion
@REM set "SCRIPT_NAME=%~nx0"
@REM git add .
@REM git commit -m "make save point by !SCRIPT_NAME!"
@REM git push


set BASENAME=%~n0


python "%BASE_DIR%\%BASENAME%.py"
