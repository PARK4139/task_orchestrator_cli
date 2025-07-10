#!/bin/bash

# 색상 정의
GREEN=$(tput setaf 2)
RED=$(tput setaf 1)
RESET=$(tput sgr0)

# 실행할 스크립트 목록
SCRIPTS=(
    "25_ensure_jetson_setup_processed_after_reboot.sh"
    # "30_ensure_nvme_set_up_for_log.sh"
    "40_ensure_container_0_0_4_dev_for_no.sh"
    "50_ensure_jetson_stress_activate.sh"
    "60_remove_all_useless.sh"
    "65_ensure_ai_framework_container_ran.sh"
    "68_ensure_dashboard_ran.sh"
    "70_ensure_network_for_no.sh"
    "80_monitor.sh"
)

TOTAL=${#SCRIPTS[@]}
STEP=1

run_script_with_status() {
    local script="$1"

    # 줄 출력 후 개행
    echo "___________________________________________"

    # 결과 출력
    if ./"$script"; then
        echo -e "[${STEP}/${TOTAL} STEP] ${script}${GREEN} SUCCESS${RESET}"
    else
        echo -e "[${STEP}/${TOTAL} STEP] ${script}${RED} FAIL${RESET}"
    fi

    STEP=$((STEP + 1))
}

# 실행 루프
for script in "${SCRIPTS[@]}"; do
    run_script_with_status "$script"
done
