#!/bin/bash

# 색상 정의
GREEN=$(tput setaf 2)
RED=$(tput setaf 1)
RESET=$(tput sgr0)

# 현재 스크립트 경로
SELF="$0"

# step_echo 호출 횟수 자동 계산
TOTAL=$(grep -c '^[[:space:]]*step_run' "$SELF")
TOTAL=$((TOTAL - 1))  # 자기 자신 포함된 줄 제외

STEP=1

# STEP 출력 및 명령 실행 함수
step_run() {
    local msg="$1"
    shift
    local cmd="$@"

    echo "___________________________________________"
    if eval "$cmd"; then
        echo -e "[${STEP}/${TOTAL} STEP] ${msg} ${GREEN}SUCCESS${RESET}"
    else
        echo -e "[${STEP}/${TOTAL} STEP] ${msg} ${RED}FAIL${RESET}"
    fi
    STEP=$((STEP + 1))
}

# ----------------------------------------
# 사용 예: step_run "설명" 명령어

# step_run "rm -rf /home/nvidia/Data/nvme" rm -rf /home/nvidia/Data/nvme

step_run "/home/nvidia/Data/nvme 생성" mkdir -p /home/nvidia/Data/nvme

step_run "/etc/fstab edit 라인 추가" "echo '/dev/nvme0n1 /home/nvidia/Data/nvme ext4 errors=remount-ro 0 1' | sudo tee -a /etc/fstab"

step_run "/etc/fstab vi 편집" sudo vi /etc/fstab

step_run "mount -a 실행" sudo mount -a

step_run "chown nvidia:nvidia /home/nvidia/Data/nvme" sudo chown nvidia:nvidia /home/nvidia/Data/nvme

# step_run "ls -l /home/nvidia/Data/nvme" ls -l /home/nvidia/Data/nvme

step_run "sudo fdisk -l" sudo fdisk -l

step_run "lsblk" lsblk

step_run "df -hT" df -hT

step_run "gnome-disks 실행" sudo gnome-disks

step_run "최종 확인: ls -l /home/nvidia/Data/nvme" ls -l /home/nvidia/Data/nvme
