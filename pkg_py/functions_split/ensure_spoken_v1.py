from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.directories  import D_PROJECT
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style


def ensure_spoken_v1(str_working, after_delay=1.00, delimiter=None):
    # 최적화 필요
    # 많이 쓸 수록 프로그램이 느려진다
    import os
    import traceback
    import pyglet

    if not delimiter:
        delimiter = ','  # , 를 넣으면 나누어 읽도록 업데이트
    str_working = str(str_working)
    str_working = str_working.strip()
    if is_containing_special_characters(text=str_working):
        str_working = remove_special_characters(text=str_working)
    if str_working == "":
        return None
    try:
        while 1:
            working_list = []
            if LTA:
                ensure_printed(f'''working_list={working_list} {'%%%FOO%%%' if LTA else ''}''')
            if delimiter in str_working:
                working_list = str_working.split(delimiter)
                for str_working in working_list:
                    ensure_spoken_v2(str_working=str_working, comma_delay=0.98)
                break
            if type(str_working) == str:
                cache_mp3 = get_pnx_os_style(rf'{D_PROJECT}/pkg_image_and_video_and_sound')
                ment__mp3 = get_pnx_os_style(rf'{cache_mp3}/{str_working}_.mp3')
                ment_mp3 = get_pnx_os_style(rf'{cache_mp3}/{str_working}.mp3')

                ensure_pnx_made(pnx=cache_mp3, mode="d")

                # "ment 전처리, 윈도우 경로명에 들어가면 안되는 문자들 공백으로 대체"
                str_working = get_str_replaced_special_characters(target=str_working, replacement=" ")
                str_working = str_working.replace("\n", " ")

                # f 없으면 생성
                if not os.path.exists(ment_mp3):
                    if not os.path.exists(ment__mp3):
                        from gtts import gTTS
                        if "special_characters" in what_does_this_consist_of(text=str_working):
                            gtts = gTTS(text=str_working, lang='ko')
                            gtts.save(ment__mp3)
                        elif "kor" in what_does_this_consist_of(text=str_working):
                            gtts = gTTS(text=str_working, lang='ko')
                            gtts.save(ment__mp3)
                        elif "eng" in what_does_this_consist_of(text=str_working):
                            gtts = gTTS(text=str_working, lang='en')
                            gtts.save(ment__mp3)
                        elif "jpn" in what_does_this_consist_of(text=str_working):
                            gtts = gTTS(text=str_working, lang='ja')
                            gtts.save(ment__mp3)
                        else:
                            gtts = gTTS(text=str_working, lang='ko')
                            gtts.save(ment__mp3)
                try:
                    silent_mp3 = F_SILENT_MP3
                    if not os.path.exists(silent_mp3):
                        ensure_printed(str_working="사일런트 mp3 f이 없습니다", print_color='red')
                        break
                    if not os.path.exists(ment_mp3):
                        cmd = rf'echo y | "ffmpeg" -i "concat:{os.path.abspath(silent_mp3)}|{os.path.abspath(ment__mp3)}" -acodec copy -metadata "title=Some Song" "{os.path.abspath(ment_mp3)}" -map_metadata 0:-1  >nul 2>&1'
                        ensure_command_excuted_to_os(cmd)
                except Exception:
                    ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
                try:
                    ment_mp3 = os.path.abspath(ment_mp3)
                    try:
                        source = pyglet.media.load(ment_mp3)
                        source.play()

                        length_of_mp3 = get_length_of_mp3(ment_mp3)
                        ensure_slept(seconds=length_of_mp3 * after_delay)
                        return length_of_mp3
                    except FileNotFoundError:
                        ensure_printed(f"{ment_mp3} 재생할 f이 없습니다")
                    except:
                        ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
                        break
                    ensure_printed("before_mp3_length_used_in_speak_as_async 업데이트")
                    length_of_mp3 = round(float(get_length_of_mp3(ment_mp3)), 1)
                    PREVIOUS_MP3_LENGTH_USED_IN_SPEAK_AS_ASYNC = length_of_mp3
                except Exception:
                    ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

                os.system(f'echo y | del /f "{ment__mp3}" >nul 2>&1')
                ensure_printed(f"TTS 재생시도")
            break
    except Exception:
        ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
