"""
하이브리드 TTS 함수 - 여러 TTS 방법을 순차적으로 시도
목소리 변경 기능 포함
"""

import os
import time
import tempfile
import threading
import queue
from typing import Optional, List, Dict, Any
from dataclasses import dataclass

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.is_internet_connected import is_internet_connected
from pkg_py.functions_split.remove_special_characters import remove_special_characters
from pkg_py.functions_split.is_containing_special_characters_with_thread import is_containing_special_characters_with_thread
from pkg_py.system_object.etc import PLAYING_SOUNDS


@dataclass
class VoiceConfig:
    """음성 설정"""
    name: str = "기본 음성"
    rate: int = 150  # 속도 (pyttsx3)
    volume: float = 0.8  # 볼륨 (pyttsx3)
    voice_id: Optional[str] = None  # 특정 음성 ID
    language: str = "ko"  # 언어 (gTTS)


class HybridTTS:
    """하이브리드 TTS 클래스"""
    
    def __init__(self):
        self.voice_config = VoiceConfig()
        self.tts_methods = [
            ("Windows SAPI", self._try_windows_sapi),  # SAPI를 첫 번째로 이동
            ("pyttsx3", self._try_pyttsx3),
            ("gTTS", self._try_gtts)
        ]
        self._queue = queue.Queue()
        self._thread_started = False
        self._cache_dir = os.path.join(os.path.expanduser("~"), "Downloads", "pk_system", "pkg_sound")
        os.makedirs(self._cache_dir, exist_ok=True)
    
    def set_voice_config(self, config: VoiceConfig):
        """음성 설정 변경"""
        self.voice_config = config
        ensure_printed(f"음성 설정 변경: {config.name}")
    
    def get_available_voices(self) -> Dict[str, List[Dict[str, Any]]]:
        """사용 가능한 음성 목록 반환"""
        voices = {}
        
        # pyttsx3 음성 목록
        try:
            import pyttsx3
            engine = pyttsx3.init()
            pyttsx3_voices = engine.getProperty('voices')
            voices["pyttsx3"] = [
                {"name": voice.name, "id": voice.id, "languages": getattr(voice, 'languages', [])}
                for voice in pyttsx3_voices
            ]
        except Exception:
            voices["pyttsx3"] = []
        
        # Windows SAPI 음성 목록
        try:
            import win32com.client
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            sapi_voices = speaker.GetVoices()
            voices["windows_sapi"] = [
                {"name": sapi_voices.Item(i).GetDescription(), "id": i}
                for i in range(sapi_voices.Count)
            ]
        except Exception:
            voices["windows_sapi"] = []
        
        return voices
    
    def _try_pyttsx3(self, text: str) -> bool:
        """pyttsx3로 TTS 시도"""
        try:
            import pyttsx3
            
            engine = pyttsx3.init()
            
            # 음성 설정 적용
            engine.setProperty('rate', self.voice_config.rate)
            engine.setProperty('volume', self.voice_config.volume)
            
            # 특정 음성 ID가 설정된 경우
            if self.voice_config.voice_id:
                voices = engine.getProperty('voices')
                for voice in voices:
                    if self.voice_config.voice_id in voice.id:
                        engine.setProperty('voice', voice.id)
                        break
            
            engine.say(text)
            engine.runAndWait()
            return True
            
        except Exception as e:
            ensure_printed(f"pyttsx3 오류: {str(e)[:50]}")
            return False
    
    def _try_windows_sapi(self, text: str) -> bool:
        """Windows SAPI로 TTS 시도"""
        try:
            import win32com.client
            
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            
            # 속도 설정 (1.2로 설정, 실패하면 1.0으로)
            # 테스트 가능한 다른 속도: 0.5, 1.0, 1.5, 2.0
            try:
                speaker.Rate = 1.2  # 현재 설정: 1.2 (자연스러운 빠름)
            except:
                try:
                    speaker.Rate = 1.0  # 대체 설정: 1.0 (보통 속도)
                except:
                    pass  # 기본 속도 사용
            
            # 볼륨 설정 (30%로 설정)
            # 테스트 가능한 다른 볼륨: 20, 30, 50, 70
            try:
                speaker.Volume = 30  # 현재 설정: 30% (적당한 크기)
            except:
                pass  # 기본 볼륨 사용
            
            # 특정 음성 ID가 설정된 경우
            if self.voice_config.voice_id:
                voices = speaker.GetVoices()
                for i in range(voices.Count):
                    voice = voices.Item(i)
                    if self.voice_config.voice_id in voice.GetDescription():
                        speaker.Voice = voice
                        break
            
            speaker.Speak(text)
            return True
            
        except Exception as e:
            ensure_printed(f"Windows SAPI 오류: {str(e)[:50]}")
            return False
    
    def _try_gtts(self, text: str) -> bool:
        """gTTS로 TTS 시도"""
        try:
            from gtts import gTTS
            import tempfile
            
            # 캐시 파일명 생성
            cache_filename = f"{hash(text)}_{self.voice_config.language}.mp3"
            cache_path = os.path.join(self._cache_dir, cache_filename)
            
            # 캐시된 파일이 있으면 재생
            if os.path.exists(cache_path):
                try:
                    import pyglet
                    source = pyglet.media.load(cache_path)
                    player = source.play()
                    
                    # 재생 시간 대기
                    duration = self._get_mp3_duration(cache_path)
                    time.sleep(duration)
                    return True
                except Exception:
                    pass
            
            # 새로 생성
            tts = gTTS(text=text, lang=self.voice_config.language)
            tts.save(cache_path)
            
            # 재생
            import pyglet
            source = pyglet.media.load(cache_path)
            player = source.play()
            
            # 재생 시간 대기
            duration = self._get_mp3_duration(cache_path)
            time.sleep(duration)
            
            return True
            
        except Exception as e:
            ensure_printed(f"gTTS 오류: {str(e)[:50]}")
            return False
    
    def _get_mp3_duration(self, file_path: str) -> float:
        """MP3 파일 재생 시간 반환"""
        try:
            from mutagen.mp3 import MP3
            audio = MP3(file_path)
            return audio.info.length
        except Exception:
            return 2.0  # 기본값
    
    def speak(self, text: str, force_method: Optional[str] = None) -> bool:
        """텍스트를 음성으로 재생"""
        if not text or not text.strip():
            return False
        
        # 특수문자 제거
        if is_containing_special_characters_with_thread(text=text):
            text = remove_special_characters(text=text)
        
        # 특정 방법 강제 사용
        if force_method:
            for method_name, method_func in self.tts_methods:
                if method_name.lower() == force_method.lower():
                    return method_func(text)
            return False
        
        # 하이브리드 방식: 순차적으로 시도
        for method_name, method_func in self.tts_methods:
            ensure_printed(f"🔄 {method_name} 시도 중...")
            if method_func(text):
                ensure_printed(f"✅ {method_name} 성공")
                return True
            else:
                ensure_printed(f"❌ {method_name} 실패")
        
        ensure_printed("❌ 모든 TTS 방법 실패")
        return False
    
    def speak_async(self, text: str, delay: float = 0.5):
        """비동기 음성 재생"""
        def _speak_with_delay():
            time.sleep(delay)
            self.speak(text)
        
        thread = threading.Thread(target=_speak_with_delay, daemon=True)
        thread.start()
        return thread


