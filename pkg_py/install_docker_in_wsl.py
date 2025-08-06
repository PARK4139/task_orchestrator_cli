"""
WSL Ubuntu에 Docker 설치 스크립트
"""
import subprocess
import sys
import os


def install_docker_in_wsl():
    """WSL Ubuntu에 Docker 설치"""
    print("�� WSL Ubuntu에 Docker 설치 중...")
    print("=" * 50)
    
    try:
        # 1. 시스템 업데이트
        print("1️⃣ 시스템 업데이트...")
        result = subprocess.run(
            ['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', 'sudo apt-get update'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=300
        )
        if result.returncode == 0:
            print("✅ 시스템 업데이트 완료")
        else:
            print(f"❌ 시스템 업데이트 실패: {result.stderr}")
            return False
        
        # 2. 필요한 패키지 설치
        print("\n2️⃣ 필요한 패키지 설치...")
        packages = [
            'apt-transport-https',
            'ca-certificates',
            'curl',
            'gnupg',
            'lsb-release'
        ]
        
        for package in packages:
            result = subprocess.run(
                ['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', f'sudo apt-get install -y {package}'],
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='ignore',
                timeout=300
            )
            if result.returncode == 0:
                print(f"✅ {package} 설치 완료")
            else:
                print(f"❌ {package} 설치 실패: {result.stderr}")
                return False
        
        # 3. Docker GPG 키 추가
        print("\n3️⃣ Docker GPG 키 추가...")
        result = subprocess.run(
            ['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', 
             'curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=300
        )
        if result.returncode == 0:
            print("✅ Docker GPG 키 추가 완료")
        else:
            print(f"❌ Docker GPG 키 추가 실패: {result.stderr}")
            return False
        
        # 4. Docker 저장소 추가
        print("\n4️⃣ Docker 저장소 추가...")
        result = subprocess.run(
            ['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', 
             'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=300
        )
        if result.returncode == 0:
            print("✅ Docker 저장소 추가 완료")
        else:
            print(f"❌ Docker 저장소 추가 실패: {result.stderr}")
            return False
        
        # 5. 패키지 목록 업데이트
        print("\n5️⃣ 패키지 목록 업데이트...")
        result = subprocess.run(
            ['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', 'sudo apt-get update'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=300
        )
        if result.returncode == 0:
            print("✅ 패키지 목록 업데이트 완료")
        else:
            print(f"❌ 패키지 목록 업데이트 실패: {result.stderr}")
            return False
        
        # 6. Docker 설치
        print("\n6️⃣ Docker 설치...")
        result = subprocess.run(
            ['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', 
             'sudo apt-get install -y docker-ce docker-ce-cli containerd.io'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=600
        )
        if result.returncode == 0:
            print("✅ Docker 설치 완료")
        else:
            print(f"❌ Docker 설치 실패: {result.stderr}")
            return False
        
        # 7. Docker Compose 설치
        print("\n7️⃣ Docker Compose 설치...")
        result = subprocess.run(
            ['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', 
             'sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=300
        )
        if result.returncode == 0:
            print("✅ Docker Compose 설치 완료")
        else:
            print(f"❌ Docker Compose 설치 실패: {result.stderr}")
            return False
        
        # 8. 현재 사용자를 docker 그룹에 추가
        print("\n8️⃣ 현재 사용자를 docker 그룹에 추가...")
        result = subprocess.run(
            ['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', 'sudo usermod -aG docker $USER'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=300
        )
        if result.returncode == 0:
            print("✅ 사용자를 docker 그룹에 추가 완료")
        else:
            print(f"❌ 사용자를 docker 그룹에 추가 실패: {result.stderr}")
            return False
        
        # 9. Docker 서비스 시작
        print("\n9️⃣ Docker 서비스 시작...")
        result = subprocess.run(
            ['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', 'sudo service docker start'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=300
        )
        if result.returncode == 0:
            print("✅ Docker 서비스 시작 완료")
        else:
            print(f"❌ Docker 서비스 시작 실패: {result.stderr}")
            return False
        
        # 10. 설치 확인
        print("\n�� 설치 확인...")
        result = subprocess.run(
            ['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', 'docker --version'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=10
        )
        if result.returncode == 0:
            print(f"✅ Docker 설치 확인: {result.stdout.strip()}")
        else:
            print(f"❌ Docker 설치 확인 실패: {result.stderr}")
            return False
        
        result = subprocess.run(
            ['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', 'docker-compose --version'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=10
        )
        if result.returncode == 0:
            print(f"✅ Docker Compose 설치 확인: {result.stdout.strip()}")
        else:
            print(f"❌ Docker Compose 설치 확인 실패: {result.stderr}")
            return False
        
        print("\n" + "=" * 50)
        print("✅ Docker 설치가 완료되었습니다!")
        print("⚠️  WSL을 재시작한 후 docker 명령어를 사용할 수 있습니다.")
        return True
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        return False


if __name__ == "__main__":
    success = install_docker_in_wsl()
    if success:
        print("\n✅ Docker 설치 성공!")
        sys.exit(0)
    else:
        print("\n❌ Docker 설치 실패!")
        sys.exit(1) 