# tests/test_tts_windows.py
"""
Windows 환경 TTS 테스트
"""

import sys
import os
import time
import platform

# 프로젝트 루트를 Python 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def test_windows_environment():
    """Windows 환경 확인"""
    print("🧪 Windows 환경 확인")
    
    if platform.system() == "Windows":
        print("✅ Windows 환경입니다")
        return True
    else:
        print(f"❌ Windows가 아닙니다: {platform.system()}")
        return False


def test_pyttsx3():
    """pyttsx3 테스트"""
    print("🧪 pyttsx3 테스트")
    
    try:
        import pyttsx3
        
        # 엔진 초기화
        engine = pyttsx3.init()
        
        # 음성 목록 확인
        voices = engine.getProperty('voices')
        print(f"✅ pyttsx3 사용 가능 (음성 개수: {len(voices)})")
        
        # 음성 정보 출력
        for i, voice in enumerate(voices):
            print(f"  음성 {i+1}: {voice.name} ({voice.id})")
        
        # 설정
        engine.setProperty('rate', 150)  # 속도
        engine.setProperty('volume', 0.8)  # 볼륨
        
        # 테스트 음성 재생
        test_text = "안녕하세요, pyttsx3 테스트입니다"
        print(f"🔊 '{test_text}' 재생 중...")
        
        start_time = time.time()
        engine.say(test_text)
        engine.runAndWait()
        end_time = time.time()
        
        execution_time = end_time - start_time
        print(f"✅ pyttsx3 테스트 성공 (실행시간: {execution_time:.2f}초)")
        
        return True
        
    except ImportError:
        print("❌ pyttsx3 설치 필요: uv add pyttsx3")
        return False
    except Exception as e:
        print(f"❌ pyttsx3 오류: {str(e)[:50]}")
        return False


def test_windows_sapi():
    """Windows SAPI 테스트"""
    print("🧪 Windows SAPI 테스트")
    
    try:
        import win32com.client
        
        # SAPI 스피커 생성
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        
        # 음성 목록 확인
        voices = speaker.GetVoices()
        print(f"✅ Windows SAPI 사용 가능 (음성 개수: {voices.Count})")
        
        # 음성 정보 출력
        for i in range(voices.Count):
            voice = voices.Item(i)
            print(f"  음성 {i+1}: {voice.GetDescription()}")
        
        # 테스트 음성 재생
        test_text = "안녕하세요, Windows SAPI 테스트입니다"
        print(f"🔊 '{test_text}' 재생 중...")
        
        start_time = time.time()
        speaker.Speak(test_text)
        end_time = time.time()
        
        execution_time = end_time - start_time
        print(f"✅ Windows SAPI 테스트 성공 (실행시간: {execution_time:.2f}초)")
        
        return True
        
    except ImportError:
        print("❌ pywin32 설치 필요: uv add pywin32")
        return False
    except Exception as e:
        print(f"❌ Windows SAPI 오류: {str(e)[:50]}")
        return False


def test_gtts():
    """gTTS 테스트"""
    print("🧪 gTTS 테스트")
    
    try:
        from gtts import gTTS
        import tempfile
        import os
        
        print("✅ gTTS 사용 가능")
        
        # 테스트 음성 생성
        test_text = "안녕하세요, gTTS 테스트입니다"
        print(f"🔊 '{test_text}' 음성 파일 생성 중...")
        
        start_time = time.time()
        
        # 임시 파일에 TTS 저장
        tts = gTTS(text=test_text, lang='ko')
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            temp_file = fp.name
            tts.save(temp_file)
        
        # 파일 생성 확인
        if os.path.exists(temp_file):
            file_size = os.path.getsize(temp_file)
            print(f"✅ gTTS 파일 생성 성공 (크기: {file_size} bytes)")
            
            # 임시 파일 삭제
            os.unlink(temp_file)
            
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"✅ gTTS 테스트 성공 (실행시간: {execution_time:.2f}초)")
            
            return True
        else:
            print("❌ gTTS 파일 생성 실패")
            return False
        
    except ImportError:
        print("❌ gTTS 설치 필요: uv add gTTS")
        return False
    except Exception as e:
        print(f"❌ gTTS 오류: {str(e)[:50]}")
        return False


def test_hybrid_tts():
    """하이브리드 TTS 테스트"""
    print("🧪 하이브리드 TTS 테스트")
    
    def try_pyttsx3(text):
        """pyttsx3로 TTS 시도"""
        try:
            import pyttsx3
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.setProperty('volume', 0.8)
            engine.say(text)
            engine.runAndWait()
            return True
        except Exception:
            return False
    
    def try_windows_sapi(text):
        """Windows SAPI로 TTS 시도"""
        try:
            import win32com.client
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak(text)
            return True
        except Exception:
            return False
    
    def try_gtts(text):
        """gTTS로 TTS 시도"""
        try:
            from gtts import gTTS
            import tempfile
            import os
            
            tts = gTTS(text=text, lang='ko')
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
                temp_file = fp.name
                tts.save(temp_file)
            
            if os.path.exists(temp_file):
                os.unlink(temp_file)
                return True
            return False
        except Exception:
            return False
    
    test_text = "안녕하세요, 하이브리드 TTS 테스트입니다"
    print(f"🔊 '{test_text}' 테스트 중...")
    
    # 우선순위별로 TTS 시도
    tts_methods = [
        ("pyttsx3", try_pyttsx3),
        ("Windows SAPI", try_windows_sapi),
        ("gTTS", try_gtts)
    ]
    
    for method_name, method_func in tts_methods:
        print(f"  🔄 {method_name} 시도 중...")
        if method_func(test_text):
            print(f"  ✅ {method_name} 성공")
            return True
        else:
            print(f"  ❌ {method_name} 실패")
    
    print("❌ 모든 TTS 방법 실패")
    return False


