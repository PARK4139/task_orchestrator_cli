#!/bin/sh

# PYTHON INTERPRETER ALTERNATIVE
PYTHON_CANDIDATES="python3 python py"
PYTHON_EXEC=""

# 실행기 탐색
for candidate in $PYTHON_CANDIDATES; do
    if command -v $candidate >/dev/null 2>&1; then
        PYTHON_EXEC=$candidate
        break
    fi
done

if [ -z "$PYTHON_EXEC" ]; then
    echo "❌ Python 실행기를 찾을 수 없습니다 (python3, python, py)."
    echo "   https://www.python.org/downloads 에서 설치하세요."
    exit 1
fi

echo "✅ SELECTED PYTHON INTERPRETER: $PYTHON_EXEC"
echo "==============================="

# pytest 설치 여부 확인
$PYTHON_EXEC -m pytest --version >/dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "⚠️ pytest가 설치되어 있지 않습니다. 다음 명령어로 설치하세요:"
    echo "   $PYTHON_EXEC -m pip install pytest"
    exit 1
fi

# 테스트 실행
$PYTHON_EXEC pk_test_tests.py
