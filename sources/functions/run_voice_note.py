from tkinter import UNDERLINE
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE

from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from tkinter import UNDERLINE

from sources.objects.pk_local_test_activate import LTA
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from sources.objects.encodings import Encoding
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
import logging
from sources.functions.does_pnx_exist import is_pnx_existing


def run_voice_note():
    import traceback
    import speech_recognition as sr

    f_txt = rf"{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}/voice_memo.txt"

    f_txt = get_pnx_unix_style(pnx=f_txt)
    if not is_pnx_existing(pnx=f_txt):
        ensure_pnx_made(pnx=f_txt, mode='f')

    ensure_str_writen_to_f(msg=f"{PK_UNDERLINE}{get_time_as_('now')}\n", f=f_txt)

    f_txt = get_pnx_windows_style(pnx=f_txt)
    cmd = rf"explorer {f_txt}"
    ensure_command_executed(cmd=cmd, mode='a')

    logging.debug_and_speak("저는 텍스트f에 받아쓰는 음성메모장 voice_note 입니다")
    recognizer = sr.Recognizer()

    while 1:
        try:
            logging.debug_and_speak("말씀해주세요")
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
            str_prompt = recognizer.recognize_google(audio, language="ko")
            logging.debug_and_speak(rf"{str_prompt}")

            # 텍스트를 f에 저장
            with open(file=rf"{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}/voice_memo.txt", mode="a", encoding=Encoding.UTF8.value) as file:
                file.write(str_prompt + "\n")
        except sr.UnknownValueError:
            pass  # 음성을 인식하지 못한 경우 무시
        except OSError:
            logging.debug(f'''마이크 장비가 없습니다" ''')
            break
        except:
            logging.debug(f'''"음성 인식 서비스에 오류가 발생했습니다"" ''')
            logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
