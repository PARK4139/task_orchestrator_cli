@echo off

set "D_PK_SYSTEM=%USERPROFILE%\Downloads\pk_system"
set "D_PKG_PY=%D_PK_SYSTEM%\pkg_py"
set "D_PKG_WINDOWS=%D_PK_SYSTEM%\pkg_windows"
set "D_pkg_txt=%D_PK_SYSTEM%\pkg_txt"

doskey /macrofile="%D_pkg_txt%\pk_alias_macros.txt"