#!/usr/bin/env python3
"""
컨테이너 빌드 테스트를 재현하는 함수
"""

import subprocess
import os
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple


def ensure_container_build_test(
    project_path: str = None,
    docker_compose_file: str = "infra/docker-compose.yml",
    service_name: str = "gateway",
    build_only: bool = False,
    verbose: bool = True
) -> Dict[str, any]:
    """
    컨테이너 빌드 테스트를 실행하는 함수
    
    Args:
        project_path: 프로젝트 경로 (기본값: 현재 디렉토리)
        docker_compose_file: docker-compose.yml 파일 경로
        service_name: 빌드할 서비스 이름
        build_only: 빌드만 실행하고 실행하지 않음
        verbose: 상세 출력 여부
    
    Returns:
        Dict: 실행 결과 정보
    """
    
    if project_path is None:
        project_path = os.getcwd()
    
    result = {
        "success": False,
        "project_path": project_path,
        "docker_compose_file": docker_compose_file,
        "service_name": service_name,
        "build_only": build_only,
        "steps": [],
        "errors": [],
        "logs": []
    }
    
    try:
        # 1. 프로젝트 경로 확인
        if verbose:
            print(f"🔍 프로젝트 경로 확인: {project_path}")
        
        if not os.path.exists(project_path):
            result["errors"].append(f"프로젝트 경로가 존재하지 않습니다: {project_path}")
            return result
        
        # 2. pyproject.toml 파일 확인
        pyproject_path = os.path.join(project_path, "pyproject.toml")
        if not os.path.exists(pyproject_path):
            result["errors"].append("pyproject.toml 파일을 찾을 수 없습니다.")
            return result
        
        result["steps"].append("pyproject.toml 파일 확인 완료")
        
        # 3. Docker 상태 확인
        if verbose:
            print("🔍 Docker 상태 확인 중...")
        
        try:
            docker_info = subprocess.run(
                ["docker", "info"],
                capture_output=True,
                text=True,
                check=True
            )
            result["steps"].append("Docker 상태 확인 완료")
        except subprocess.CalledProcessError:
            result["errors"].append("Docker가 실행되지 않았습니다.")
            return result
        
        # 4. 기존 컨테이너 정리
        if verbose:
            print("🧹 기존 컨테이너 정리 중...")
        
        try:
            cleanup_cmd = ["docker-compose", "-f", docker_compose_file, "down"]
            cleanup_result = subprocess.run(
                cleanup_cmd,
                cwd=project_path,
                capture_output=True,
                text=True
            )
            result["steps"].append("기존 컨테이너 정리 완료")
            result["logs"].append(f"정리 명령어: {' '.join(cleanup_cmd)}")
        except Exception as e:
            result["errors"].append(f"컨테이너 정리 중 오류: {str(e)}")
            return result
        
        # 5. 데이터베이스 서비스 시작
        if verbose:
            print("🗄️ 데이터베이스 서비스 시작 중...")
        
        try:
            db_start_cmd = ["docker-compose", "up", "-d", "postgres", "redis"]
            db_result = subprocess.run(
                db_start_cmd,
                cwd=os.path.join(project_path, "deployment"),
                capture_output=True,
                text=True,
                check=True
            )
            result["steps"].append("데이터베이스 서비스 시작 완료")
            result["logs"].append(f"DB 시작 명령어: {' '.join(db_start_cmd)}")
            
            # 잠시 대기
            time.sleep(5)
            
        except subprocess.CalledProcessError as e:
            result["errors"].append(f"데이터베이스 서비스 시작 실패: {e.stderr}")
            return result
        
        # 6. API 서비스 빌드
        if verbose:
            print(f"🏗️ {service_name} 서비스 빌드 중 (pyproject.toml 사용)...")
        
        try:
            build_cmd = ["docker-compose", "build", service_name]
            build_result = subprocess.run(
                build_cmd,
                cwd=os.path.join(project_path, "deployment"),
                capture_output=True,
                text=True,
                check=True
            )
            result["steps"].append(f"{service_name} 서비스 빌드 완료")
            result["logs"].append(f"빌드 명령어: {' '.join(build_cmd)}")
            result["logs"].append(f"빌드 출력: {build_result.stdout}")
            
        except subprocess.CalledProcessError as e:
            result["errors"].append(f"서비스 빌드 실패: {e.stderr}")
            return result
        
        # 7. 서비스 실행 (build_only가 False인 경우)
        if not build_only:
            if verbose:
                print(f"🚀 {service_name} 서비스 시작 중...")
            
            try:
                start_cmd = ["docker-compose", "up", "-d", service_name]
                start_result = subprocess.run(
                    start_cmd,
                    cwd=os.path.join(project_path, "deployment"),
                    capture_output=True,
                    text=True,
                    check=True
                )
                result["steps"].append(f"{service_name} 서비스 시작 완료")
                result["logs"].append(f"시작 명령어: {' '.join(start_cmd)}")
                
                # 서비스 상태 확인
                time.sleep(3)
                
                status_cmd = ["docker-compose", "ps"]
                status_result = subprocess.run(
                    status_cmd,
                    cwd=os.path.join(project_path, "deployment"),
                    capture_output=True,
                    text=True,
                    check=True
                )
                result["logs"].append(f"서비스 상태:\n{status_result.stdout}")
                
            except subprocess.CalledProcessError as e:
                result["errors"].append(f"서비스 시작 실패: {e.stderr}")
                return result
        
        # 8. 성공 메시지 출력
        if verbose:
            print("✅ 컨테이너 빌드 테스트가 성공적으로 완료되었습니다!")
            if not build_only:
                print("")
                print("📊 서비스 URL:")
                print("  - API Gateway: http://localhost:8000")
                print("  - Swagger UI: http://localhost:8000/docs")
                print("")
                print("🛠️ 유용한 명령어:")
                print(f"  - 로그 확인: docker-compose -f {docker_compose_file} logs {service_name}")
                print(f"  - 서비스 중지: docker-compose -f {docker_compose_file} down")
                print(f"  - 서비스 재시작: docker-compose -f {docker_compose_file} restart {service_name}")
                print("")
                print("🧪 테스트 예시:")
                print("  curl http://localhost:8000/")
                print("  curl 'http://localhost:8000/api/v1/recommend/invest-timing?asset_name=삼성전자'")
        
        result["success"] = True
        return result
        
    except Exception as e:
        result["errors"].append(f"예상치 못한 오류: {str(e)}")
        return result


