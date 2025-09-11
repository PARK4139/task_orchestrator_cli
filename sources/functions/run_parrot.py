from sources.objects.pk_local_test_activate import LTA
import logging


def run_parrot():
    import traceback
    import speech_recognition as sr

    recognizer = sr.Recognizer()
    logging.debug_and_speak("저는 따라쟁이 앵무새 parrot 입니다")
    while 1:
        try:
            logging.debug("말씀해주세요")
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
            str_prompt = recognizer.recognize_google(audio, language="ko")
            logging.debug_and_speak(rf"{str_prompt}")
        except sr.UnknownValueError:
            pass
        except OSError:
            logging.debug(f'''마이크 장비가 없습니다" ''')
            break
        except:
            logging.debug(f'''"음성 인식 서비스에 오류가 발생했습니다"" ''')
            logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
