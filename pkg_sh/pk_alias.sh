#!/bin/bash
# PK System Alias Script
# Linux/WSL 환경에서 PK 시스템의 유틸리티 함수들과 alias들을 제공

# PK System utility functions
pk_enable() {
    echo '🔧 PK System 활성화 중...'
    cd "$D_PK_PROJECT"
    ./pkg_sh/ensure_pk_system_enabled.sh
}

pk_sync() {
    echo '🔄 PK System 동기화 중...'
    cd "$D_PK_PROJECT"
    uv sync
}

pk_test() {
    echo '🧪 PK System 테스트 중...'
    cd "$D_PK_PROJECT"
    if [ -f 'tests/run_tests.py' ]; then
        python-venv tests/run_tests.py
    else
        echo '❌ 테스트 파일을 찾을 수 없습니다.'
    fi
}

pk_info() {
    echo '🐍 PK System Information'
    echo '================'
    echo "📁 Root: $D_PK_PROJECT"
    echo "🐍 Python: $(which python3)"
    echo "📦 uv: $(which uv 2>/dev/null || echo 'Not installed')"
    echo "🔍 fzf: $(which fzf 2>/dev/null || echo 'Not installed')"
    echo '================'
}

# Create aliases for the functions
alias pk-enable="pk_enable"
alias pk-sync="pk_sync"
alias pk-test="pk_test"
alias pk-info="pk_info"

# Additional utility functions
pk_working() {
    echo '📁 PK Working 디렉토리로 이동...'
    cd "$D_PK_WORKING"
}

pk_business() {
    echo '💼 Business Demo 디렉토리로 이동...'
    cd "$D_BUSINESS_DEMO"
}

# Export functions for use in other scripts
export -f pk_enable pk_sync pk_test pk_info pk_working pk_business 