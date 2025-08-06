"""
SSH 키 확인 및 생성 테스트
"""
import os
import subprocess
import sys
from pathlib import Path

# 프로젝트 루트 경로 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def test_ssh_key_check():
    print("SSH 키 확인 및 생성 테스트")
    print("=" * 40)
    
    ssh_key_path = os.path.expanduser('~/.ssh/id_ed25519')
    
    # 1. SSH 키 존재 확인
    print("1️⃣ SSH 키 존재 확인...")
    if os.path.exists(ssh_key_path):
        print(f"✅ SSH 키 존재: {ssh_key_path}")
    else:
        print(f"❌ SSH 키 없음: {ssh_key_path}")
        print("SSH 키를 생성합니다...")
        
        # SSH 키 생성
        try:
            result = subprocess.run(
                ['ssh-keygen', '-t', 'ed25519', '-b', '4096', '-C', 'pk_ssh_key', '-f', ssh_key_path, '-N', ''],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                print("✅ SSH 키 생성 완료")
            else:
                print(f"❌ SSH 키 생성 실패: {result.stderr}")
                return False
        except Exception as e:
            print(f"❌ SSH 키 생성 중 오류: {str(e)}")
            return False
    
    # 2. SSH 키를 WSL에 복사
    print("\n2️⃣ SSH 키를 WSL에 복사...")
    try:
        # WSL에 .ssh 디렉토리 생성
        subprocess.run(['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', 'mkdir -p ~/.ssh'], check=True)
        
        # SSH 키를 WSL에 복사
        subprocess.run(['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', f'cp /mnt/c/Users/{os.getenv("USERNAME")}/.ssh/id_ed25519 ~/.ssh/'], check=True)
        subprocess.run(['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', f'cp /mnt/c/Users/{os.getenv("USERNAME")}/.ssh/id_ed25519.pub ~/.ssh/'], check=True)
        
        # 권한 설정
        subprocess.run(['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', 'chmod 600 ~/.ssh/id_ed25519'], check=True)
        subprocess.run(['wsl', '-d', 'Ubuntu', '-e', 'bash', '-c', 'chmod 644 ~/.ssh/id_ed25519.pub'], check=True)
        
        print("✅ SSH 키 WSL 복사 완료")
        return True
        
    except Exception as e:
        print(f"❌ SSH 키 WSL 복사 실패: {str(e)}")
        return False


if __name__ == "__main__":
    test_ssh_key_check() 