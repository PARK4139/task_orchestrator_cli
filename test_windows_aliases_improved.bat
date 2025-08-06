@echo off
echo ========================================
echo Windows PK System 별칭 테스트 (개선된 버전)
echo ========================================

echo.
echo 1. 현재 doskey 별칭 확인:
doskey /macros

echo.
echo 2. PK System 별칭 테스트:
echo - '0' 명령어 테스트 (pk_system으로 이동):
0
echo 현재 디렉토리: %CD%

echo.
echo 3. 'pk' 명령어 테스트:
pk

echo.
echo 4. 'venv' 명령어 테스트:
venv

echo.
echo 5. 'ls' 명령어 테스트 (dir 대신):
ls

echo.
echo 6. 'gpt' 명령어 테스트:
gpt

echo.
echo ========================================
echo 테스트 완료
echo.
echo 별칭이 제대로 작동하지 않으면 새 CMD 창을 열어서 테스트해보세요.
pause 