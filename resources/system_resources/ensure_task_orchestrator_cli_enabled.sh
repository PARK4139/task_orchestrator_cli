#!/bin/bash
set -e  # 에러 발생 시 즉시 종료

# UTF-8 설정
export LANG=en_US.UTF-8

echo -e "\e[36m🐍 task_orchestrator_cli Enable Script (Linux/WSL)\e[0m"
echo "=================================================="

# 현재 스크립트 위치(절대경로)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo "📁 Script directory: $SCRIPT_DIR"
echo "📁 Project root: $PROJECT_ROOT"

# ➊ 프로젝트 루트를 PYTHONPATH 에 포함
export PYTHONPATH="$PROJECT_ROOT:${PYTHONPATH:-}"

# Python 찾기 함수
find_python() {
    echo "🔍 Python 찾는 중..."
    
    # n. 시스템 python 확인
    if command -v python3 &> /dev/null; then
        echo "✅ 시스템 Python 발견: python3"
        PYTHON_CMD="python3"
        return 0
    fi
    
    # n. python 명령어 확인
    if command -v python &> /dev/null; then
        echo "✅ 시스템 Python 발견: python"
        PYTHON_CMD="python"
        return 0
    fi
    
    # n. virtual environment python 확인 (Linux/WSL용)
    VENV_PYTHON="$PROJECT_ROOT/.venv_linux/bin/python"
    if [ -f "$VENV_PYTHON" ]; then
        echo "task_orchestrator_cli virtual environment python detected: $VENV_PYTHON"
        PYTHON_CMD="$VENV_PYTHON"
        return 0
    fi
    
    # n. system_resources 하위에서 python 찾기
    for python_file in "$PROJECT_ROOT/system_resources"/*/python*; do
        if [ -f "$python_file" ] && [ -x "$python_file" ]; then
            echo "✅ Python 발견: $python_file"
            PYTHON_CMD="$python_file"
            return 0
        fi
    done
    
    # n. 전체 프로젝트에서 python 찾기
    while IFS= read -r -d '' python_file; do
        if [ -f "$python_file" ] && [ -x "$python_file" ]; then
            echo "✅ Python 발견: $python_file"
            PYTHON_CMD="$python_file"
            return 0
        fi
    done < <(find "$PROJECT_ROOT" -name "python*" -type f -executable 2>/dev/null | head -1)
    
    # Python을 찾을 수 없는 경우
    echo "❌ Python을 찾을 수 없습니다."
    echo "📥 Python 설치를 시도합니다..."
    echo ""
    echo "다음 중 하나를 선택하세요:"
    echo "1. apt를 사용하여 Python 설치 (권장)"
    echo "2. python.org에서 수동 설치"
    echo "3. 취소"
    echo ""
    read -p "선택 (1-3): " choice
    
    case $choice in
        1)
            echo "🛒 apt를 사용하여 Python 설치 중..."
            sudo apt update
            sudo apt install -y python3 python3-pip python3-venv
            echo "✅ Python 설치 완료"
            PYTHON_CMD="python3"
            return 0
            ;;
        2)
            echo "🌐 python.org로 이동 중..."
            echo "https://www.python.org/downloads/"
            echo "설치 완료 후 이 스크립트를 다시 실행하세요."
            exit 1
            ;;
        3)
            echo "취소되었습니다."
            exit 1
            ;;
        *)
            echo "잘못된 선택입니다."
            exit 1
            ;;
    esac
}

# Python 찾기 실행
find_python

# Python 스크립트 실행 ---------------------------------------------------------
# 실행 대상 PY 스크립트 경로
PY_SCRIPT="$PROJECT_ROOT/resources/functions/ensure_task_orchestrator_cli_enabled.py"

echo "🚀 Python 스크립트 실행 중: $PYTHON_CMD $PY_SCRIPT"

# 스크립트 존재 여부 확인 후 실행
if [ -f "$PY_SCRIPT" ]; then
    "$PYTHON_CMD" "$PY_SCRIPT"
    EXIT_CODE=$?
    
    if [ $EXIT_CODE -eq 0 ]; then
        echo "✅ 스크립트 실행 완료"
    else
        echo "❌ 스크립트 실행 실패 (오류 코드: $EXIT_CODE)"
        exit $EXIT_CODE
    fi
else
    echo "❌ Python 스크립트를 찾을 수 없습니다: $PY_SCRIPT"
    exit 1
fi

echo "=================================================="
echo "✅ task_orchestrator_cli Enable Script 완료"
