@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

@REM echo ──────────────────────────────────────────────────────────
@REM Step 01: Backup existing PATH
@REM set OLD_PATH=%PATH%
@REM echo %OLD_PATH% > "%USERPROFILE%\Desktop\old_path_backup.txt"
@REM 중복 확인
@REM for /f "delims=" %%a in ('echo %PATH% ^| find /i "%VSCODE_PATH%"') do set FOUND=1
@REM if not defined FOUND (
@REM     setx /M PATH "%PATH%;%VSCODE_PATH%"
@REM     echo VS Code path has been added.
@REM ) else (
@REM     echo VS Code path already exists.
@REM )

echo ──────────────────────────────────────────────────────────
:: OS Variable PATH Management
set PATH "%PATH%;%D_PKG_EXE%"
setx PATH "%PATH%;%D_PKG_EXE%"
@REM call "%D_PKG_WINDOWS%\pk_ensure_windows_os_variable_path_deduplicated.cmd"
@REM python "%D_PKG_PY%\pk_ensure_windows_os_variable_path_deduplicated.py"   관리자 권한으로 실행이 되어야 합니다.

echo ──────────────────────────────────────────────────────────
:: Initial state
set "CURRENT_STEP="
set "D_PKG_WINDOWS=%USERPROFILE%\Downloads\pk_system\pkg_windows"
echo ──────────────────────────────────────────────────────────

:: Step 00: ensure OS variable
call "%D_PKG_WINDOWS%\ensure_pk_os_constants_imported.cmd"
set "VSCODE_PATH=%USERPROFILE%\AppData\Local\Programs\Microsoft VS Code\bin"

echo ──────────────────────────────────────────────────────────
:: Step 02: Start message
powershell -Command "Write-Host 'ensure_pk_imported.cmd started' -ForegroundColor Cyan"

echo ──────────────────────────────────────────────────────────
:: Step 10: Import pk_alias
set "CURRENT_STEP=Importing pk_alias"
powershell -Command "Write-Host '[1/6] %CURRENT_STEP%' -ForegroundColor Cyan"
call "%D_PKG_WINDOWS%\ensure_pk_alias_imorted.cmd" || goto END

echo ──────────────────────────────────────────────────────────
:: Step 20: Import ahk
@REM set "CURRENT_STEP=Importing ahk"
@REM powershell -Command "Write-Host '[2/6] %CURRENT_STEP%' -ForegroundColor Cyan"
@REM taskkill /f /im AutoHotkeyU64.exe >nul 2>&1
@REM icacls "%USERPROFILE%\Downloads\pk_archived\AutoHotkey_Portable\AutoHotkeyU64.exe" /grant "%USERNAME%":F >nul 2>&1
@REM call "%D_PKG_WINDOWS%\ensure_pk_ahk_imorted.cmd"
echo ──────────────────────────────────────────────────────────
:: Step 30: Installing uv
set "CURRENT_STEP=Installing uv"
powershell -Command "Write-Host '[3/6] %CURRENT_STEP%' -ForegroundColor Cyan"
call "%D_PKG_WINDOWS%\ensure_uv_installed.cmd" || goto END

echo ──────────────────────────────────────────────────────────
:: Step 40: Syncing uv
set "CURRENT_STEP=Syncing uv packages"
powershell -Command "Write-Host '[4/6] %CURRENT_STEP%' -ForegroundColor Cyan"
set "UV_PATH=%USERPROFILE%\Downloads\pk_system\pkg_exe"
set "PATH=%PATH%;%UV_PATH%"
call "%D_PKG_WINDOWS%\ensure_uv_synced.cmd" || goto END

echo ──────────────────────────────────────────────────────────
:: Step 50: Delete AutoRun key
set "CURRENT_STEP=Deleting previous AutoRun key"
powershell -Command "Write-Host '[5/6] %CURRENT_STEP%' -ForegroundColor Yellow"
reg delete "HKCU\Software\Microsoft\Command Processor" /v AutoRun /f >nul 2>&1

echo ──────────────────────────────────────────────────────────
:: Step 60: Register pk_alias to AutoRun
set "CURRENT_STEP=Registering pk_alias to AutoRun"
powershell -Command "Write-Host '[6/6] %CURRENT_STEP%' -ForegroundColor Cyan"
reg add "HKCU\Software\Microsoft\Command Processor" /v AutoRun /t REG_SZ /d "\"%D_PKG_WINDOWS%\pk_alias.cmd\"" /f
echo ──────────────────────────────────────────────────────────
:: ✅ Completed
set "CURRENT_STEP=All steps completed successfully"
powershell -Command "Write-Host '✅ %CURRENT_STEP%' -ForegroundColor Green"


:END
pause
exit /b 0
