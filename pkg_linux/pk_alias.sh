#!/bin/bash
# PK System Aliases
# This file contains useful aliases for the PK system

# PK System root directory
export PK_SYSTEM_ROOT="$(dirname "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")")"

# Python virtual environment aliases
if [ -f "$PK_SYSTEM_ROOT/.venv/bin/python" ]; then
    alias pk-python="$PK_SYSTEM_ROOT/.venv/bin/python"
    alias pk-pip="$PK_SYSTEM_ROOT/.venv/bin/pip"
fi

# PK System navigation aliases
alias pk-cd="cd $PK_SYSTEM_ROOT"
alias pk-py="cd $PK_SYSTEM_ROOT/pkg_py"
alias pk-sh="cd $PK_SYSTEM_ROOT/pkg_linux"
alias pk-log="cd $PK_SYSTEM_ROOT/pkg_log"

# PK System utility functions
pk_enable() {
    echo "🔧 PK System 활성화 중..."
    cd "$PK_SYSTEM_ROOT"
    ./pkg_linux/ensure_pk_system_enabled.sh
}

pk_sync() {
    echo "🔄 PK System 동기화 중..."
    cd "$PK_SYSTEM_ROOT"
    uv sync
}

pk_test() {
    echo "🧪 PK System 테스트 중..."
    cd "$PK_SYSTEM_ROOT"
    if [ -f "tests/run_tests.py" ]; then
        pk-python tests/run_tests.py
    else
        echo "❌ 테스트 파일을 찾을 수 없습니다."
    fi
}

# Display PK System info
pk_info() {
    echo "🐍 PK System Information"
    echo "========================"
    echo "📁 Root: $PK_SYSTEM_ROOT"
    echo "🐍 Python: $(which python3)"
    if [ -f "$PK_SYSTEM_ROOT/.venv/bin/python" ]; then
        echo "🔗 Virtual Env: $PK_SYSTEM_ROOT/.venv/bin/python"
    fi
    echo "📦 uv: $(which uv 2>/dev/null || echo 'Not installed')"
    echo "========================"
}

# Create aliases for the functions
alias pk-enable="pk_enable"
alias pk-sync="pk_sync"
alias pk-test="pk_test"
alias pk-info="pk_info"

echo "✅ PK System aliases loaded" 