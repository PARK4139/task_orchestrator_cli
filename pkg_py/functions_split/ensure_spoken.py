def ensure_spoken(str_working, after_delay=1.00, delimiter=None, voice_config=None):
    import os
    import json
    import time
    import re
    from datetime import datetime
    from pydub.playback import play
    from pkg_py.functions_split.ensure_elevenlabs_quota_managed import ensure_elevenlabs_quota_managed
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.directories import D_PKG_SOUND
    index_file = os.path.join(D_PKG_SOUND, "index.json")

    def detect_language(text):
        return "english" if re.fullmatch(r"[a-zA-Z0-9\s\.,!?;:'\"()\-]+", text.strip()) else "korean"

    def get_voice_id_by_language(text):
        voice_ids = {
            "english": "EXAVITQu4vr4xnSDxMaL",
            "korean": "21m00Tcm4TlvDq8ikWAM",  # 한글은 gtts 가 나을수도.
        }
        return voice_ids.get(detect_language(text), voice_ids["korean"])

    def sanitize_filename(text):
        text = text.strip().replace('\n', ' ')[:30]
        text = re.sub(r'[\\/*?:"<>|]', '_', text)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{timestamp}_{text}.mp3"

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

    def play_audio(mp3_path):
        from pydub import AudioSegment
        from pkg_py.functions_split.ensure_ffmpeg_installed_to_pkg_windows import ensure_ffmpeg_installed_to_pkg_windows
        try:
            ffmpeg_path, ffprobe_path = ensure_ffmpeg_installed_to_pkg_windows()
            if ffmpeg_path and ffprobe_path:
                AudioSegment.converter = ffmpeg_path
                AudioSegment.ffprobe = ffprobe_path

            sound = AudioSegment.from_file(mp3_path, format="mp3")
            play(sound)
        except Exception as e:
            ensure_printed(f"❌ 재생 실패: {e}", print_color="red")

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

        key = input("🔑 ElevenLabs API 키 입력: ").strip()
        if key:
            os.makedirs(config_dir, exist_ok=True)
            with open(config_file, "w") as f:
                json.dump({"api_key": key}, f)
            os.environ['ELEVENLABS_API_KEY'] = key
            return key
        return None

    def fetch_tts_and_save(text, path):
        import requests
        quota = ensure_elevenlabs_quota_managed()
        if not quota.check_quota(len(text)):
            ensure_printed("❌ 한도 초과", print_color="red")
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
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
        }

        try:
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
            res = requests.post(url, headers=headers, json=data)
            if res.status_code == 200:
                with open(path, "wb") as f:
                    f.write(res.content)
                quota.update_usage(len(text))
                return True
            else:
                ensure_printed(f"❌ API 오류: {res.status_code}", print_color="red")
                return False
        except Exception as e:
            ensure_printed(f"❌ 요청 실패: {e}", print_color="red")
            return False

    if not str_working or not str_working.strip():
        return

    os.makedirs(D_PKG_SOUND, exist_ok=True)
    index = load_index()

    if str_working in index and os.path.exists(index[str_working]):
        play_audio(index[str_working])
        time.sleep(after_delay)
        return

    mp3_filename = sanitize_filename(str_working)
    file_mp3 = os.path.join(D_PKG_SOUND, mp3_filename)

    success = fetch_tts_and_save(str_working, file_mp3)
    if success:
        index[str_working] = file_mp3
        save_index(index)
        play_audio(file_mp3)
    else:
        ensure_printed("❌ TTS 생성 실패", print_color="red")

    time.sleep(after_delay)
