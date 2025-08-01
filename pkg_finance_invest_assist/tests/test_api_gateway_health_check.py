"""
API Gateway 헬스체크 테스트
"""
import requests
import time
import inspect
from typing import Dict, Any


def test_api_gateway_health_check() -> Dict[str, Any]:
    """
    API Gateway 헬스체크를 테스트합니다.
    """
    # 현재 함수명을 동적으로 가져오기
    func_n = inspect.currentframe().f_code.co_name
    
    print(f"🔍 {func_n} 함수 실행 시작")
    
    try:
        # API Gateway 헬스체크
        response = requests.get("http://localhost:8000/health", timeout=10)
        
        if response.status_code == 200:
            print("✅ API Gateway 헬스체크 성공")
            return {"success": True, "status_code": response.status_code}
        else:
            print(f"❌ API Gateway 헬스체크 실패: {response.status_code}")
            return {"success": False, "status_code": response.status_code}
            
    except requests.exceptions.RequestException as e:
        print(f"❌ API Gateway 연결 실패: {e}")
        return {"success": False, "error": str(e)}


def test_api_gateway_root_endpoint() -> Dict[str, Any]:
    """
    API Gateway 루트 엔드포인트를 테스트합니다.
    """
    # 현재 함수명을 동적으로 가져오기
    func_n = inspect.currentframe().f_code.co_name
    
    print(f"🔍 {func_n} 함수 실행 시작")
    
    try:
        response = requests.get("http://localhost:8000/", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API Gateway 루트 엔드포인트 성공: {data}")
            return {"success": True, "data": data}
        else:
            print(f"❌ API Gateway 루트 엔드포인트 실패: {response.status_code}")
            return {"success": False, "status_code": response.status_code}
            
    except requests.exceptions.RequestException as e:
        print(f"❌ API Gateway 연결 실패: {e}")
        return {"success": False, "error": str(e)}


def main():
    """
    메인 테스트 실행 함수
    """
    # 현재 함수명을 동적으로 가져오기
    func_n = inspect.currentframe().f_code.co_name
    
    print(f"🚀 {func_n} 함수 시작")
    print("=" * 50)
    
    # 서비스 시작 대기
    print("⏳ 서비스 시작 대기 중...")
    time.sleep(5)
    
    # 테스트 실행
    health_result = test_api_gateway_health_check()
    root_result = test_api_gateway_root_endpoint()
    
    # 결과 요약
    print("\n📊 테스트 결과:")
    print(f"헬스체크: {'✅ 성공' if health_result['success'] else '❌ 실패'}")
    print(f"루트 엔드포인트: {'✅ 성공' if root_result['success'] else '❌ 실패'}")
    
    if health_result['success'] and root_result['success']:
        print("\n🎉 모든 API Gateway 테스트가 성공했습니다!")
        return 0
    else:
        print("\n💥 일부 테스트가 실패했습니다.")
        return 1


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code) 