@echo off
echo ========================================
echo CMD에서 별칭 등록
echo ========================================

echo.
echo UTF-8 인코딩 설정...
chcp 65001 >nul

echo.
echo 별칭 등록 중...

set "PK_SYSTEM_PATH=C:\Users\wjdgn\Downloads\pk_system"

REM 기본 별칭들 등록
doskey 0=cd "%PK_SYSTEM_PATH%"
doskey 1=cd "%PK_SYSTEM_PATH%\pkg_py"
doskey 2=cd "%PK_SYSTEM_PATH%\pkg_windows"
doskey 3=cd "%USERPROFILE%\pk_working"
doskey 4=cd "%USERPROFILE%\pk_memo"
doskey 5=cd "%USERPROFILE%\business_demo"
doskey pk=python "%PK_SYSTEM_PATH%\pkg_py\pk_ensure_pk_system_enabled.py"
doskey venv="%PK_SYSTEM_PATH%\.venv\Scripts\activate"
doskey ls=dir
doskey cat=type
doskey which=where
doskey pwd=cd
doskey gpt=start https://chat.openai.com
doskey x=exit

echo.
echo 등록된 별칭 확인:
doskey /macros

echo.
echo ========================================
echo 별칭 등록 완료!
echo 이제 다음 명령어들을 사용할 수 있습니다:
echo   0 - pk_system으로 이동
echo   1 - pkg_py로 이동
echo   2 - pkg_windows로 이동
echo   3 - pk_working으로 이동
echo   4 - pk_memo로 이동
echo   5 - business_demo로 이동
echo   pk - PK System 재실행
echo   venv - 가상환경 활성화
echo   ls - dir 명령어
echo   gpt - ChatGPT 열기
echo ========================================

echo.
echo 테스트를 위해 다음 명령어를 입력하세요:
echo   0
pause 