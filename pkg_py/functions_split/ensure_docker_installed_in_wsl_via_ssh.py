"""
SSH를 통해 WSL에 Docker 설치하는 함수
"""
import subprocess
import os
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.cmd_to_remote_os_with_pubkey import cmd_to_remote_os_with_pubkey
from pkg_py.functions_split.ensure_wsl_ip_detected import ensure_wsl_ip_detected


def ensure_docker_installed_in_wsl_via_ssh():
    """SSH를 통해 WSL에 Docker를 설치하는 함수"""
    try:
        # 1. WSL IP 주소 감지
        ensure_printed(" WSL IP 주소 감지 중...")
        wsl_ip = ensure_wsl_ip_detected()
        
        if not wsl_ip:
            ensure_printed(" WSL IP 주소를 찾을 수 없어 Docker 설치를 중단합니다.")
            return False
        
        # 2. SSH 설정
        config_remote_os = {
            'ip': wsl_ip,
            'port': 22,
            'user_n': 'ubuntu',  # WSL Ubuntu 사용자명
            'local_ssh_private_key': os.path.expanduser('~/.ssh/id_ed25519')
        }
        
        # 3. 시스템 업데이트
        ensure_printed("1️⃣ 시스템 업데이트 중...")
        std_out, std_err = cmd_to_remote_os_with_pubkey(
            "sudo apt-get update -y",
            **config_remote_os
        )
        
        if std_err and len(std_err) > 0:
            ensure_printed(f" 시스템 업데이트 실패: {std_err}")
            return False
        
        # 4. Docker 설치
        ensure_printed("2️⃣ Docker 설치 중...")
        docker_install_commands = [
            "sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release",
            "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg",
            "echo \"deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable\" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null",
            "sudo apt-get update -y",
            "sudo apt-get install -y docker-ce docker-ce-cli containerd.io"
        ]
        
        for cmd in docker_install_commands:
            ensure_printed(f"실행 중: {cmd}")
            std_out, std_err = cmd_to_remote_os_with_pubkey(cmd, **config_remote_os)
            
            if std_err and len(std_err) > 0:
                ensure_printed(f" Docker 설치 실패: {std_err}")
                return False
        
        # 5. Docker 서비스 시작
        ensure_printed("3️⃣ Docker 서비스 시작 중...")
        std_out, std_err = cmd_to_remote_os_with_pubkey(
            "sudo systemctl start docker && sudo systemctl enable docker",
            **config_remote_os
        )
        
        # 6. 현재 사용자를 docker 그룹에 추가
        ensure_printed("4️⃣ 현재 사용자를 docker 그룹에 추가 중...")
        std_out, std_err = cmd_to_remote_os_with_pubkey(
            "sudo usermod -aG docker $USER",
            **config_remote_os
        )
        
        # 7. Docker 설치 확인
        ensure_printed("5️⃣ Docker 설치 확인 중...")
        std_out, std_err = cmd_to_remote_os_with_pubkey(
            "docker --version",
            **config_remote_os
        )
        
        if std_out and len(std_out) > 0:
            ensure_printed(f" Docker 설치 완료: {std_out[0]}")
            return True
        else:
            ensure_printed(" Docker 설치 확인 실패")
            return False
            
    except Exception as e:
        ensure_printed(f" Docker 설치 중 오류 발생: {str(e)}")
        return False 