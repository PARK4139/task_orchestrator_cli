#!/usr/bin/env python3
"""
Smart Person AI 서비스 시작 스크립트

개발 환경에서 모든 마이크로서비스를 순차적으로 시작하는 스크립트
"""

import subprocess
import time
import signal
import sys
import os
from pathlib import Path

# 서비스 설정
SERVICES = [
    {
        "name": "API Gateway",
        "port": 8000,
        "command": ["python", "service_api_gateway/main.py"],
        "health_check": "http://localhost:8000/health"
    },
    {
        "name": "AI Image Service", 
        "port": 8001,
        "command": ["python", "service_ai_content_image/main.py"],
        "health_check": "http://localhost:8001/health"
    },
    {
        "name": "AI Book Service", 
        "port": 8002,
        "command": ["python", "service_ai_content_book/main.py"],
        "health_check": "http://localhost:8002/health"
    },
    {
        "name": "Excel Automation Service",
        "port": 8011, 
        "command": ["python", "service_automation_excel_service/main.py"],
        "health_check": "http://localhost:8011/health"
    },
    {
        "name": "Web Crawler Service",
        "port": 8012, 
        "command": ["python", "service_automation_web_crawler/main.py"],
        "health_check": "http://localhost:8012/health"
    },
    {
        "name": "Payment Service",
        "port": 8021, 
        "command": ["python", "service_payment/main.py"],
        "health_check": "http://localhost:8021/health"
    }
]

# 실행 중인 프로세스들
processes = []

def signal_handler(sig, frame):
    """Ctrl+C 시 모든 프로세스 종료"""
    print("\n🛑 Shutting down all services...")
    
    for process in processes:
        if process.poll() is None:  # 프로세스가 아직 실행 중인 경우
            process.terminate()
            
    # 2초 대기 후 강제 종료
    time.sleep(2)
    for process in processes:
        if process.poll() is None:
            process.kill()
            
    print("✅ All services stopped")
    sys.exit(0)

def start_service(service_config):
    """개별 서비스 시작"""
    print(f"🚀 Starting {service_config['name']} on port {service_config['port']}...")
    
    try:
        process = subprocess.Popen(
            service_config['command'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        processes.append(process)
        
        # 잠시 대기 (서비스 시작 시간)
        time.sleep(3)
        
        if process.poll() is None:  # 프로세스가 아직 실행 중
            print(f"✅ {service_config['name']} started successfully")
            return True
        else:
            stdout, stderr = process.communicate()
            print(f"❌ {service_config['name']} failed to start")
            print(f"   Error: {stderr.decode('utf-8')}")
            return False
            
    except Exception as e:
        print(f"❌ Error starting {service_config['name']}: {e}")
        return False

def main():
    """메인 실행 함수"""
    
    # Ctrl+C 핸들러 등록
    signal.signal(signal.SIGINT, signal_handler)
    
    print("🏗️  Smart Person AI - Starting Development Environment")
    print("=" * 60)
    
    # 프로젝트 루트로 이동
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)
    
    print(f"📁 Working directory: {os.getcwd()}")
    print()
    
    # 필수 의존성 확인
    try:
        import fastapi
        import uvicorn
        print("✅ FastAPI dependencies found")
    except ImportError:
        print("❌ Missing dependencies. Please run: uv sync")
        return
    
    # 서비스들 순차 시작
    started_services = 0
    
    for service in SERVICES:
        if start_service(service):
            started_services += 1
        else:
            print(f"❌ Failed to start {service['name']}")
            break
    
    if started_services == len(SERVICES):
        print()
        print("🎉 All services started successfully!")
        print("=" * 60)
        print("📡 Service Endpoints:")
        for service in SERVICES:
            print(f"   • {service['name']}: http://localhost:{service['port']}")
        
        print()
        print("🔍 Health Check: http://localhost:8000/health") 
        print("📖 API Docs: http://localhost:8000/docs")
        print()
        print("Press Ctrl+C to stop all services")
        
        # 서비스들이 실행 중인 동안 대기
        try:
            while True:
                time.sleep(1)
                # 모든 프로세스가 아직 실행 중인지 확인
                running_count = sum(1 for p in processes if p.poll() is None)
                if running_count == 0:
                    print("❌ All services have stopped")
                    break
        except KeyboardInterrupt:
            pass
    else:
        print("❌ Some services failed to start. Shutting down...")
        signal_handler(None, None)

if __name__ == "__main__":
    main()