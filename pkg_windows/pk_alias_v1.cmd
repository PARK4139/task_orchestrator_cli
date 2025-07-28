@echo off

setlocal
set "D_PK_SYSTEM=%USERPROFILE%\Downloads\pk_system"
set "D_PKG_PY=%D_PK_SYSTEM%\pkg_py"
set "D_PKG_WINDOWS=%D_PK_SYSTEM%\pkg_windows"

call doskey x=exit
call doskey wsld=wsl $*
call doskey wsl24=wsl -d Ubuntu-24.04 $*
call doskey wsl20=wsl -d Ubuntu-20.04 $*
call doskey wsl18=wsl -d Ubuntu-18.04 $*
call doskey reboot=shutdown /r /t 0
call doskey logout=logoff

call doskey cmda="%D_PK_SYSTEM%\pkg_windows\ensure_cmd_exe_ran_as_admin.cmd"
call doskey ps="%D_PK_SYSTEM%\pkg_windows\ensure_powershell_exe_ran.cmd"
call doskey psa=powershell -Command "Start-Process powershell -Verb runAs"

call doskey pycharm="C:\Program Files\JetBrains\PyCharm Community Edition 2024.3.1\bin\pycharm64.exe" $*
@REM call doskey pycharm="C:\Program Files\JetBrains\PyCharm Community Edition 2024.2.4\bin\pycharm64.exe" $*

call doskey 1=cd /d "%D_PK_SYSTEM%"
call doskey 2=cd /d "%USERPROFILE%\Downloads\pk_working"
call doskey 3=cd /d "%USERPROFILE%\Downloads\pk_working\pk_temp"

call doskey .=explorer .
call doskey gpt=explorer "https://chatgpt.com/"
call doskey history=call doskey /history
call doskey cat=wsl cat $*
call doskey which=where $*
call doskey pwd=echo %cd%
call doskey venv=%D_PK_SYSTEM%\.venv\Scripts\activate.bat

call doskey pk=uv run python -m "pkg_py.pk" $* 

@REM call doskey ls=wsl -d wsl ls $*
call doskey ls=dir /b
call doskey rm_f=del /s $*
call doskey rm_d=rmdir /s /q $*
call doskey find_f= wsl sudo find -type f -name "*$*"
call doskey find_d= wsl sudo find -type d -name "*$*"
call doskey find_pnx= wsl sudo find -name "*$*"
call doskey cp_pwd=powershell -Command "Set-Clipboard -Value '%cd%'"

endlocal

@REM uv run python -m pkg_py.pk_paste_as_auto