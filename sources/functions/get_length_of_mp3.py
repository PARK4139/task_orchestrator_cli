def get_length_of_mp3(f: str):
    import logging
    from sources.objects.pk_local_test_activate import LTA

    import traceback

    import mutagen
    try:
        from mutagen.mp3 import MP3
        audio = MP3(f)
        return audio.info.length
    except mutagen.MutagenError:
        # logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")   # gtts 모듈 불능? mutagen 모듈 불능? license 찾아보자 으로 어쩔수 없다.
        return
    except Exception:
        logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
