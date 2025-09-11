from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_spoken_and_slept_for_playing_length(text):
    from functions.ensure_spoken import ensure_spoken
    from functions.ensure_slept import ensure_slept
    from functions.get_tts_cache_file_play_length_milliseconds import get_tts_cache_file_play_length_milliseconds

    ensure_spoken(text)
    ensure_slept(milliseconds=get_tts_cache_file_play_length_milliseconds(text))
