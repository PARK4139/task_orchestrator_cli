#!/bin/bash
export LANG="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"


### 결과 로깅 파일 생성 및 초기화
file_txt="$(basename "$0" .sh).txt"
touch "$file_txt"
> "$file_txt"


print_command_tried() {
    echo "[ATTEMPTED] $@" >> "$file_txt"
}

run() {
    eval "$@" >> "$file_txt" 2>&1
}

run_commands() {
    local section="$1"
    shift
    echo "_____________________________ $section __________________________" >> "$file_txt"
    for command in "$@"; do
        print_command_tried "$command"
        run "$command"
    done
}
# 현재디렉토리 위치 starting_directory 변수에 저장


#echo "영상처리제어기 타입 :"  >> "$file_txt"
#echo "XC 일련번호 :"  >> "$file_txt"
#echo "배포일자:"  >> "$file_txt"


run_commands "NVIDIA Serial Number" \
    "cat /sys/firmware/devicetree/base/serial-number && echo '' " \
    # "sudo i2cdump -f -y 2 0x50" \
    # "sudo lshw | grep serial" \
    # "jtop" \

run_commands "User Basic Information" \
    "whoami"\
    "users"\
    "hostname"\

run_commands "Power Mode (edit)" \
    'sudo nvpmodel -q | grep "Power Mode:"'  \

run_commands "Linux Version" \
    "cat /etc/os-release | grep VERSION="

run_commands "Linux Package Version" \
    "echo '(업데이트 예정)'" \
    # 'sudo apt list --installed'

run_commands "Jetpack Version" \
    "sudo apt show nvidia-jetpack | grep Version:"

run_commands "AI Framework Release Version" \
    "sudo find ~/works -type f -name 'remote_release*'"


run_commands "IP Information" \
    "ifconfig | awk '/^[a-zA-Z0-9]+:/ || /inet /'"
    # "curl ifconfig.me" \
    # "ifconfig"

run_commands "Network eth0 Connection Number" \
    "sudo nmcli d | grep eth0"

run_commands "Network Wired Connection 1" \
    "sudo nmcli connection show 'Wired connection 1' | grep ipv4.address" \
    "sudo nmcli connection show 'Wired connection 1' | grep ipv4.method" \
    "sudo nmcli connection show 'Wired connection 1' | grep ipv4.gateway" \
    "sudo nmcli connection show 'Wired connection 1' | grep ipv4.dns:"

run_commands "Network Wired Connection 2" \
    "sudo nmcli connection show 'Wired connection 2' | grep ipv4.address" \
    "sudo nmcli connection show 'Wired connection 2' | grep ipv4.method" \
    "sudo nmcli connection show 'Wired connection 2' | grep ipv4.gateway" \
    "sudo nmcli connection show 'Wired connection 2' | grep ipv4.dns:"

run_commands "Network Wired Connection 3" \
    "sudo nmcli connection show 'Wired connection 3' | grep ipv4.address" \
    "sudo nmcli connection show 'Wired connection 3' | grep ipv4.method" \
    "sudo nmcli connection show 'Wired connection 3' | grep ipv4.gateway" \
    "sudo nmcli connection show 'Wired connection 3' | grep ipv4.dns:"

run_commands "Network Wired Connection 4" \
    "sudo nmcli connection show 'Wired connection 4' | grep ipv4.address" \
    "sudo nmcli connection show 'Wired connection 4' | grep ipv4.method" \
    "sudo nmcli connection show 'Wired connection 4' | grep ipv4.gateway" \
    "sudo nmcli connection show 'Wired connection 4' | grep ipv4.dns:"

run_commands "Stack Size (Configured)" \
    "ulimit -s" \
    "awk '/# End of file/ {flag=1} flag' /etc/security/limits.conf" \
#    "awk '/^\[Time\]/ {flag=1} /^\[/ && !/^\[Time\]/ {flag=0} flag' /etc/systemd/timesyncd.conf" \
#    "cat /etc/security/limits.conf" \