def ensure_container_status_check(
    project_path: str = None,
    docker_compose_file: str = "infra/docker-compose.yml"
) -> Dict[str, any]:
    """
    컨테이너 상태를 확인하는 함수
    
    Args:
        project_path: 프로젝트 경로
        docker_compose_file: docker-compose.yml 파일 경로
    
    Returns:
        Dict: 상태 확인 결과
    """
    
    if project_path is None:
        project_path = os.getcwd()
    
    result = {
        "success": False,
        "project_path": project_path,
        "docker_compose_file": docker_compose_file,
        "services": {},
        "errors": []
    }
    
    try:
        # 서비스 상태 확인
        status_cmd = ["docker-compose", "ps"]
        status_result = subprocess.run(
            status_cmd,
            cwd=os.path.join(project_path, "deployment"),
            capture_output=True,
            text=True,
            check=True
        )
        
        result["services"] = status_result.stdout
        result["success"] = True
        
        return result
        
    except subprocess.CalledProcessError as e:
        result["errors"].append(f"상태 확인 실패: {e.stderr}")
        return result


if __name__ == "__main__":
    # 테스트 실행
    print("🐳 컨테이너 빌드 테스트를 시작합니다...")
    
    # 현재 디렉토리에서 실행
    result = ensure_container_build_test(
        project_path=os.getcwd(),
        build_only=False,
        verbose=True
    )
    
    if result["success"]:
        print("✅ 테스트가 성공적으로 완료되었습니다!")
    else:
        print("❌ 테스트가 실패했습니다.")
        for error in result["errors"]:
            print(f"  - {error}") 