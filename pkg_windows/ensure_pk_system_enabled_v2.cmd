    @echo off
    chcp 65001 >nul
    setlocal enabledelayedexpansion

    :: steps numbers define
    set /a TOTAL_STEPS=5
    set /a STEP_INDEX=0

    :: path define
    set "D_PKG_WINDOWS=%USERPROFILE%\Downloads\pk_system\pkg_windows"
    set "VSCODE_PATH=%USERPROFILE%\AppData\Local\Programs\Microsoft VS Code\bin"

    echo ──────────────────────────────────────────────────────────
    :: Start message
    powershell -Command "Write-Host 'ensure_pk_enabled.cmd started' -ForegroundColor Cyan"

    echo ──────────────────────────────────────────────────────────
    :: Step 1: Import pk_alias
    set /a STEP_INDEX+=1
    set "CURRENT_STEP=Importing pk_alias"
    powershell -Command "Write-Host '[!STEP_INDEX!/!TOTAL_STEPS!] !CURRENT_STEP!' -ForegroundColor Cyan"
    call "%D_PKG_WINDOWS%\ensure_pk_alias_enabled.cmd" || goto END

    echo ──────────────────────────────────────────────────────────
    :: Step 2: Installing uv
    set /a STEP_INDEX+=1
    set "CURRENT_STEP=Installing uv"
    powershell -Command "Write-Host '[!STEP_INDEX!/!TOTAL_STEPS!] !CURRENT_STEP!' -ForegroundColor Cyan"
    call "%D_PKG_WINDOWS%\ensure_uv_enabled.cmd" || goto END

    echo ──────────────────────────────────────────────────────────
    :: Step 3: Syncing uv
    set /a STEP_INDEX+=1
    set "CURRENT_STEP=Syncing uv packages"
    powershell -Command "Write-Host '[!STEP_INDEX!/!TOTAL_STEPS!] !CURRENT_STEP!' -ForegroundColor Cyan"
    set "UV_PATH=%USERPROFILE%\Downloads\pk_system\pkg_exe"
    set "PATH=%PATH%;%UV_PATH%"
    call "%D_PKG_WINDOWS%\ensure_uv_synced.cmd" || goto END

    echo ──────────────────────────────────────────────────────────
    :: Step 4: Delete AutoRun key
    set /a STEP_INDEX+=1
    set "CURRENT_STEP=Deleting previous AutoRun key"
    powershell -Command "Write-Host '[!STEP_INDEX!/!TOTAL_STEPS!] !CURRENT_STEP!' -ForegroundColor Yellow"
    reg delete "HKCU\Software\Microsoft\Command Processor" /v AutoRun /f >nul 2>&1

    echo ──────────────────────────────────────────────────────────
    :: Step 5: Register pk_alias to AutoRun
    set /a STEP_INDEX+=1
    set "CURRENT_STEP=Registering pk_alias to AutoRun"
    powershell -Command "Write-Host '[!STEP_INDEX!/!TOTAL_STEPS!] !CURRENT_STEP!' -ForegroundColor Cyan"
    reg add "HKCU\Software\Microsoft\Command Processor" /v AutoRun /t REG_SZ /d "\"%D_PKG_WINDOWS%\pk_alias.cmd\"" /f

    echo ──────────────────────────────────────────────────────────
    :: All Complete
    set "CURRENT_STEP=All steps completed successfully"
    powershell -Command "Write-Host '✅ !CURRENT_STEP!' -ForegroundColor Green"

    :END
    pause
    exit /b 0
