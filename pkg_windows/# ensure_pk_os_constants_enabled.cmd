@echo off
chcp 65001 >nul

@REM ______________________________________ import at current session
set PK_URL=https://github.com/astral-sh/uv/releases/download/0.6.12/uv-x86_64-pc-windows-msvc.zip

set D_DOWNLOADS=%USERPROFILE%\Downloads
set D_PK_SYSTEM=%D_DOWNLOADS%\pk_system
set D_PK_WORKING=%D_DOWNLOADS%\pk_working
set D_PK_MEMO=%D_DOWNLOADS%\pk_memo
set D_PKG_WINDOWS=%D_PK_SYSTEM%\pkg_windows
set D_PKG_WINDOWS=%D_PK_SYSTEM%\pkg_windows
set D_PKG_TXT=%D_PK_SYSTEM%\pkg_txt
set D_AUTO_UTILITY=%D_DOWNLOADS%\auto_utility

set F_UV_ZIP=%D_DOWNLOADS%\uv.zip
set F_UV_EXE=%D_PKG_WINDOWS%\uv.exe
set F_PK_ALIAS_MACROS_TXT=%D_PKG_TXT%\pk_alias_macros.txt

@REM ______________________________________ import at next session
setx PK_URL "https://github.com/astral-sh/uv/releases/download/0.6.12/uv-x86_64-pc-windows-msvc.zip"

setx D_DOWNLOADS "%D_DOWNLOADS%"
setx D_PK_SYSTEM "%D_DOWNLOADS%\pk_system"
setx D_PK_WORKING "%D_DOWNLOADS%\pk_working"
setx D_PK_MEMO "%D_DOWNLOADS%\pk_memo"
setx D_PKG_WINDOWS "%D_PK_SYSTEM%\pkg_windows"
setx D_PKG_WINDOWS "%D_PK_SYSTEM%\pkg_windows"
setx D_PKG_TXT "%D_PK_SYSTEM%\pkg_txt"

setx F_UV_ZIP "%D_DOWNLOADS%\uv.zip"
setx F_UV_EXE "%D_PKG_WINDOWS%\uv.exe"
setx F_PK_ALIAS_MACROS_TXT "%D_PKG_TXT%\pk_alias_macros.txt"
setx D_AUTO_UTILITY "%D_DOWNLOADS%\auto_utility"

@REM ______________________________________ set path
set PATH=%PATH%;C:\Users\user\Downloads\pk_system\pkg_windows


@REM ______________________________________ print
@REM echo PK_URL=%PK_URL%
@REM echo D_PKG_WINDOWS=%D_PKG_WINDOWS%
@REM echo F_UV_ZIP=%F_UV_ZIP%
@REM echo F_UV_EXE=%F_UV_EXE%