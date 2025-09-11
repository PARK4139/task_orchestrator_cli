#!/bin/bash
set -e

echo "🔄 uv 패키지 동기화 중..."

# 프로젝트 루트로 이동
cd "$(dirname "$(dirname "$0")")"

# Add uv to PATH if not already there (check both possible locations)
export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"

# Check if uv is available
if command -v uv &> /dev/null; then
    echo "📦 uv sync --active 실행 중 (Linux/WSL용 .venv_linux virtual environment )..."
    UV_PROJECT_ENVIRONMENT=.venv_linux uv sync --active
    echo "✅ uv sync --active 완료"
else
    echo "❌ uv가 설치되지 않았습니다."
    echo "💡 uv를 먼저 설치하세요:"
    echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo "   source ~/.bashrc"
    exit 1
fi 