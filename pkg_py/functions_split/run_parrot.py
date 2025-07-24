from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def run_parrot():
    import traceback
    import speech_recognition as sr

    recognizer = sr.Recognizer()
    pk_print_and_speak("저는 따라쟁이 앵무새 parrot 입니다")
    while 1:
        try:
            pk_print(str_working="말씀해주세요", print_color='blue')
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
            str_prompt = recognizer.recognize_google(audio, language="ko")
            pk_print_and_speak(rf"{str_prompt}")
        except sr.UnknownValueError:
            pass
        except OSError:
            pk_print(f'''마이크 장비가 없습니다" ''', print_color='red')
            break
        except:
            pk_print(f'''"음성 인식 서비스에 오류가 발생했습니다"" ''', print_color='red')
            pk_print(f"{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}", print_color='red')
