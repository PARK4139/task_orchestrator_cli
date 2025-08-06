#!/usr/bin/env python3
"""
PK System 내장 Alias 관리 기능 사용 예제
"""
import os
import sys
from pathlib import Path

# 프로젝트 루트 경로 추가
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

def show_alias_categories():
    """alias 카테고리별로 보여주기"""
    print("📋 PK System 내장 Alias 카테고리")
    print("=" * 50)
    
    try:
        from pkg_py.functions_split.ensure_pk_system_enabled import (
            load_default_aliases
        )
        
        # 기본 alias 로드
        load_default_aliases()
        
        # 로드 후 _aliases import
        from pkg_py.functions_split.ensure_pk_system_enabled import aliases
        
        # 카테고리별 alias 정리
        categories = {
            "🖥️ 시스템": ['x', 'wsld', 'wsl24', 'wsl20', 'wsl18', 'reboot', 'poweroff', 'logout'],
            "🔧 관리자": ['cmda', 'ps', 'psa'],
            "💻 IDE": ['pycharm', 'code'],
            "📁 디렉토리": ['0', '1', '2', '3', '4', '5'],
            "✏️ 편집": ['E100', 'E200', 'E000'],
            "🛠️ 유틸리티": ['.', 'gpt', 'history', 'cat', 'which', 'pwd', 'venv', 'pk', 'ls', 'rm_f', 'rm_d', 'find_f', 'find_d', 'find_pnx', 'cp_pwd']
        }
        
        for category, alias_names in categories.items():
            print(f"\n{category}:")
            for name in alias_names:
                if name in aliases:
                    command = aliases[name]
                    print(f"  {name:<10} = {command}")
        
        print(f"\n📊 총 {len(aliases)}개의 alias가 등록되어 있습니다.")
        
    except Exception as e:
        print(f"❌ 오류: {e}")

def show_environment_setup():
    """환경변수 설정 예제"""
    print("\n🔧 PK System 환경변수 설정 예제")
    print("=" * 50)
    
    try:
        from pkg_py.functions_split.ensure_pk_system_enabled import (
            get_environment_paths,
            setup_pk_environment_with_aliases
        )
        
        # 환경변수 경로 확인
        paths = get_environment_paths()
        print("설정되는 환경변수:")
        for key, value in paths.items():
            print(f"  {key}: {value}")
        
        # Windows에서만 환경변수 설정 테스트
        if os.name == 'nt':
            print("\n환경변수 설정 테스트:")
            result = setup_pk_environment_with_aliases()
            print(f"결과: {'성공' if result else '실패'}")
        else:
            print("\nℹ️ Windows가 아니므로 환경변수 설정 테스트를 건너뜁니다.")
        
    except Exception as e:
        print(f"❌ 오류: {e}")

def show_doskey_integration():
    """doskey 통합 예제"""
    print("\n🔧 Doskey 통합 예제")
    print("=" * 50)
    
    try:
        from pkg_py.functions_split.ensure_pk_system_enabled import (
            load_default_aliases,
            save_to_doskey
        )
        
        # 기본 alias 로드
        load_default_aliases()
        
        # 로드 후 _aliases import
        from pkg_py.functions_split.ensure_pk_system_enabled import aliases
        
        # Windows에서만 doskey 테스트
        if os.name == 'nt':
            print("Doskey에 alias 등록 예제:")
            test_aliases = ['x', 'ls', 'pwd', 'pk']
            
            for alias_name in test_aliases:
                if alias_name in aliases:
                    command = aliases[alias_name]
                    success = save_to_doskey(alias_name, command)
                    status = "✅" if success else "❌"
                    print(f"  {status} {alias_name} = {command}")
                else:
                    print(f"  ⚠️ {alias_name} alias를 찾을 수 없습니다")
        else:
            print("ℹ️ Windows가 아니므로 doskey 테스트를 건너뜁니다.")
        
    except Exception as e:
        print(f"❌ 오류: {e}")

def show_usage_guide():
    """사용 가이드"""
    print("\n📖 PK System 내장 Alias 사용 가이드")
    print("=" * 50)
    
    print("""
🔧 주요 기능:
  1. 환경변수 자동 설정
  2. 37개의 유용한 alias 자동 로드
  3. Windows AutoRun 레지스트리 등록
  4. Doskey 통합

📋 주요 Alias:
  • x, wsld, wsl24, wsl20, wsl18 - WSL 관련
  • 0, 1, 2, 3, 4, 5 - 디렉토리 이동
  • pycharm, code - IDE 실행
  • pk - PK System 실행
  • ls, pwd, cat - 유틸리티 명령어

🚀 사용 방법:
  1. ensure_pk_system_enabled.py 실행
  2. Windows AutoRun에 자동 등록
  3. 새 명령 프롬프트에서 alias 사용 가능

💡 특징:
  • 절차지향 방식으로 구현
  • 별도 파일 없이 내장
  • 환경변수 자동 설정
  • Doskey 자동 등록
""")

def main():
    """메인 함수"""
    print("🚀 PK System 내장 Alias 관리 기능 사용 예제")
    print("=" * 60)
    
    # alias 카테고리 보여주기
    show_alias_categories()
    
    # 환경변수 설정 예제
    show_environment_setup()
    
    # doskey 통합 예제
    show_doskey_integration()
    
    # 사용 가이드
    show_usage_guide()
    
    print("\n🎉 예제 완료!")

if __name__ == "__main__":
    main() 