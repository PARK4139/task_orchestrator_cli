"""
간단한 WSL 확인 스크립트
"""
import subprocess
import sys


def test_wsl_simple():
    """간단한 WSL 확인 테스트"""
    print("🔍 WSL 상태 확인 중...")
    print("=" * 50)
    
    try:
        # 1. WSL 명령어 실행 가능 여부 확인
        print("1️⃣ WSL 명령어 실행 가능 여부 확인...")
        result = subprocess.run(['wsl', '--version'], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ WSL 설치됨: {result.stdout.strip()}")
        else:
            print(f"❌ WSL 설치되지 않음: {result.stderr}")
            return False
        
        # 2. 설치된 배포판 목록 확인
        print("\n2️⃣ 설치된 배포판 목록 확인...")
        result = subprocess.run(['wsl', '--list', '--verbose'], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✅ 설치된 배포판:")
            print(result.stdout)
        else:
            print(f"❌ 배포판 목록 조회 실패: {result.stderr}")
            return False
        
        # 3. Ubuntu-24.04 배포판 확인
        print("\n3️⃣ Ubuntu-24.04 배포판 확인...")
        result = subprocess.run(['wsl', '-d', 'Ubuntu-24.04', '-e', 'bash', '-c', 'pwd'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ Ubuntu-24.04 사용 가능: {result.stdout.strip()}")
        else:
            print(f"❌ Ubuntu-24.04 사용 불가: {result.stderr}")
            return False
        
        # 4. Docker 설치 확인
        print("\n4️⃣ Docker 설치 확인...")
        result = subprocess.run(['wsl', '-d', 'Ubuntu-24.04', '-e', 'bash', '-c', 'docker --version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ Docker 설치됨: {result.stdout.strip()}")
        else:
            print(f"❌ Docker 설치되지 않음: {result.stderr}")
            return False
        
        # 5. Docker Compose 설치 확인
        print("\n5️⃣ Docker Compose 설치 확인...")
        result = subprocess.run(['wsl', '-d', 'Ubuntu-24.04', '-e', 'bash', '-c', 'docker-compose --version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ Docker Compose 설치됨: {result.stdout.strip()}")
        else:
            print(f"❌ Docker Compose 설치되지 않음: {result.stderr}")
            return False
        
        print("\n" + "=" * 50)
        print("�� WSL 환경이 정상적으로 설정되어 있습니다!")
        return True
        
    except subprocess.TimeoutExpired:
        print("❌ 명령어 실행 시간 초과")
        return False
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        return False


if __name__ == "__main__":
    success = test_wsl_simple()
    if success:
        print("\n✅ WSL 테스트 성공!")
        sys.exit(0)
    else:
        print("\n❌ WSL 테스트 실패!")
        sys.exit(1) 