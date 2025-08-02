#!/usr/bin/env python3
"""
ensure_pk_system_processes_killed() 동작 테스트
"""

from pkg_py.functions_split.ensure_pk_system_processes_killed import ensure_pk_system_processes_killed
from pkg_py.functions_split.get_pk_system_process_nxs import get_pk_system_process_nxs
from pkg_py.functions_split.ensure_printed import ensure_printed


def test_get_pk_system_process_nxs():
    """get_pk_system_process_nxs() 함수 테스트"""
    print("🔍 get_pk_system_process_nxs() 테스트")
    print("=" * 50)
    
    try:
        processes = get_pk_system_process_nxs()
        print(f"�� 발견된 pk_* 프로세스 수: {len(processes)}")
        
        for i, process in enumerate(processes[:10], 1):  # 처음 10개만 표시
            print(f"  {i}. {process}")
        
        if len(processes) > 10:
            print(f"  ... 외 {len(processes) - 10}개 더")
        
        return processes
        
    except Exception as e:
        print(f"❌ 오류: {e}")
        return []


def test_ensure_pk_system_processes_killed():
    """ensure_pk_system_processes_killed() 함수 테스트"""
    print("\n🔍 ensure_pk_system_processes_killed() 테스트")
    print("=" * 50)
    
    try:
        # 테스트 전 프로세스 목록 확인
        print("📋 테스트 전 프로세스 목록:")
        processes = get_pk_system_process_nxs()
        for i, process in enumerate(processes[:5], 1):  # 처음 5개만 표시
            print(f"  {i}. {process}")
        
        # 사용자 확인
        response = input("\n⚠️ 이 프로세스들을 종료하시겠습니까? (y/N): ").strip().lower()
        if response != 'y':
            print("❌ 테스트가 취소되었습니다.")
            return
        
        # 프로세스 종료 실행
        print("\n🚀 프로세스 종료 시작...")
        ensure_pk_system_processes_killed()
        
        print("✅ 프로세스 종료 테스트 완료!")
        
    except Exception as e:
        print(f"❌ 오류: {e}")


def test_safe_mode():
    """안전 모드 테스트 - 실제 종료하지 않고 시뮬레이션"""
    print("\n🔍 안전 모드 테스트 (시뮬레이션)")
    print("=" * 50)
    
    try:
        processes = get_pk_system_process_nxs()
        print(f"�� 발견된 pk_* 프로세스 수: {len(processes)}")
        
        # 각 프로세스에 대해 시뮬레이션
        for i, process_name in enumerate(processes[:10], 1):  # 처음 10개만
            print(f"  {i}. {process_name} - 시뮬레이션 종료")
            
            # 실제로는 종료하지 않고 로그만 출력
            print(f"     ✅ 창 제목 '{process_name}'에 대한 창 찾기 시뮬레이션")
            print(f"     ✅ 창 닫기 요청 시뮬레이션 완료")
        
        print("✅ 안전 모드 테스트 완료!")
        
    except Exception as e:
        print(f"❌ 오류: {e}")


def main():
    """메인 테스트 함수"""
    print("🧪 ensure_pk_system_processes_killed() 동작 테스트")
    print("=" * 60)
    
    # 1. 기본 함수 테스트
    test_get_pk_system_process_nxs()
    
    # 2. 안전 모드 테스트 (시뮬레이션)
    test_safe_mode()
    
    # 3. 실제 테스트 (사용자 확인 필요)
    print("\n" + "=" * 60)
    print("⚠️  실제 프로세스 종료 테스트")
    print("⚠️  주의: 이 테스트는 실제로 실행 중인 프로세스를 종료할 수 있습니다!")
    print("=" * 60)
    
    response = input("실제 테스트를 실행하시겠습니까? (y/N): ").strip().lower()
    if response == 'y':
        test_ensure_pk_system_processes_killed()
    else:
        print("❌ 실제 테스트가 취소되었습니다.")
    
    print("\n✅ 모든 테스트 완료!")


if __name__ == "__main__":
    main() 