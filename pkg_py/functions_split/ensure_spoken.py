def ensure_spoken(str_working, after_delay=1.00, delimiter=None, voice_config=None):
    """
    ElevenLabs API 기반 TTS 함수 (무료 한도 관리 포함)
    
    Args:
        str_working: 읽을 텍스트
        after_delay: 재생 후 대기 시간
        delimiter: 구분자 (기본값: 쉼표)
        voice_config: 음성 설정 (VoiceConfig 객체)
    """
    # ===== 기존 로직 주석처리 =====
    # from pkg_py.functions_split.ensure_spoken_hybrid import ensure_spoken_hybrid
    # 
    # # 하이브리드 TTS 사용 (SAPI 우선순위)
    # ensure_spoken_hybrid(
    #     str_working=str_working, 
    #     after_delay=after_delay, 
    #     delimiter=delimiter,
    #     voice_config=voice_config
    # )
    # ===== 기존 로직 주석처리 끝 =====

    import os
    import re
    import json
    import requests
    import tempfile
    import subprocess
    import time
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.ensure_elevenlabs_quota_managed import ensure_elevenlabs_quota_managed

    def detect_language(text):
        """
        텍스트 언어 감지
        영어로만 이루어져 있으면 영어로 판단
        """
        # 영어로만 이루어져 있는지 확인 (알파벳, 공백, 구두점, 숫자만)
        english_only_pattern = re.compile(r'^[a-zA-Z\s\.,!?;:\'\"()\-0-9]+$')

        # 텍스트에서 영어가 아닌 문자 확인 (한글, 특수문자 등)
        non_english_chars = re.findall(r'[^a-zA-Z\s\.,!?;:\'\"()\-0-9]', text)

        if len(non_english_chars) == 0 and text.strip():
            return "english"
        else:
            return "korean"

    def get_voice_id_by_language(text):
        """
        언어에 따른 Voice ID 선택 (위치 바뀜)
        """
        language = detect_language(text)

        voice_ids = {
            "english": "EXAVITQu4vr4xnSDxMaL",  # elevenlabs Rachel
            # "english": "LcfcDJNUP1GQjkzn1xUU",   # elevenlabs 에밀리
            "korean": "21m00Tcm4TlvDq8ikWAM",  # 한국어용 Voice ID
        }
        return voice_ids.get(language, voice_ids["korean"])  # 기본값도 한국어용으로 변경

    def setup_elevenlabs_api_key():
        """
        ElevenLabs API 키 설정
        """
        ensure_printed("🔧 ElevenLabs API 키 설정이 필요합니다.", print_color='yellow')

        # 현재 API 키 확인
        current_key = os.getenv('ELEVENLABS_API_KEY')
        if current_key:
            ensure_printed(f" 현재 API 키: {current_key[:10]}...", print_color='cyan')
            return True

        # 설정 파일에서 로드 시도
        config_dir = os.path.join(os.path.expanduser("~"), ".pk_system")
        config_file = os.path.join(config_dir, "elevenlabs_config.json")

        if os.path.exists(config_file):
            try:
                with open(config_file, 'r') as f:
                    config = json.load(f)

                if 'api_key' in config:
                    os.environ['ELEVENLABS_API_KEY'] = config['api_key']
                    ensure_printed("✅ 설정 파일에서 API 키를 로드했습니다.", print_color='green')
                    return True
            except Exception as e:
                ensure_printed(f"❌ 설정 파일 로드 실패: {str(e)}", print_color='red')

        # API 키 입력 요청
        ensure_printed("💡 ElevenLabs API 키를 입력해주세요.", print_color='blue')
        ensure_printed(" https://elevenlabs.io/ 에서 무료 계정을 만들고 API 키를 생성하세요.", print_color='cyan')

        new_key = input("ElevenLabs API 키: ").strip()

        if new_key:
            # 환경변수 설정
            os.environ['ELEVENLABS_API_KEY'] = new_key

            # 설정 파일에 저장 (Voice ID 위치도 바뀜)
            os.makedirs(config_dir, exist_ok=True)
            config = {
                "api_key": new_key,
                "default_voice_id": "EXAVITQu4vr4xnSDxMaL",  # 한국어용으로 변경
                "english_voice_id": "21m00Tcm4TlvDq8ikWAM",
                "model_id": "eleven_monolingual_v1"
            }

            with open(config_file, 'w') as f:
                json.dump(config, f, indent=2)

            ensure_printed("✅ ElevenLabs API 키가 설정되었습니다!", print_color='green')
            return True
        else:
            ensure_printed("❌ API 키가 입력되지 않았습니다.", print_color='red')
            ensure_printed(" 나중에 'python pkg_py/pk_ensure_elevenlabs_api_key_set.py'로 설정할 수 있습니다.", print_color='yellow')
            return False

    def elevenlabs_tts_with_quota(text, api_key=None):
        """
        ElevenLabs API를 사용한 TTS (무료 한도 관리 포함)
        """
        # 언어 감지 및 Voice ID 선택
        language = detect_language(text)
        voice_id = get_voice_id_by_language(text)

        ensure_printed(f"🌐 감지된 언어: {language}", print_color='blue')
        ensure_printed(f"🎤 선택된 Voice ID: {voice_id}", print_color='cyan')

        # 한도 관리자 초기화
        quota_manager = ensure_elevenlabs_quota_managed()

        # 한도 정보 표시
        quota_manager.display_quota_info()

        # 텍스트 길이 계산
        text_length = len(text)

        # 한도 확인
        if not quota_manager.check_quota(text_length):
            ensure_printed("❌ 무료 한도를 초과했습니다.", print_color='red')
            return False

        # API 키 확인
        if not api_key:
            api_key = os.getenv('ELEVENLABS_API_KEY')

        if not api_key:
            ensure_printed("❌ ElevenLabs API 키가 설정되지 않았습니다.", print_color='red')
            if setup_elevenlabs_api_key():
                api_key = os.getenv('ELEVENLABS_API_KEY')
            else:
                return False

        try:
            # ElevenLabs API 호출
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

            headers = {
                "xi-api-key": api_key,
                "Content-Type": "application/json"
            }

            data = {
                "text": text,
                "model_id": "eleven_monolingual_v1",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.75
                }
            }

            ensure_printed("🎵 ElevenLabs TTS 요청 중...", print_color='blue')
            response = requests.post(url, headers=headers, json=data)

            if response.status_code == 200:
                # 임시 파일에 오디오 저장
                with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
                    temp_file.write(response.content)
                    temp_file_path = temp_file.name

                # 오디오 재생
                ensure_printed("🔊 오디오 재생 중...", print_color='green')

                # Windows에서 오디오 재생
                try:
                    subprocess.run(['start', temp_file_path], shell=True, check=True)
                except subprocess.CalledProcessError:
                    # 대안: Python의 playsound 사용
                    try:
                        from playsound import playsound
                        playsound(temp_file_path)
                    except ImportError:
                        ensure_printed("❌ 오디오 재생을 위한 라이브러리가 설치되지 않았습니다.", print_color='red')
                        ensure_printed(" pip install playsound", print_color='yellow')

                # 사용량 업데이트
                quota_manager.update_usage(text_length)

                # 임시 파일 정리
                time.sleep(after_delay)
                try:
                    os.unlink(temp_file_path)
                except:
                    pass

                ensure_printed("✅ TTS 완료!", print_color='green')
                return True

            else:
                ensure_printed(f"❌ ElevenLabs API 오류: {response.status_code}", print_color='red')
                ensure_printed(f" 응답: {response.text}", print_color='red')
                return False

        except Exception as e:
            ensure_printed(f"❌ ElevenLabs TTS 실패: {str(e)}", print_color='red')
            return False

    # 메인 로직
    if not str_working:
        return

    # 텍스트 정리
    cleaned_text = str_working.strip()
    if not cleaned_text:
        return

    # ElevenLabs TTS 실행
    success = elevenlabs_tts_with_quota(cleaned_text)

    if not success:
        ensure_printed("❌ ElevenLabs TTS 실패", print_color='red')
        # 여기서 기존 TTS 시스템으로 폴백할 수 있음
        # ensure_spoken_hybrid(str_working, after_delay, delimiter, voice_config)
