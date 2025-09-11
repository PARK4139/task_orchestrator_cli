#!/bin/bash
# task_orchestrator_cli Aliases
# This file contains useful aliases for the task_orchestrator_cli

# task_orchestrator_cli root directory
export TASK_ORCHESTRATOR_CLI_ROOT="$(dirname "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")")"

# Python virtual environment aliases (Linux/WSL용)
if [ -f "$TASK_ORCHESTRATOR_CLI_ROOT/.venv_linux/bin/python" ]; then
    alias pk-python="$TASK_ORCHESTRATOR_CLI_ROOT/.venv_linux/bin/python"
    alias pk-pip="$TASK_ORCHESTRATOR_CLI_ROOT/.venv_linux/bin/pip"
fi

# task_orchestrator_cli navigation aliases
alias pk-cd="cd $TASK_ORCHESTRATOR_CLI_ROOT"
alias pk-py="cd $TASK_ORCHESTRATOR_CLI_ROOT/resources"
alias pk-sh="cd $TASK_ORCHESTRATOR_CLI_ROOT/system_resources"

# task_orchestrator_cli utility functions
pk_enable() {
    echo "🔧 task_orchestrator_cli 활성화 중..."
    cd "$TASK_ORCHESTRATOR_CLI_ROOT"
    ./system_resources/ensure_task_orchestrator_cli_enabled.sh
}

pk_sync() {
    echo "🔄 task_orchestrator_cli 동기화 중..."
    cd "$TASK_ORCHESTRATOR_CLI_ROOT"
    UV_PROJECT_ENVIRONMENT=.venv_linux uv sync --active
}

pk_test() {
    echo "🧪 task_orchestrator_cli 테스트 중..."
    cd "$TASK_ORCHESTRATOR_CLI_ROOT"
    if [ -f "tests/run_tests.py" ]; then
        pk-python tests/run_tests.py
    else
        echo "❌ 테스트 파일을 찾을 수 없습니다."
    fi
}

# Display task_orchestrator_cli info
pk_info() {
    echo "🐍 task_orchestrator_cli Information"
    echo "========================"
    echo "📁 Root: $TASK_ORCHESTRATOR_CLI_ROOT"
    echo "🐍 Python: $(which python3)"
    if [ -f "$TASK_ORCHESTRATOR_CLI_ROOT/.venv_linux/bin/python" ]; then
        echo "🔗 Virtual Env: $TASK_ORCHESTRATOR_CLI_ROOT/.venv_linux/bin/python"
    fi
    echo "📦 uv: $(which uv 2>/dev/null || echo 'Not installed')"
    echo "========================"
}

# Create aliases for the functions
alias pk-enable="pk_enable"
alias pk-sync="pk_sync"
alias pk-test="pk_test"
alias pk-info="pk_info"

echo "✅ task_orchestrator_cli aliases loaded"