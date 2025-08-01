#!/bin/bash
set -e  # 에러 발생 시 즉시 종료

echo -e "\e[36m🐍 Python Virtual Environment Setup\e[0m"
echo "=================================================="

# 프로젝트 루트 디렉토리 설정
PROJECT_ROOT="/home/pk/Downloads/pk_system"
VENV_PATH="$PROJECT_ROOT/.venv"

echo "📁 Project root: $PROJECT_ROOT"
echo "📁 Virtual environment path: $VENV_PATH"

# .venv 디렉토리가 존재하는지 확인
if [ -d "$VENV_PATH" ]; then
    echo "✅ Virtual environment found at: $VENV_PATH"
    
    # Python 경로 설정
    VENV_PYTHON="$VENV_PATH/bin/python"
    VENV_PIP="$VENV_PATH/bin/pip"
    
    # Python 심볼릭 링크 생성 (전역에서 사용할 수 있도록)
    if [ -f "$VENV_PYTHON" ]; then
        echo "🔗 Creating Python symlink for virtual environment..."
        
        # 기존 심볼릭 링크 제거 (존재하는 경우)
        if [ -L "/usr/local/bin/python-venv" ]; then
            sudo rm -f /usr/local/bin/python-venv
        fi
        
        # 새로운 심볼릭 링크 생성
        sudo ln -sf "$VENV_PYTHON" /usr/local/bin/python-venv
        
        # pip 심볼릭 링크도 생성
        if [ -f "$VENV_PIP" ]; then
            if [ -L "/usr/local/bin/pip-venv" ]; then
                sudo rm -f /usr/local/bin/pip-venv
            fi
            sudo ln -sf "$VENV_PIP" /usr/local/bin/pip-venv
        fi
        
        echo "✅ Python virtual environment symlinks created:"
        echo "  - python-venv -> $VENV_PYTHON"
        echo "  - pip-venv -> $VENV_PIP"
        
        # 환경 변수 설정을 .bashrc에 추가
        if ! grep -Fxq "# Python virtual environment setup" "$HOME/.bashrc"; then
            echo "" >> "$HOME/.bashrc"
            echo "# Python virtual environment setup" >> "$HOME/.bashrc"
            echo "export VENV_PYTHON=\"$VENV_PYTHON\"" >> "$HOME/.bashrc"
            echo "export VENV_PIP=\"$VENV_PIP\"" >> "$HOME/.bashrc"
            echo "alias python-venv=\"$VENV_PYTHON\"" >> "$HOME/.bashrc"
            echo "alias pip-venv=\"$VENV_PIP\"" >> "$HOME/.bashrc"
        fi
        
        # 현재 세션에서도 환경 변수 설정
        export VENV_PYTHON="$VENV_PYTHON"
        export VENV_PIP="$VENV_PIP"
        alias python-venv="$VENV_PYTHON"
        alias pip-venv="$VENV_PIP"
        
        echo "✅ Python virtual environment aliases configured"
        echo "  - Use 'python-venv' to run Python from virtual environment"
        echo "  - Use 'pip-venv' to run pip from virtual environment"
        
        # Python 버전 확인
        echo "📋 Python version in virtual environment:"
        "$VENV_PYTHON" --version
        
    else
        echo "❌ Python executable not found in virtual environment: $VENV_PYTHON"
    fi
else
    echo "❌ Virtual environment not found at: $VENV_PATH"
    echo "💡 To create virtual environment, run:"
    echo "   cd $PROJECT_ROOT && python -m venv .venv"
fi

echo "=================================================="
echo "✅ Python virtual environment setup completed!" 