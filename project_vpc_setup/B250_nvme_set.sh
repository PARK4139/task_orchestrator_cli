#!/bin/bash

# 색상 정의
GREEN=$(tput setaf 2)
RED=$(tput setaf 1)
RESET=$(tput sgr0)

# 실행할 스크립트 목록
SCRIPTS=(
    "30_pk_ensure_nvme_set_up_for_log.sh"
)

TOTAL=${#SCRIPTS[@]}
STEP=1

run_script_with_status() {
    local script="$1"

    echo "___________________________________________"
    if ./"$script"; then
        echo -e "[${STEP}/${TOTAL} STEP] ${GREEN}${script} SUCCESS${RESET}"
    else
        echo -e "[${STEP}/${TOTAL} STEP] ${RED}${script} FAIL${RESET}"
    fi

    STEP=$((STEP + 1))
}

# 실행 루프
for script in "${SCRIPTS[@]}"; do
    run_script_with_status "$script"
done