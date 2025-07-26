from tkinter import UNDERLINE
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories import D_PKG_TXT

from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from tkinter import UNDERLINE

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.directories import D_PKG_TXT
from pkg_py.system_object.encodings import Encoding
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def run_voice_note():
    import traceback
    import speech_recognition as sr

    f_txt = rf"{D_PKG_TXT}/voice_memo.txt"

    f_txt = get_pnx_unix_style(pnx=f_txt)
    if not does_pnx_exist(pnx=f_txt):
        ensure_pnx_made(pnx=f_txt, mode='f')

    ensure_str_writen_to_f(msg=f"{PK_UNDERLINE}{get_time_as_('now')}\n", f=f_txt)

    f_txt = get_pnx_windows_style(pnx=f_txt)
    cmd = rf"explorer {f_txt}"
    cmd_to_os(cmd=cmd, mode='a')

    ensure_printed_and_speak("저는 텍스트f에 받아쓰는 음성메모장 voice_note 입니다")
    recognizer = sr.Recognizer()

    while 1:
        try:
            ensure_printed_and_speak("말씀해주세요", print_color='blue')
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
            str_prompt = recognizer.recognize_google(audio, language="ko")
            ensure_printed_and_speak(rf"{str_prompt}")

            # 텍스트를 f에 저장
            with open(file=rf"{D_PKG_TXT}/voice_memo.txt", mode="a", encoding=Encoding.UTF8.value) as file:
                file.write(str_prompt + "\n")
        except sr.UnknownValueError:
            pass  # 음성을 인식하지 못한 경우 무시
        except OSError:
            ensure_printed(f'''마이크 장비가 없습니다" ''', print_color='red')
            break
        except:
            ensure_printed(f'''"음성 인식 서비스에 오류가 발생했습니다"" ''', print_color='red')
            ensure_printed(f"{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}", print_color='red')
