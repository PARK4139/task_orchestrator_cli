"""
데이터베이스 연결 테스트
"""
import psycopg2
import redis
import time
import inspect
from typing import Dict, Any


def test_postgresql_connection() -> Dict[str, Any]:
    """
    PostgreSQL 데이터베이스 연결을 테스트합니다.
    """
    # 현재 함수명을 동적으로 가져오기
    func_n = inspect.currentframe().f_code.co_name
    
    print(f"🔍 {func_n} 함수 실행 시작")
    
    try:
        # PostgreSQL 연결
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="finance_db",
            user="finance_user",
            password="finance_password"
        )
        
        # 연결 테스트
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        print(f"✅ PostgreSQL 연결 성공: {version[0]}")
        return {"success": True, "version": version[0]}
        
    except Exception as e:
        print(f"❌ PostgreSQL 연결 실패: {e}")
        return {"success": False, "error": str(e)}


def test_redis_connection() -> Dict[str, Any]:
    """
    Redis 캐시 연결을 테스트합니다.
    """
    # 현재 함수명을 동적으로 가져오기
    func_n = inspect.currentframe().f_code.co_name
    
    print(f"🔍 {func_n} 함수 실행 시작")
    
    try:
        # Redis 연결
        r = redis.Redis(host="localhost", port=6379, db=0)
        
        # 연결 테스트
        r.ping()
        
        # 간단한 테스트 데이터 쓰기/읽기
        test_key = "test_connection"
        test_value = "test_value"
        r.set(test_key, test_value)
        retrieved_value = r.get(test_key)
        r.delete(test_key)
        
        if retrieved_value.decode() == test_value:
            print("✅ Redis 연결 성공")
            return {"success": True}
        else:
            print("❌ Redis 데이터 읽기/쓰기 실패")
            return {"success": False, "error": "Data read/write failed"}
            
    except Exception as e:
        print(f"❌ Redis 연결 실패: {e}")
        return {"success": False, "error": str(e)}


def test_database_operations() -> Dict[str, Any]:
    """
    데이터베이스 기본 작업을 테스트합니다.
    """
    # 현재 함수명을 동적으로 가져오기
    func_n = inspect.currentframe().f_code.co_name
    
    print(f"🔍 {func_n} 함수 실행 시작")
    
    try:
        # PostgreSQL 연결
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="finance_db",
            user="finance_user",
            password="finance_password"
        )
        
        cursor = conn.cursor()
        
        # 테이블 존재 확인
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """)
        
        tables = cursor.fetchall()
        print(f"✅ 데이터베이스 테이블 확인: {len(tables)}개 테이블 발견")
        
        cursor.close()
        conn.close()
        
        return {"success": True, "table_count": len(tables)}
        
    except Exception as e:
        print(f"❌ 데이터베이스 작업 실패: {e}")
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
    print("⏳ 데이터베이스 서비스 시작 대기 중...")
    time.sleep(5)
    
    # 테스트 실행
    postgres_result = test_postgresql_connection()
    redis_result = test_redis_connection()
    db_ops_result = test_database_operations()
    
    # 결과 요약
    print("\n📊 테스트 결과:")
    print(f"PostgreSQL: {'✅ 성공' if postgres_result['success'] else '❌ 실패'}")
    print(f"Redis: {'✅ 성공' if redis_result['success'] else '❌ 실패'}")
    print(f"데이터베이스 작업: {'✅ 성공' if db_ops_result['success'] else '❌ 실패'}")
    
    success_count = sum([
        postgres_result['success'],
        redis_result['success'],
        db_ops_result['success']
    ])
    
    if success_count == 3:
        print("\n🎉 모든 데이터베이스 테스트가 성공했습니다!")
        return 0
    else:
        print(f"\n💥 {3 - success_count}개 테스트가 실패했습니다.")
        return 1


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code) 