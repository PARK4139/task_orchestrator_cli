def ensure_spoken(str_working, after_delay=1.00, delimiter=None, voice_config=None, speed_factor=1.30):
    import os
    import json
    import time
    import re
    from datetime import datetime
    from pydub.playback import play
    from pkg_py.functions_split.ensure_elevenlabs_quota_managed import ensure_elevenlabs_quota_managed
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.get_pk_program_language_v2 import get_pk_program_language_v2
    from pkg_py.system_object.directories import D_PKG_SOUND
    from pkg_py.system_object.map_massages import PkMessages2025
    from pkg_py.system_object.files import F_SILENT_MP3
    # WAV 포맷용 silent 파일 경로 정의
    F_SILENT_WAV = os.path.join(D_PKG_SOUND, "silent.wav")
    index_file = os.path.join(D_PKG_SOUND, "index.json")

    def detect_language(text):
        return "english" if re.fullmatch(r"[a-zA-Z0-9\s\.,!?;:'\"()\-]+", text.strip()) else "korean"

    def get_voice_id_by_language(text):
        voice_ids = {
            "english": "EXAVITQu4vr4xnSDxMaL",
            "korean": "21m00Tcm4TlvDq8ikWAM",  # 한글은 gtts 로 한 상태
        }
        return voice_ids.get(detect_language(text), voice_ids["korean"])

    def sanitize_filename(text):
        text = text.strip().replace('\n', ' ')[:30]
        text = re.sub(r'[\\/*?:"<>|]', '_', text)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{timestamp}_{text}.wav"  # MP3 → WAV로 변경

    def load_index():
        if os.path.exists(index_file):
            try:
                with open(index_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                pass
        return {}

    def save_index(index):
        with open(index_file, "w", encoding="utf-8") as f:
            json.dump(index, f, ensure_ascii=False, indent=2)

    def play_audio(wav_path, speed_factor=1.0):
        from pydub import AudioSegment
        from pydub.playback import play
        import os
        
        try:
            ensure_printed(f"🔊 오디오 재생 시작: {os.path.basename(wav_path)}", print_color="blue")
            
            # 한글 앞부분 소리가 먹히는 문제 해결을 위해 silent.wav를 앞에 추가
            if ensure_silent_wav_exists():
                ensure_printed("📝 Silent WAV 적용 중...", print_color="blue")
                
                # silent.wav와 메인 오디오 로드
                silent_audio = AudioSegment.from_wav(F_SILENT_WAV)
                main_audio = AudioSegment.from_wav(wav_path)
                
                # 노이즈 제거 및 볼륨 최적화
                from pydub.effects import normalize
                
                # 볼륨 부스트 최소화 (5dB → 0dB, 증폭 없음)
                # main_audio = main_audio + 0  # 증폭 없음
                ensure_printed("📈 볼륨 부스트 없음 (0dB)", print_color="blue")
                
                # 노이즈 게이트 적용 (낮은 볼륨 제거) - 최대 강화
                noise_threshold = -20  # dB (최대 엄격한 노이즈 제거)
                main_audio = main_audio.apply_gain_stereo(noise_threshold, noise_threshold)
                ensure_printed("🔇 노이즈 게이트 최대 강화 적용 (-20dB)", print_color="blue")
                
                # 속도 조절 (기본 1.0배, 빠르게 하려면 1.2~1.5배)
                if speed_factor != 1.0:
                    main_audio = main_audio.speedup(playback_speed=speed_factor)
                    ensure_printed(f"⚡ 속도 조절: {speed_factor}배", print_color="blue")
                
                # 정규화 (클리핑 방지)
                main_audio = normalize(main_audio)
                ensure_printed("📊 오디오 정규화 완료", print_color="blue")
                
                # silent.wav와 메인 오디오 연결
                combined_audio = silent_audio + main_audio
                ensure_printed("🔗 silent.wav와 메인 오디오 연결됨", print_color="blue")
                
                # pydub로 재생
                play(combined_audio)
                ensure_printed("✅ pydub로 재생 완료 (노이즈 제거)", print_color="green")
                
            else:
                # silent.wav 없으면 원본 파일로 재생 (볼륨 높임)
                ensure_printed("⚠️ Silent WAV 없음, 원본 파일로 재생", print_color="yellow")
                try:
                    # 원본 오디오 로드
                    audio = AudioSegment.from_wav(wav_path)
                    
                    # 노이즈 제거 및 볼륨 최적화
                    from pydub.effects import normalize
                    
                    # 볼륨 부스트 최소화 (5dB → 0dB, 증폭 없음)
                    # audio = audio + 0  # 증폭 없음
                    ensure_printed("📈 볼륨 부스트 없음 (0dB)", print_color="blue")
                    
                    # 노이즈 게이트 적용 (낮은 볼륨 제거) - 최대 강화
                    noise_threshold = -20  # dB (최대 엄격한 노이즈 제거)
                    audio = audio.apply_gain_stereo(noise_threshold, noise_threshold)
                    ensure_printed("🔇 노이즈 게이트 최대 강화 적용 (-20dB)", print_color="blue")
                    
                    # 속도 조절 (기본 1.0배, 빠르게 하려면 1.2~1.5배)
                    if speed_factor != 1.0:
                        audio = audio.speedup(playback_speed=speed_factor)
                        ensure_printed(f"⚡ 속도 조절: {speed_factor}배", print_color="blue")
                    
                    # 정규화 (클리핑 방지)
                    audio = normalize(audio)
                    ensure_printed("📊 오디오 정규화 완료", print_color="blue")
                    
                    # pydub로 재생
                    play(audio)
                    ensure_printed("✅ pydub로 재생 완료 (노이즈 제거)", print_color="green")
                    
                except Exception as e:
                    ensure_printed(f"❌ pydub 재생 실패: {e}", print_color="red")
                
        except Exception as e:
            ensure_printed(f"❌ {PkMessages2025.PLAYBACK_FAILED}: {e}", print_color="red")

    def setup_elevenlabs_api_key():
        config_dir = os.path.join(os.path.expanduser("~"), ".pk_system")
        config_file = os.path.join(config_dir, "elevenlabs_config.json")

        if os.getenv('ELEVENLABS_API_KEY'):
            return os.getenv('ELEVENLABS_API_KEY')

        if os.path.exists(config_file):
            try:
                with open(config_file, 'r') as f:
                    data = json.load(f)
                    key = data.get('api_key')
                    if key:
                        os.environ['ELEVENLABS_API_KEY'] = key
                        return key
            except:
                pass

        key = input(f"🔑 {PkMessages2025.ELEVENLABS_API_KEY_INPUT}: ").strip()
        if key:
            os.makedirs(config_dir, exist_ok=True)
            with open(config_file, "w") as f:
                json.dump({"api_key": key}, f)
            os.environ['ELEVENLABS_API_KEY'] = key
            return key
        return None

    def fetch_tts_with_gtts(text, path):
        """Use gTTS for Korean text with improved quality"""
        try:
            from gtts import gTTS
            # 고품질 설정으로 TTS 생성 (WAV로 변환) - 빠른 속도
            tts = gTTS(text=text, lang='ko', slow=False)  # slow=False로 최대 속도
            # 임시 MP3 파일 생성
            temp_mp3 = path.replace('.wav', '_temp.mp3')
            tts.save(temp_mp3)
            
            # MP3를 WAV로 변환 (고품질)
            from pydub import AudioSegment
            audio = AudioSegment.from_mp3(temp_mp3)
            
            # 고품질 설정으로 변환 (44.1kHz, 16bit, 스테레오)
            high_quality_audio = audio.set_frame_rate(44100).set_sample_width(2).set_channels(2)
            high_quality_audio.export(path, format="wav", parameters=[
                "-ar", "44100",  # 44.1kHz 샘플레이트
                "-ac", "2",      # 스테레오
                "-sample_fmt", "s16"  # 16bit
            ])
            
            # 임시 MP3 파일 삭제
            os.remove(temp_mp3)
            return True
        except Exception as e:
            ensure_printed(f"❌ {PkMessages2025.GTTS_FAILED}: {e}", print_color="red")
            return False

    def fetch_tts_with_elevenlabs(text, path):
        """Use ElevenLabs for English text with improved quality"""
        import requests
        quota = ensure_elevenlabs_quota_managed()
        if not quota.check_quota(len(text)):
            ensure_printed(f"❌ {PkMessages2025.QUOTA_EXCEEDED}", print_color="red")
            return False

        api_key = os.getenv("ELEVENLABS_API_KEY") or setup_elevenlabs_api_key()
        if not api_key:
            return False

        voice_id = get_voice_id_by_language(text)
        headers = {
            "xi-api-key": api_key,
            "Content-Type": "application/json"
        }

        data = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.7,  # 안정성 증가
                "similarity_boost": 0.8,  # 유사성 부스트 증가
                "style": 0.0,
                "use_speaker_boost": True  # 스피커 부스트 활성화
            }
        }

        try:
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
            res = requests.post(url, headers=headers, json=data)
            if res.status_code == 200:
                # 임시 MP3 파일로 저장
                temp_mp3 = path.replace('.wav', '_temp.mp3')
                with open(temp_mp3, "wb") as f:
                    f.write(res.content)
                
                # MP3를 WAV로 변환 (고품질)
                from pydub import AudioSegment
                audio = AudioSegment.from_mp3(temp_mp3)
                
                # 고품질 설정으로 변환 (44.1kHz, 16bit, 스테레오)
                high_quality_audio = audio.set_frame_rate(44100).set_sample_width(2).set_channels(2)
                high_quality_audio.export(path, format="wav", parameters=[
                    "-ar", "44100",  # 44.1kHz 샘플레이트
                    "-ac", "2",      # 스테레오
                    "-sample_fmt", "s16"  # 16bit
                ])
                
                # 임시 MP3 파일 삭제
                os.remove(temp_mp3)
                quota.update_usage(len(text))
                return True
            else:
                ensure_printed(f"❌ {PkMessages2025.API_ERROR}: {res.status_code}", print_color="red")
                return False
        except Exception as e:
            ensure_printed(f"❌ {PkMessages2025.REQUEST_FAILED}: {e}", print_color="red")
            return False

    def fetch_tts_and_save(text, path):
        """Choose TTS method based on language and program setting"""
        # Get program language setting
        program_lang = get_pk_program_language_v2()
        
        # Detect text language
        text_lang = detect_language(text)
        
        # For Korean text, use gTTS regardless of program language
        if text_lang == "korean":
            return fetch_tts_with_gtts(text, path)
        else:
            # For English text, use ElevenLabs
            return fetch_tts_with_elevenlabs(text, path)

    def create_silent_wav():
        """700ms간 소리가 없는 silent.wav 파일을 생성합니다."""
        from pydub import AudioSegment
        
        try:
            # 700ms간 무음 생성 (고품질 설정)
            duration_ms = 700
            
            # 고품질 무음 오디오 세그먼트 생성 (44.1kHz, 16bit, 스테레오)
            silent_audio = AudioSegment.silent(duration=duration_ms, frame_rate=44100)
            silent_audio = silent_audio.set_sample_width(2).set_channels(2)
            
            # silent.wav로 저장 (고품질 설정)
            silent_audio.export(F_SILENT_WAV, format="wav", parameters=[
                "-ar", "44100",  # 44.1kHz 샘플레이트
                "-ac", "2",      # 스테레오
                "-sample_fmt", "s16"  # 16bit
            ])
            ensure_printed(f"✅ Silent WAV 파일이 생성되었습니다: {F_SILENT_WAV}")
            return True
        except Exception as e:
            ensure_printed(f"❌ Silent WAV 파일 생성 실패: {e}", print_color="red")
            return False

    def ensure_silent_wav_exists():
        """silent.wav 파일이 존재하는지 확인하고, 없으면 생성합니다."""
        if not os.path.exists(F_SILENT_WAV):
            os.makedirs(os.path.dirname(F_SILENT_WAV), exist_ok=True)
            return create_silent_wav()
        return True

    if not str_working or not str_working.strip():
        return

    os.makedirs(D_PKG_SOUND, exist_ok=True)
    index = load_index()

    if str_working in index and os.path.exists(index[str_working]):
        play_audio(index[str_working], speed_factor)
        time.sleep(after_delay)
        return

    mp3_filename = sanitize_filename(str_working)
    file_wav = os.path.join(D_PKG_SOUND, mp3_filename)

    success = fetch_tts_and_save(str_working, file_wav)
    if success:
        index[str_working] = file_wav
        save_index(index)
        play_audio(file_wav, speed_factor)
    else:
        ensure_printed(f"❌ {PkMessages2025.TTS_GENERATION_FAILED}", print_color="red")

    time.sleep(after_delay)
