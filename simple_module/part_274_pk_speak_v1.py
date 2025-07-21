from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style


def pk_speak_v1(working_str, after_delay=1.00, delimiter=None):
    # 최적화 필요
    # 많이 쓸 수록 프로그램이 느려진다
    import os
    import traceback
    import pyglet

    if not delimiter:
        delimiter = ','  # , 를 넣으면 나누어 읽도록 업데이트
    working_str = str(working_str)
    working_str = working_str.strip()
    if is_containing_special_characters(text=working_str):
        working_str = remove_special_characters(text=working_str)
    if working_str == "":
        return None
    try:
        while 1:
            working_list = []
            if LTA:
                pk_print(f'''working_list={working_list} {'%%%FOO%%%' if LTA else ''}''')
            if delimiter in working_str:
                working_list = working_str.split(delimiter)
                for working_str in working_list:
                    pk_speak_v2(working_str=working_str, comma_delay=0.98)
                break
            if type(working_str) == str:
                cache_mp3 = get_pnx_os_style(rf'{D_PROJECT}/pkg_mp3')
                ment__mp3 = get_pnx_os_style(rf'{cache_mp3}/{working_str}_.mp3')
                ment_mp3 = get_pnx_os_style(rf'{cache_mp3}/{working_str}.mp3')

                ensure_pnx_made(pnx=cache_mp3, mode="d")

                # "ment 전처리, 윈도우 경로명에 들어가면 안되는 문자들 공백으로 대체"
                working_str = get_str_replaced_special_characters(target=working_str, replacement=" ")
                working_str = working_str.replace("\n", " ")

                # f 없으면 생성
                if not os.path.exists(ment_mp3):
                    if not os.path.exists(ment__mp3):
                        from gtts import gTTS
                        if "special_characters" in what_does_this_consist_of(text=working_str):
                            gtts = gTTS(text=working_str, lang='ko')
                            gtts.save(ment__mp3)
                        elif "kor" in what_does_this_consist_of(text=working_str):
                            gtts = gTTS(text=working_str, lang='ko')
                            gtts.save(ment__mp3)
                        elif "eng" in what_does_this_consist_of(text=working_str):
                            gtts = gTTS(text=working_str, lang='en')
                            gtts.save(ment__mp3)
                        elif "jpn" in what_does_this_consist_of(text=working_str):
                            gtts = gTTS(text=working_str, lang='ja')
                            gtts.save(ment__mp3)
                        else:
                            gtts = gTTS(text=working_str, lang='ko')
                            gtts.save(ment__mp3)
                try:
                    silent_mp3 = F_SILENT_MP3
                    if not os.path.exists(silent_mp3):
                        pk_print(working_str="사일런트 mp3 f이 없습니다", print_color='red')
                        break
                    if not os.path.exists(ment_mp3):
                        cmd = rf'echo y | "ffmpeg" -i "concat:{os.path.abspath(silent_mp3)}|{os.path.abspath(ment__mp3)}" -acodec copy -metadata "title=Some Song" "{os.path.abspath(ment_mp3)}" -map_metadata 0:-1  >nul 2>&1'
                        cmd_to_os(cmd)
                except Exception:
                    pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
                try:
                    ment_mp3 = os.path.abspath(ment_mp3)
                    try:
                        source = pyglet.media.load(ment_mp3)
                        source.play()

                        length_of_mp3 = get_length_of_mp3(ment_mp3)
                        pk_sleep(seconds=length_of_mp3 * after_delay)
                        return length_of_mp3
                    except FileNotFoundError:
                        pk_print(f"{ment_mp3} 재생할 f이 없습니다")
                    except:
                        pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
                        break
                    pk_print("before_mp3_length_used_in_speak_as_async 업데이트")
                    length_of_mp3 = round(float(get_length_of_mp3(ment_mp3)), 1)
                    PREVIOUS_MP3_LENGTH_USED_IN_SPEAK_AS_ASYNC = length_of_mp3
                except Exception:
                    pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

                os.system(f'echo y | del /f "{ment__mp3}" >nul 2>&1')
                pk_print(f"TTS 재생시도")
            break
    except Exception:
        pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