# 전역 하이브리드 TTS 인스턴스
_hybrid_tts = HybridTTS()


def ensure_spoken_hybrid(str_working, after_delay=1.00, delimiter=None, voice_config=None):
    """
    하이브리드 TTS 함수
    
    Args:
        str_working: 읽을 텍스트
        after_delay: 재생 후 대기 시간
        delimiter: 구분자 (기본값: 쉼표)
        voice_config: 음성 설정 (VoiceConfig 객체)
    """
    import traceback
    
    try:
        # 음성 설정 적용
        if voice_config:
            _hybrid_tts.set_voice_config(voice_config)
        
        # 인터넷 연결 확인 (gTTS 사용 시)
        if not is_internet_connected():
            ensure_printed("인터넷 연결이 없어 gTTS를 사용할 수 없습니다.")
        
        # 구분자 처리
        if not delimiter:
            delimiter = ','
        
        str_working = str(str_working).strip()
        if not str_working:
            return
        
        # 구분자로 분할
        if delimiter in str_working:
            segments = [seg.strip() for seg in str_working.split(delimiter) if seg.strip()]
            for segment in segments:
                _hybrid_tts.speak(segment)
                time.sleep(after_delay)
        else:
            _hybrid_tts.speak(str_working)
            time.sleep(after_delay)
            
    except Exception as e:
        ensure_printed(f"TTS 오류: {str(e)}", print_color='red')


def get_available_voices():
    """사용 가능한 음성 목록 반환"""
    return _hybrid_tts.get_available_voices()


def set_voice_config(config: VoiceConfig):
    """음성 설정 변경"""
    _hybrid_tts.set_voice_config(config)


def test_hybrid_tts():
    """하이브리드 TTS 테스트"""
    ensure_printed("🧪 하이브리드 TTS 테스트 시작")
    
    # 사용 가능한 음성 목록 출력
    voices = get_available_voices()
    for method, voice_list in voices.items():
        ensure_printed(f"{method}: {len(voice_list)}개 음성")
        for voice in voice_list[:3]:  # 처음 3개만 출력
            ensure_printed(f"  - {voice.get('name', 'Unknown')}")
    
    # 테스트 음성 재생
    test_text = "안녕하세요, 하이브리드 TTS 테스트입니다"
    ensure_printed(f"🔊 '{test_text}' 재생 중...")
    
    success = _hybrid_tts.speak(test_text)
    
    if success:
        ensure_printed("✅ 하이브리드 TTS 테스트 성공")
    else:
        ensure_printed("❌ 하이브리드 TTS 테스트 실패")
    
    return success


if __name__ == "__main__":
    test_hybrid_tts() 