def test_hybrid_tts_with_voice_config():
    """음성 설정을 포함한 하이브리드 TTS 테스트"""
    print("🧪 음성 설정을 포함한 하이브리드 TTS 테스트")
    
    try:
        from pkg_py.functions_split.ensure_spoken_hybrid import (
            HybridTTS, VoiceConfig, get_available_voices, set_voice_config
        )
        
        # 사용 가능한 음성 목록 확인
        voices = get_available_voices()
        print(f"✅ 사용 가능한 음성 목록:")
        for method, voice_list in voices.items():
            print(f"  {method}: {len(voice_list)}개")
        
        # 다양한 음성 설정으로 테스트
        test_configs = [
            VoiceConfig(name="기본 음성", rate=150, volume=0.8),
            VoiceConfig(name="빠른 음성", rate=200, volume=0.9),
            VoiceConfig(name="느린 음성", rate=100, volume=0.7),
        ]
        
        test_text = "안녕하세요, 음성 설정 테스트입니다"
        
        for i, config in enumerate(test_configs, 1):
            print(f"\n🔊 테스트 {i}: {config.name}")
            print(f"  속도: {config.rate}, 볼륨: {config.volume}")
            
            set_voice_config(config)
            
            # 하이브리드 TTS 테스트
            hybrid_tts = HybridTTS()
            success = hybrid_tts.speak(test_text)
            
            if success:
                print(f"  ✅ {config.name} 성공")
            else:
                print(f"  ❌ {config.name} 실패")
        
        return True
        
    except ImportError as e:
        print(f"❌ 모듈 import 오류: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ 테스트 오류: {str(e)}")
        return False


def test_ensure_spoken_hybrid():
    """개선된 ensure_spoken 함수 테스트"""
    print("🧪 개선된 ensure_spoken 함수 테스트")
    
    try:
        from pkg_py.functions_split.ensure_spoken import ensure_spoken
        from pkg_py.functions_split.ensure_spoken_hybrid import VoiceConfig
        
        # 기본 테스트
        test_text = "안녕하세요, 개선된 ensure_spoken 테스트입니다"
        print(f"🔊 '{test_text}' 재생 중...")
        
        ensure_spoken(test_text)
        
        # 음성 설정 테스트
        voice_config = VoiceConfig(name="테스트 음성", rate=180, volume=0.9)
        test_text_with_config = "안녕하세요, 음성 설정이 적용된 테스트입니다"
        print(f"🔊 '{test_text_with_config}' 재생 중...")
        
        ensure_spoken(test_text_with_config, voice_config=voice_config)
        
        print("✅ 개선된 ensure_spoken 함수 테스트 성공")
        return True
        
    except Exception as e:
        print(f"❌ 테스트 오류: {str(e)}")
        return False


def main():
    """메인 테스트 함수"""
    print("🚀 Windows TTS 테스트 시작")
    print("=" * 50)
    
    # Windows 환경 확인
    if not test_windows_environment():
        print("❌ Windows 환경이 아니므로 테스트를 중단합니다.")
        return
    
    print()
    
    # 개별 TTS 테스트
    test_results = []
    
    test_results.append(("pyttsx3", test_pyttsx3()))
    print()
    
    test_results.append(("Windows SAPI", test_windows_sapi()))
    print()
    
    test_results.append(("gTTS", test_gtts()))
    print()
    
    # 하이브리드 테스트
    test_results.append(("하이브리드 TTS", test_hybrid_tts()))
    print()
    
    # 음성 설정을 포함한 하이브리드 테스트
    test_results.append(("하이브리드 TTS (음성 설정)", test_hybrid_tts_with_voice_config()))
    print()
    
    # 개선된 ensure_spoken 함수 테스트
    test_results.append(("개선된 ensure_spoken", test_ensure_spoken_hybrid()))
    print()
    
    # 결과 요약
    print("📊 테스트 결과 요약")
    print("=" * 30)
    for method, result in test_results:
        status = "✅ 성공" if result else "❌ 실패"
        print(f"{method}: {status}")
    
    # 성공한 방법 개수
    success_count = sum(1 for _, result in test_results if result)
    print(f"\n총 {len(test_results)}개 방법 중 {success_count}개 성공")


if __name__ == "__main__":
    main() 