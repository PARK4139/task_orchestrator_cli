@echo off
chcp 65001 >nul

curl -L -o "%F_UV_ZIP%" "%PK_URL%"
powershell -NoLogo -NoProfile -Command "Expand-Archive -Path '%F_UV_ZIP%' -DestinationPath '%D_PKG_EXE%' -Force"

if not exist "%F_UV_EXE%" (
    echo ❌ uv.exe not found at: %F_UV_EXE%
    exit /b 1
)

"%F_UV_EXE%" --version

for /f "tokens=2*" %%A in ('reg query "HKCU\Environment" /v Path 2^>nul') do set "OLD_PATH=%%B"

if not defined OLD_PATH (
    set "OLD_PATH="
)

echo %OLD_PATH% | find /I "%D_PKG_EXE%" >nul
if not errorlevel 1 (
    echo ⚠️ uv path already exists in PATH. Skipping.
    goto :done
)


@REM set PATH=%D_PKG_EXE%;%PATH%
setx PATH "%OLD_PATH%;%D_PKG_EXE%" >nul
echo ✅ PATH updated (applies to future sessions).

:done
echo ENSURE UV INSTALLED 

del /f %F_UV_ZIP%