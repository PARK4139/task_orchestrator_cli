@echo off
chcp 65001 >nul


@echo off
setlocal enabledelayedexpansion

:: 프로젝트 디렉토리 경로 설정
set "PK_PROJECT_DIR=%USERPROFILE%\Downloads\pk_system"

:: 삭제 여부 확인
echo [INFO] 삭제할 디렉토리: "%PK_PROJECT_DIR%"
echo.
set /p USER_CONFIRM=정말로 해당 디렉토리를 삭제하시겠습니까? (Y/N): 
if /i not "!USER_CONFIRM!"=="Y" (
    echo [CANCELLED] 삭제 작업이 취소되었습니다.
    goto :EOF
)

:: 디렉토리 존재 확인 및 삭제
if exist "%PK_PROJECT_DIR%" (
    echo [INFO] 디렉토리 삭제 중...
    rmdir /s /q "%PK_PROJECT_DIR%"
    if exist "%PK_PROJECT_DIR%" (
        echo [ERROR] 디렉토리 삭제에 실패했습니다: "%PK_PROJECT_DIR%"
    ) else (
        echo [SUCCESS] 디렉토리가 성공적으로 삭제되었습니다.
    )
) else (
    echo [INFO] 디렉토리가 존재하지 않습니다: "%PK_PROJECT_DIR%"
)

endlocal
pause
