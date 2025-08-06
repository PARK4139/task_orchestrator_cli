#!/usr/bin/env python3
"""
PK System 내장 Alias 관리 기능 테스트
"""
import os
import sys
import subprocess
from pathlib import Path

# 프로젝트 루트 경로 추가
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

def test_alias_functions():
    """내장 alias 함수들 테스트"""
    print("🧪 PK System 내장 Alias 관리 기능 테스트")
    print("=" * 50)
    
    try:
        # ensure_pk_system_enabled 모듈 import
        from pkg_py.functions_split.ensure_pk_system_enabled import (
            get_environment_paths,
            load_default_aliases,
            load_all_aliases,
            setup_pk_environment_with_aliases
        )
        
        print("✅ 모듈 import 성공")
        
        # 환경변수 경로 테스트
        print("\n📁 환경변수 경로 테스트:")
        paths = get_environment_paths()
        for key, value in paths.items():
            print(f"  {key}: {value}")
        
        # 기본 alias 로드 테스트
        print("\n📋 기본 alias 로드 테스트:")
        load_default_aliases()
        
        # 로드 후 _aliases import
        from pkg_py.functions_split.ensure_pk_system_enabled import aliases
        print(f"  로드된 alias 개수: {len(aliases)}")
        
        # alias 카테고리별 확인
        categories = {
            "시스템": ['x', 'wsld', 'wsl24', 'wsl20', 'wsl18', 'reboot', 'poweroff', 'logout'],
            "관리자": ['cmda', 'ps', 'psa'],
            "IDE": ['pycharm', 'code'],
            "디렉토리": ['0', '1', '2', '3', '4', '5'],
            "편집": ['E100', 'E200', 'E000'],
            "유틸리티": ['.', 'gpt', 'history', 'cat', 'which', 'pwd', 'venv', 'pk', 'ls', 'rm_f', 'rm_d', 'find_f', 'find_d', 'find_pnx', 'cp_pwd']
        }
        
        for category, alias_names in categories.items():
            found_count = sum(1 for name in alias_names if name in aliases)
            print(f"  {category}: {found_count}/{len(alias_names)} 개")
        
        # 환경변수 설정 테스트 (Windows에서만)
        if os.name == 'nt':  # Windows
            print("\n🔧 환경변수 설정 테스트:")
            result = setup_pk_environment_with_aliases()
            print(f"  환경변수 설정 결과: {'성공' if result else '실패'}")
        
        print("\n✅ 모든 테스트 완료")
        
    except ImportError as e:
        print(f"❌ 모듈 import 실패: {e}")
    except Exception as e:
        print(f"❌ 테스트 중 오류: {e}")

def test_doskey_integration():
    """doskey 통합 테스트 (Windows에서만)"""
    if os.name != 'nt':
        print("ℹ️ Windows가 아니므로 doskey 테스트를 건너뜁니다.")
        return
    
    print("\n🔧 Doskey 통합 테스트:")
    
    try:
        from pkg_py.functions_split.ensure_pk_system_enabled import (
            load_default_aliases,
            save_to_doskey
        )
        
        # 기본 alias 로드
        load_default_aliases()
        
        # 로드 후 _aliases import
        from pkg_py.functions_split.ensure_pk_system_enabled import aliases
        
        # 몇 개의 alias만 테스트
        test_aliases = ['x', 'ls', 'pwd']
        success_count = 0
        
        for alias_name in test_aliases:
            if alias_name in aliases:
                command = aliases[alias_name]
                if save_to_doskey(alias_name, command):
                    print(f"  ✅ {alias_name} = {command}")
                    success_count += 1
                else:
                    print(f"  ❌ {alias_name} 저장 실패")
            else:
                print(f"  ⚠️ {alias_name} alias를 찾을 수 없습니다")
        
        print(f"\n📊 Doskey 테스트 결과: {success_count}/{len(test_aliases)} 성공")
        
    except Exception as e:
        print(f"❌ Doskey 테스트 실패: {e}")

def main():
    """메인 테스트 함수"""
    print("🚀 PK System 내장 Alias 관리 기능 테스트 시작")
    print("=" * 60)
    
    # 기본 함수 테스트
    test_alias_functions()
    
    # Doskey 통합 테스트
    test_doskey_integration()
    
    print("\n🎉 모든 테스트 완료!")

if __name__ == "__main__":
    main() 