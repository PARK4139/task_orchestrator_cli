"""
WSL 내부에서 직접 Docker 설치하는 함수
"""
import subprocess
import platform
from pkg_py.functions_split.ensure_printed import ensure_printed


def ensure_docker_installed_in_wsl_direct():
    """WSL 내부에서 직접 Docker를 설치하는 함수"""
    try:
        # Windows 환경 확인
        if platform.system() != "Windows":
            ensure_printed(" 이 함수는 Windows 환경에서만 실행 가능합니다.")
            return False
        
        ensure_printed(" Windows 환경 감지됨")
        ensure_printed(" WSL 환경에서 Docker 설치를 시작합니다.")
        ensure_printed("=" * 50)
        
        # 1. 시스템 업데이트
        ensure_printed("1️⃣ 시스템 업데이트 중...")
        result = subprocess.run(
            ['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', 'sudo apt-get update -y'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=300
        )
        
        if result.returncode != 0:
            ensure_printed(f" 시스템 업데이트 실패: {result.stderr}")
            return False
        
        ensure_printed(" 시스템 업데이트 완료")
        
        # 2. Docker 설치
        ensure_printed("2️⃣ Docker 설치 중...")
        docker_install_script = '''
        sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
        echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
        sudo apt-get update -y
        sudo apt-get install -y docker-ce docker-ce-cli containerd.io
        '''
        
        result = subprocess.run(
            ['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', docker_install_script],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=900
        )
        
        if result.returncode != 0:
            ensure_printed(f" Docker 설치 실패: {result.stderr}")
            return False
        
        ensure_printed(" Docker 설치 완료")
        
        # 3. Docker 서비스 시작
        ensure_printed("3️⃣ Docker 서비스 시작 중...")
        result = subprocess.run(
            ['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', 'sudo systemctl start docker && sudo systemctl enable docker'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=60
        )
        
        # 4. 현재 사용자를 docker 그룹에 추가
        ensure_printed("4️⃣ 현재 사용자를 docker 그룹에 추가 중...")
        result = subprocess.run(
            ['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', 'sudo usermod -aG docker $USER'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=30
        )
        
        # 5. Docker 버전 확인
        ensure_printed("5️⃣ Docker 버전 확인 중...")
        result = subprocess.run(
            ['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', 'docker --version'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=30
        )
        
        if result.returncode == 0:
            ensure_printed(f" Docker 설치 확인: {result.stdout.strip()}")
            return True
        else:
            ensure_printed(f" Docker 버전 확인 실패: {result.stderr}")
            return False
            
    except Exception as e:
        ensure_printed(f" Docker 설치 중 오류 발생: {str(e)}")
        return False 