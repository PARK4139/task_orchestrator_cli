sudo nmcli connection down "Wired connection 1"

# sudo nmcli connection delete "Wired connection mkr"

sudo nmcli connection modify "Wired connection 1" ipv4.address ""
sudo nmcli connection modify "Wired connection 1" ipv4.method auto
sudo nmcli connection modify "Wired connection 1" ipv4.gateway ''
sudo nmcli connection modify "Wired connection 1" ipv4.dns ''

# sudo nmcli connection show 'Wired connection mkr' | grep ipv4.address
# sudo nmcli connection show 'Wired connection mkr' | grep ipv4.method
# sudo nmcli connection show 'Wired connection mkr' | grep ipv4.gateway
# sudo nmcli connection show 'Wired connection mkr' | grep ipv4.dns

# sudo nmcli connection up "Wired connection 1"


#!/bin/bash

# 연결 이름 입력 받기
# read -p "자동 IP 설정을 복원할 연결 이름을 입력하세요 (예: Wired connection 1): " AUTO_CONN
# read -p "삭제할 연결 프로필 이름을 입력하세요 (예: Wired connection mkr): " DELETE_CONN

# 연결 종료
# echo "[*] 연결 종료: $AUTO_CONN"
sudo nmcli connection down "eth0"
sudo nmcli connection down "eth1"
sudo nmcli connection up "eth0"
sudo nmcli connection up "eth1"


# 연결 프로필 삭제
# echo "[*] 연결 프로필 삭제: $DELETE_CONN"
# sudo nmcli connection delete "$DELETE_CONN"

# 자동 IP 설정으로 복원
# echo "[*] $AUTO_CONN 프로필을 자동 IP 설정으로 복원 중..."
# sudo nmcli connection modify "$AUTO_CONN" ipv4.address ""
# sudo nmcli connection modify "$AUTO_CONN" ipv4.method auto
# sudo nmcli connection modify "$AUTO_CONN" ipv4.gateway ''
# sudo nmcli connection modify "$AUTO_CONN" ipv4.dns ''

# 설정 확인
# echo -e "\n--- 적용된 설정 확인 ---"
 #sudo nmcli connection show "$AUTO_CONN" | grep ipv4.address
# sudo nmcli connection show "$AUTO_CONN" | grep ipv4.method
# sudo nmcli connection show "$AUTO_CONN" | grep ipv4.gateway
# sudo nmcli connection show "$AUTO_CONN" | grep ipv4.dns

# 연결 다시 활성화
# echo "[*] 연결 활성화: $AUTO_CONN"
# sudo nmcli connection up "$AUTO_CONN"
