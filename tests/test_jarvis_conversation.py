#!/usr/bin/env python3
"""
대화형 Jarvis 루프 테스트
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_jarvis_ran import ensure_jarvis_ran

def test_jarvis_conversation():
    """대화형 Jarvis 테스트"""
    print("🤖 대화형 Jarvis 루프 테스트")
    print("=" * 50)
    
    print("📋 테스트할 명령어들:")
    print("- hello/안녕: 인사")
    print("- time/시간: 현재 시간")
    print("- date/날짜: 현재 날짜")
    print("- clear/클리어: 화면 정리")
    print("- help/도움말: 명령어 목록")
    print("- quit/종료: Jarvis 종료")
    print()
    
    print("🎤 Jarvis를 시작합니다...")
    print("💡 헤드폰에서 음성이 들리는지 확인하세요!")
    print("=" * 50)
    
    try:
        # Jarvis 시작
        ensure_jarvis_ran()
        
    except KeyboardInterrupt:
        print("\n🔄 사용자가 Jarvis를 중단했습니다.")
    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")

def main():
    """메인 함수"""
    print("🎧 대화형 Jarvis 테스트 시작")
    print("=" * 60)
    
    # Jarvis 대화형 루프 테스트
    test_jarvis_conversation()
    
    print("\n🎉 Jarvis 테스트 완료!")

if __name__ == "__main__":
    main() 