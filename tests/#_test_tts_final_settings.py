#!/usr/bin/env python3
"""
최종 설정이 적용된 ensure_spoken 함수 테스트
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkg_py.functions_split.ensure_spoken import ensure_spoken
import time

def test_ensure_spoken_with_final_settings():
    """최종 설정으로 ensure_spoken 테스트"""
    print("🎧 최종 설정이 적용된 ensure_spoken 테스트")
    print("=" * 50)
    
    test_texts = [
        "안녕하세요, 최종 설정 테스트입니다",
        "볼륨 30%, 속도 1.2로 설정되었습니다",
        "Windows SAPI 엔진을 사용합니다",
        "헤드폰에서 완벽하게 들립니다",
        "테스트가 완료되었습니다"
    ]
    
    for i, text in enumerate(test_texts, 1):
        print(f"🔊 테스트 {i}: '{text}'")
        
        try:
            # ensure_spoken 함수 호출
            ensure_spoken(str_working=text, after_delay=0.5)
            print(f"✅ 테스트 {i} 성공")
            
        except Exception as e:
            print(f"❌ 테스트 {i} 실패: {e}")
        
        time.sleep(1)  # 다음 테스트 전 대기
        print()

def test_ensure_spoken_with_different_texts():
    """다양한 텍스트로 테스트"""
    print("\n🔊 다양한 텍스트 테스트")
    print("=" * 50)
    
    test_cases = [
        "간단한 테스트입니다",
        "한글과 영어가 섞인 test입니다",
        "특수문자 테스트: @#$%^&*()",
        "긴 문장 테스트입니다. 이것은 여러 문장으로 구성된 긴 텍스트입니다.",
        "숫자 테스트: 12345"
    ]
    
    for i, text in enumerate(test_cases, 1):
        print(f"🔊 케이스 {i}: '{text}'")
        
        try:
            ensure_spoken(str_working=text, after_delay=0.3)
            print(f"✅ 케이스 {i} 성공")
            
        except Exception as e:
            print(f"❌ 케이스 {i} 실패: {e}")
        
        time.sleep(1)
        print()

def main():
    """메인 함수"""
    print("🎧 ensure_spoken 최종 설정 테스트 시작")
    print("=" * 60)
    
    print("📋 현재 설정:")
    print("- 엔진: Windows SAPI (우선순위 1위)")
    print("- 속도: 1.2 (자연스러운 빠름)")
    print("- 볼륨: 30% (적당한 크기)")
    print("- 출력: 헤드폰 (정상 작동)")
    print()
    
    # 1. 기본 테스트
    test_ensure_spoken_with_final_settings()
    
    # 2. 다양한 텍스트 테스트
    test_ensure_spoken_with_different_texts()
    
    print("🎉 ensure_spoken 최종 설정 테스트 완료!")
    print("헤드폰에서 모든 테스트가 정상적으로 들렸는지 확인해주세요!")

if __name__ == "__main__":
    main() 