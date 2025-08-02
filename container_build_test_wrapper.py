#!/usr/bin/env python3
"""
컨테이너 빌드 테스트를 위한 wrapper
"""

import os
import sys
from pathlib import Path

from pkg_py.system_object.directories_reuseable import D_PROJECT

# 프로젝트 루트 디렉토리 설정


# pkg_py 디렉토리를 Python 경로에 추가
pkg_py_path = os.path.join(D_PROJECT, "pkg_py")
if pkg_py_path not in sys.path:
    sys.path.insert(0, pkg_py_path)

# 함수 import
from functions_split.ensure_container_build_test import (
    ensure_container_build_test,
    ensure_container_status_check
)


def main():
    """
    컨테이너 빌드 테스트를 실행하는 메인 함수
    """
    print("🐳 컨테이너 빌드 테스트를 시작합니다...")
    print(f"📁 프로젝트 경로: {D_PROJECT}")
    print("=" * 50)
    
    # fin_service 프로젝트 경로
    fin_service_path = os.path.join(D_PROJECT, "pkg_finance_invest_assist")
    
    if not os.path.exists(fin_service_path):
        print(f"❌ fin_service 프로젝트를 찾을 수 없습니다: {fin_service_path}")
        return
    
    print(f"🔍 fin_service 프로젝트 확인: {fin_service_path}")
    
    # 컨테이너 빌드 테스트 실행
    result = ensure_container_build_test(
        project_path=fin_service_path,
        docker_compose_file="deployment/docker-compose.yml",
        service_name="api_gateway",
        build_only=False,
        verbose=True
    )
    
    print("=" * 50)
    
    if result["success"]:
        print("✅ 컨테이너 빌드 테스트가 성공적으로 완료되었습니다!")
        
        # 서비스 상태 확인
        print("\n📊 서비스 상태 확인 중...")
        status_result = ensure_container_status_check(
            project_path=fin_service_path,
            docker_compose_file="deployment/docker-compose.yml"
        )
        
        if status_result["success"]:
            print("📋 현재 서비스 상태:")
            print(status_result["services"])
        else:
            print("❌ 서비스 상태 확인 실패:")
            for error in status_result["errors"]:
                print(f"  - {error}")
    else:
        print("❌ 컨테이너 빌드 테스트가 실패했습니다.")
        print("\n📋 오류 상세:")
        for error in result["errors"]:
            print(f"  - {error}")
        
        print("\n📋 실행된 단계:")
        for step in result["steps"]:
            print(f"  ✓ {step}")
        
        if result["logs"]:
            print("\n📋 로그:")
            for log in result["logs"]:
                print(f"  {log}")


def run_build_only():
    """
    빌드만 실행하는 함수
    """
    print("🏗️ 컨테이너 빌드만 실행합니다...")
    
    fin_service_path = os.path.join(D_PROJECT, "pkg_finance_invest_assist")
    
    result = ensure_container_build_test(
        project_path=fin_service_path,
        docker_compose_file="deployment/docker-compose.yml",
        service_name="api_gateway",
        build_only=True,
        verbose=True
    )
    
    if result["success"]:
        print("✅ 빌드가 성공적으로 완료되었습니다!")
    else:
        print("❌ 빌드가 실패했습니다.")
        for error in result["errors"]:
            print(f"  - {error}")


def run_status_check():
    """
    서비스 상태만 확인하는 함수
    """
    print("📊 서비스 상태를 확인합니다...")
    
    fin_service_path = os.path.join(D_PROJECT, "pkg_finance_invest_assist")
    
    result = ensure_container_status_check(
        project_path=fin_service_path,
        docker_compose_file="deployment/docker-compose.yml"
    )
    
    if result["success"]:
        print("📋 현재 서비스 상태:")
        print(result["services"])
    else:
        print("❌ 상태 확인 실패:")
        for error in result["errors"]:
            print(f"  - {error}")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="컨테이너 빌드 테스트 실행")
    parser.add_argument(
        "--build-only",
        action="store_true",
        help="빌드만 실행하고 서비스는 시작하지 않음"
    )
    parser.add_argument(
        "--status",
        action="store_true",
        help="서비스 상태만 확인"
    )
    
    args = parser.parse_args()
    
    if args.status:
        run_status_check()
    elif args.build_only:
        run_build_only()
    else:
        main() 