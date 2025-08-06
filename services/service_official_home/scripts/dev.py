#!/usr/bin/env python3
"""
현사AI 공식 홈페이지 개발 서버 실행 스크립트

사용법:
    python scripts/dev.py                # 백엔드 + 프론트엔드 모두 실행
    python scripts/dev.py --backend     # 백엔드만 실행
    python scripts/dev.py --frontend    # 프론트엔드만 실행
"""

import subprocess
import sys
import os
import signal
import time
import argparse
from pathlib import Path

# 프로젝트 루트 디렉토리
PROJECT_ROOT = Path(__file__).parent.parent.absolute()

class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}{Colors.END}\n")

def print_success(text):
    print(f"{Colors.GREEN}✅ {text}{Colors.END}")

def print_error(text):
    print(f"{Colors.RED}❌ {text}{Colors.END}")

def print_info(text):
    print(f"{Colors.YELLOW}ℹ️  {text}{Colors.END}")

def run_backend():
    """백엔드 서버 실행"""
    print_header("현사AI 공식 홈페이지 백엔드 서버 시작")
    
    backend_dir = PROJECT_ROOT / "backend"
    os.chdir(backend_dir)
    
    # 의존성 확인
    if not (backend_dir / "requirements.txt").exists():
        print_error("requirements.txt 파일이 없습니다!")
        return None
    
    print_info("백엔드 서버를 시작합니다... (포트: 8030)")
    
    try:
        process = subprocess.Popen([
            sys.executable, "-m", "uvicorn", 
            "main:app", 
            "--host", "0.0.0.0", 
            "--port", "8030", 
            "--reload"
        ], cwd=backend_dir)
        
        print_success("백엔드 서버가 시작되었습니다!")
        print_info("🌐 백엔드 API: http://localhost:8030")
        print_info("📚 API 문서: http://localhost:8030/docs")
        
        return process
        
    except Exception as e:
        print_error(f"백엔드 서버 시작 실패: {e}")
        return None

def run_frontend():
    """프론트엔드 개발 서버 실행"""
    print_header("현사AI 공식 홈페이지 프론트엔드 서버 시작")
    
    frontend_dir = PROJECT_ROOT / "frontend"
    os.chdir(frontend_dir)
    
    # package.json 확인
    if not (frontend_dir / "package.json").exists():
        print_error("package.json 파일이 없습니다!")
        return None
    
    # node_modules 확인
    if not (frontend_dir / "node_modules").exists():
        print_info("의존성을 설치합니다...")
        try:
            subprocess.run(["npm", "install"], check=True, cwd=frontend_dir)
            print_success("의존성 설치 완료!")
        except subprocess.CalledProcessError:
            print_error("의존성 설치 실패!")
            return None
    
    print_info("프론트엔드 서버를 시작합니다... (포트: 3000)")
    
    try:
        # 환경 변수 설정
        env = os.environ.copy()
        env['NEXT_PUBLIC_API_URL'] = 'http://localhost:8030'
        env['NEXT_PUBLIC_APP_URL'] = 'http://localhost:8000'
        
        process = subprocess.Popen([
            "npm", "run", "dev"
        ], cwd=frontend_dir, env=env)
        
        print_success("프론트엔드 서버가 시작되었습니다!")
        print_info("🌐 홈페이지: http://localhost:3000")
        
        return process
        
    except Exception as e:
        print_error(f"프론트엔드 서버 시작 실패: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='현사AI 공식 홈페이지 개발 서버')
    parser.add_argument('--backend', action='store_true', help='백엔드만 실행')
    parser.add_argument('--frontend', action='store_true', help='프론트엔드만 실행')
    
    args = parser.parse_args()
    
    processes = []
    
    try:
        if args.backend:
            # 백엔드만 실행
            backend_process = run_backend()
            if backend_process:
                processes.append(backend_process)
                
        elif args.frontend:
            # 프론트엔드만 실행
            frontend_process = run_frontend()
            if frontend_process:
                processes.append(frontend_process)
                
        else:
            # 둘 다 실행
            backend_process = run_backend()
            if backend_process:
                processes.append(backend_process)
                time.sleep(3)  # 백엔드 시작 대기
            
            frontend_process = run_frontend()
            if frontend_process:
                processes.append(frontend_process)
        
        if not processes:
            print_error("서버를 시작할 수 없습니다!")
            return 1
        
        print_header("🚀 현사AI 공식 홈페이지 개발 환경 준비 완료!")
        print_info("종료하려면 Ctrl+C를 누르세요...")
        
        # 프로세스들이 종료될 때까지 대기
        for process in processes:
            process.wait()
            
    except KeyboardInterrupt:
        print_info("\n종료 신호를 받았습니다...")
        
        # 모든 프로세스 종료
        for process in processes:
            if process.poll() is None:  # 프로세스가 아직 실행 중이면
                process.terminate()
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    process.kill()
        
        print_success("모든 서버가 종료되었습니다.")
        return 0
    
    except Exception as e:
        print_error(f"예상치 못한 오류: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())