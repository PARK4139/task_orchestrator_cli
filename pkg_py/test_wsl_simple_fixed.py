"""
인코딩 문제를 해결한 WSL 확인 스크립트
"""
import subprocess
import sys
import os


def test_wsl_simple_fixed():
    """인코딩 문제를 해결한 WSL 확인 테스트"""
    print("🔍 WSL 상태 확인 중...")
    print("=" * 50)
    
    try:
        # 1. WSL 명령어 실행 가능 여부 확인
        print("1️⃣ WSL 명령어 실행 가능 여부 확인...")
        result = subprocess.run(
            ['wsl', '--version'], 
            capture_output=True, 
            text=True, 
            encoding='utf-8',
            errors='ignore',
            timeout=10
        )
        if result.returncode == 0:
            print(f"✅ WSL 설치됨: {result.stdout.strip()}")
        else:
            print(f"❌ WSL 설치되지 않음: {result.stderr}")
            return False
        
        # 2. 설치된 배포판 목록 확인
        print("\n2️⃣ 설치된 배포판 목록 확인...")
        result = subprocess.run(
            ['wsl', '--list', '--verbose'], 
            capture_output=True, 
            text=True, 
            encoding='utf-8',
            errors='ignore',
            timeout=10
        )
        if result.returncode == 0:
            print("✅ 설치된 배포판:")
            print(result.stdout)
        else:
            print(f"❌ 배포판 목록 조회 실패: {result.stderr}")
            return False
        
        # 3. 사용 가능한 배포판 찾기
        print("\n3️⃣ 사용 가능한 배포판 찾기...")
        available_distros = []
        if result.stdout:
            lines = result.stdout.strip().split('\n')
            for line in lines[1:]:  # 헤더 제외
                if line.strip():
                    parts = line.split()
                    if len(parts) >= 2:
                        distro_name = parts[0]
                        available_distros.append(distro_name)
        
        print(f"🔍 사용 가능한 배포판: {available_distros}")
        
        if not available_distros:
            print("❌ 사용 가능한 배포판이 없습니다.")
            return False
        
        # 4. Ubuntu 배포판 우선 시도
        preferred_distros = ["Ubuntu-24.04", "Ubuntu-22.04", "Ubuntu", "ubuntu-24.04", "ubuntu-22.04", "ubuntu"]
        selected_distro = None
        
        for distro in preferred_distros:
            if distro in available_distros:
                selected_distro = distro
                break
        
        if not selected_distro:
            selected_distro = available_distros[0]
        
        print(f"✅ 선택된 배포판: {selected_distro}")
        
        # 5. 선택된 배포판으로 테스트
        print(f"\n4️⃣ {selected_distro} 배포판 확인...")
        result = subprocess.run(
            ['wsl', '-d', selected_distro, '-e', 'bash', '-c', 'pwd'], 
            capture_output=True, 
            text=True, 
            encoding='utf-8',
            errors='ignore',
            timeout=10
        )
        if result.returncode == 0:
            print(f"✅ {selected_distro} 사용 가능: {result.stdout.strip()}")
        else:
            print(f"❌ {selected_distro} 사용 불가: {result.stderr}")
            return False
        
        # 6. Docker 설치 확인
        print(f"\n5️⃣ Docker 설치 확인 ({selected_distro})...")
        result = subprocess.run(
            ['wsl', '-d', selected_distro, '-e', 'bash', '-c', 'docker --version'], 
            capture_output=True, 
            text=True, 
            encoding='utf-8',
            errors='ignore',
            timeout=10
        )
        if result.returncode == 0:
            print(f"✅ Docker 설치됨: {result.stdout.strip()}")
        else:
            print(f"❌ Docker 설치되지 않음: {result.stderr}")
            return False
        
        # 7. Docker Compose 설치 확인
        print(f"\n6️⃣ Docker Compose 설치 확인 ({selected_distro})...")
        result = subprocess.run(
            ['wsl', '-d', selected_distro, '-e', 'bash', '-c', 'docker-compose --version'], 
            capture_output=True, 
            text=True, 
            encoding='utf-8',
            errors='ignore',
            timeout=10
        )
        if result.returncode == 0:
            print(f"✅ Docker Compose 설치됨: {result.stdout.strip()}")
        else:
            print(f"❌ Docker Compose 설치되지 않음: {result.stderr}")
            return False
        
        # 8. 프로젝트 디렉토리 접근 확인
        print(f"\n7️⃣ 프로젝트 디렉토리 접근 확인 ({selected_distro})...")
        user_path = os.path.expanduser("~")
        project_path = f"/mnt/c/Users/{os.path.basename(user_path)}/Downloads/pk_system/pkg_finance_invest_assist"
        
        result = subprocess.run(
            ['wsl', '-d', selected_distro, '-e', 'bash', '-c', f'cd {project_path} && pwd'], 
            capture_output=True, 
            text=True, 
            encoding='utf-8',
            errors='ignore',
            timeout=10
        )
        if result.returncode == 0:
            print(f"✅ 프로젝트 디렉토리 접근 가능: {result.stdout.strip()}")
        else:
            print(f"❌ 프로젝트 디렉토리 접근 실패: {result.stderr}")
            return False
        
        print("\n" + "=" * 50)
        print("�� WSL 환경이 정상적으로 설정되어 있습니다!")
        print(f"�� 선택된 배포판: {selected_distro}")
        return True
        
    except subprocess.TimeoutExpired:
        print("❌ 명령어 실행 시간 초과")
        return False
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        return False


if __name__ == "__main__":
    success = test_wsl_simple_fixed()
    if success:
        print("\n✅ WSL 테스트 성공!")
        sys.exit(0)
    else:
        print("\n❌ WSL 테스트 실패!")
        sys.exit(1) 