@REM @echo off >nul 2>&1
@REM set "LOCAL_TEST_ACTIVATE=1"
@REM set "F_CD_TXT=%USERPROFILE%\Downloads\pk_system\pkg_txt\pk_cd.txt"
@REM set "STAMP_DEBUG=[BATCH DEBUG]"
@REM python "%USERPROFILE%\Downloads\pk_system\pkg_py\pk_cli.py" %*
@REM
@REM if not exist "%F_CD_TXT%" (
@REM     if "%LOCAL_TEST_ACTIVATE%"=="1" (
@REM         echo %STAMP_DEBUG% f=0 : "%F_CD_TXT%"
@REM
@REM     )
@REM     exit /b
@REM ) else (
@REM     if "%LOCAL_TEST_ACTIVATE%"=="1" (
@REM         echo %STAMP_DEBUG% f=1 : "%F_CD_TXT%"
@REM         for /f "usebackq delims=" %%A in ("%F_CD_TXT%") do (
@REM             echo %STAMP_DEBUG% %%A
@REM         )
@REM     )
@REM     for /f "usebackq delims=" %%A in ("%F_CD_TXT%") do (
@REM         set "cd_path=%%A"
@REM         goto :set_complete
@REM     )
@REM )
@REM :set_complete
@REM if "%cd_path%"=="" (
@REM     if "%LOCAL_TEST_ACTIVATE%"=="1" (
@REM         echo %STAMP_DEBUG% 디렉터리 이동 실패: 경로 없음
@REM     )
@REM ) else (
@REM     if "%LOCAL_TEST_ACTIVATE%"=="1" (
@REM         echo %STAMP_DEBUG% 이동할 디렉터리: "%cd_path%"
@REM     )
@REM     cd /d "%cd_path%"
@REM )