# STACK SIZE 상향설정 #MEMORY LEAK 예방  #10240로 합의됨


run_commands "Check NTP (Configured)" \
    "timedatectl | grep 'systemd'" \
    "timedatectl | grep 'System clock sync'" \
    "awk '/^\[Time\]/ {flag=1} /^\[/ && !/^\[Time\]/ {flag=0} flag' /etc/systemd/timesyncd.conf" \
#    "cat /etc/systemd/timesyncd.conf" \

# run_commands "장치 USB 연결 " \
#     "lsusb" \


run_commands "Check Camera Interface" \
    "ls /dev/v4l/by-id" \
    "ls /dev | grep video*"


run_commands "Check Camera Configuration File" \
    "sudo find ~/ -name '*cam*.cfg'" \
    "sudo find ~/ -name '*env*.cfg'" \
    "cat ~/works/remote_release/cam_merge_f.cfg | grep 'mode='" \
    "cat ~/works/remote_release/cam_merge_lf.cfg | grep 'mode='" \
    "cat ~/works/remote_release/cam_merge_lr.cfg | grep 'mode='" \
    "cat ~/works/remote_release/cam_merge_rf.cfg | grep 'mode='" \
    "cat ~/works/remote_release/cam_merge_rr.cfg | grep 'mode='" \
    "cat ~/works/remote_release/env_merge_flrrr.cfg | grep 'mode='" \
    "cat ~/works/remote_release/enc_merge_lrrr.cfg | grep 'mode='" \
    "cat ~/works/remote_release/env_merge_flrrr.cfg | grep 'show='" \
    "cat ~/works/remote_release/enc_merge_lrrr.cfg | grep 'show='" \


run_commands "Camera Configuration (AI Framework 2.x.x)" \
    "echo '(업데이트 예정)'"

run_commands "Camera Configuration (AI Framework 3.x.x)" \
    "echo '(업데이트 예정)'"

run_commands "Power" \
    "sudo cat /sys/bus/i2c/drivers/ina3221x/1-0040/iio:device0/in_power0_input"

run_commands "Current" \
    "sudo cat /sys/bus/i2c/drivers/ina3221x/1-0040/iio:device0/in_current0_input"

run_commands "Voltage" \
    "sudo cat /sys/bus/i2c/drivers/ina3221x/1-0040/iio:device0/in_voltage0_input"

run_commands "Fan" \
    "cat ~/autorun.sh | grep 'sudo jetson_clocks --fan'" \
    "cat /sys/devices/pwm-fan/target_pwm" \
    "cat ~/works/a2z_xavier_launcher/run.cfg | grep 'fan_speed='"

run_commands "CPU Frequency" \
    "cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq"
    ## XC 보드의 경우 2035200로 고정값 이면 OK
    ## XC 보드의 경우 MEMORY LEAK 예방차원에서 2035200로 합의

run_commands "Hibernate Mode Off (Requires Re-confirmation)" \
    "systemctl status sleep.target suspend.target hibernate.target hybrid-sleep.target | grep masked"
    # sleep 없으면 OK 재확인필요


# starting_directory 변수에 있는 디렉토리로 워킹디렉토리 이동


# 프로세서 정보
# ps -a
# PID 및 프로세스exec 경과시간
# ps -a | grep a2z_component_f
#XC 보드(전방)의 경우 autorun.sh 동작 중 나오면 OK
# ps -a | grep ??????
#XC 보드(후방)의 경우 autorun.sh 동작 중 나오면 OK
# top
# %CPU에 대한 상위권 PID, 프로세스exec 경과시간, 기타정보(PR/NI/VIRT/RES/SHR/%MEM)



#온도 정보
# tegrastats
# tegra : Nvidia tegra 칩
# stats : statistics 줄임말
# ENV보드의 경우 70ºC 까지는 OK



# 디버깅용, 스크립트가 끝난 후 터미널 유지
# exec bash
# clear

cat "$file_txt"


# 로그 필요 시, 주석처리
#rm "$file_txt"


#python3 -m http.server 9090