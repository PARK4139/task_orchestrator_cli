#!/usr/bin/env python3
"""
ensure_jarvis_ran() 함수 시작 테스트
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_jarvis_ran import ensure_jarvis_ran
from pkg_py.system_object.map_massages import PkMessages2025

def start_jarvis():
    """Jarvis 시작"""
    print(f"🤖 {PkMessages2025.START_TEST}")
    print("=" * 50)
    
    print(f"📋 {PkMessages2025.COMMANDS}:")
    print("- hello/안녕: 인사")
    print("- time/시간: 현재 시간")
    print("- date/날짜: 현재 날짜")
    print("- clear/클리어: 화면 정리")
    print("- help/도움말: 명령어 목록")
    print("- quit/종료: Jarvis 종료")
    print()
    
    print(f"🎤 {PkMessages2025.STARTING}...")
    print(f"💡 {PkMessages2025.HEADPHONE_CHECK}!")
    print("=" * 50)
    
    try:
        # Jarvis 시작
        ensure_jarvis_ran()
        
    except KeyboardInterrupt:
        print(f"\n🔄 {PkMessages2025.USER_INTERRUPTED}.")
    except Exception as e:
        print(f"\n❌ {PkMessages2025.ERROR_OCCURRED}: {e}")

def main():
    """메인 함수"""
    print(f"🎧 {PkMessages2025.START_TEST}")
    print("=" * 60)
    
    # Jarvis 시작
    start_jarvis()
    
    print(f"\n🎉 {PkMessages2025.TEST_COMPLETE}!")

if __name__ == "__main__":
    main() 