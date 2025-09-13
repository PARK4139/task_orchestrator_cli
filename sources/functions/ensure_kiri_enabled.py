from functions.get_wsl_distro_config import get_wsl_distro_config


def ensure_kiri_ran():

    from sources.functions.ensure_pnx_backed_up import ensure_pnx_backed_up
    from sources.functions.cmd_f_in_cmd_exe_like_human import cmd_f_in_cmd_exe_like_human
    from sources.functions.download_youtube_thumbnails_from_youtube_channel_main_page_url import download_youtube_thumbnails_from_youtube_channel_main_page_url
    from sources.functions.empty_recycle_bin import empty_recycle_bin
    from sources.functions.ensure_work_directory_created import ensure_work_directory_created
    from functions.ensure_guided_not_prepared_yet import ensure_not_prepared_yet_guided
    from sources.functions.ensure_python_pkg_to_remote_os import ensure_python_pkg_to_remote_os
    from sources.functions.ensure_sound_track_played import ensure_sound_track_played
    from sources.functions.ensure_todo_list_guided import ensure_todo_list_guided
    from sources.functions.get_comprehensive_weather_information_from_web import get_comprehensive_weather_information_from_web
    from sources.functions.get_element_random import get_element_random
    from sources.functions.get_weekday import get_weekday
    from sources.functions.is_internet_connected import is_internet_connected
    from sources.functions.is_mic_device_connected import is_mic_device_connected
    from sources.functions.make_version_new import make_version_new
    from sources.functions.move_f_via_telegram_bot_v2 import move_f_via_telegram_bot_v2
    from sources.functions.play_my_video_track import play_my_video_track
    from sources.functions.ensure_py_system_processes_restarted import ensure_py_system_processes_restarted
    from sources.functions.run_up_and_down_game import run_up_and_down_game
    from sources.functions.ensure_power_saved_as_s4 import ensure_power_saved_as_s4
    from sources.functions.ensure_screen_saved import ensure_screen_saved
    from sources.functions.speak_today_info_as_korean import speak_today_info_as_korean
    from sources.objects.task_orchestrator_cli_directories import D_ARCHIVED

    from sources.functions.ensure_command_executed import ensure_command_executed
    from sources.functions.is_os_windows import is_os_windows
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
    from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING

    import logging

    from functions.ensure_wsl_distro_enabled import ensure_wsl_distro_enabled
    from functions.ensure_wsl_distro_session import ensure_wsl_distro_session
    from objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI
    from sources.objects.pk_local_test_activate import LTA

    import random
    import traceback
    import speech_recognition as sr

    # ensure wsl
    wsl_distro_config = get_wsl_distro_config()

    ensure_wsl_distro_enabled(distro_name=wsl_distro_config.distro_name)
    ensure_wsl_distro_session(distro_name=wsl_distro_config.distro_name)

    ensure_python_pkg_to_remote_os(py_pkg_n='SpeechRecognition', **wsl_distro_config)
    ensure_python_pkg_to_remote_os(py_pkg_n='PyAudio', **wsl_distro_config)

    # ensure_general_ubuntu_pkg()
    # mpg123 을 wsl 에 install 해서 써볼까? mpg123은 제어가 쉬울지도
    # ensure_distro_pkg_installed_to_remote_os(ubuntu_pkg_n='mpg123', ** wsl_distro_config)

    if not is_os_windows():
        cmd = 'sudo apt install mpg123'
        ensure_command_executed(cmd=cmd)

    if is_internet_connected():
        # recognizer=sr.Recognizer()
        # with sr.Microphone() as source:
        #     logging.debug("음성을 말하세요...")
        #     recognizer.adjust_for_ambient_noise(source)
        #     audio=recognizer.listen(source)
        pass
    else:
        # # CMU Sphinx로 음성 인식 (오프라인 사용 가능)
        # try:
        #     speak("음성을 인식 중...")
        #     text=recognizer.recognize_sphinx(audio)
        #     speak("인식된 텍스트: " + text)
        # except sr.UnknownValueError:
        #     speak("음성을 이해할 수 없습니다.")
        # except sr.RequestError as e:
        #     speak(f"음성 인식 서비스에 오류가 발생했습니다: {e}")
        pass

    # speak_like_parrot("테스트입니다")

    # os.system(rf"mpg123 ./{temp_mp3}")  # Linux 재생 명령
    # os.system(rf"start {temp_mp3}")  # Windows용 재생 명령

    recognizer = None
    if is_mic_device_connected():
        logging.debug(f'''mic is connected. {'%%%FOO%%%' if LTA else ''}''')
        recognizer = sr.Recognizer()
    else:
        logging.debug(f'''mic is disconnected. {'%%%FOO%%%' if LTA else ''}''')

    loop_cnt = 0
    while 1:
        if loop_cnt == 0:
            ice_breaking_ments = [
                "hello! i am mini, i am ready to assist",
                "Hello! How can I assist you today?",
                "",
            ]
            ice_breaking_ment = get_element_random(working_list=ice_breaking_ments)
            logging.debug_and_spoken(ice_breaking_ment)
        if loop_cnt % 11 == 0:
            ice_breaking_ments = [
                "please. give a command.",
                "i am boring. give a command."
                "i am boring. give a something."
                # get_str_today_day_info(),
            ]
            ice_breaking_ment = get_element_random(working_list=ice_breaking_ments)
            logging.debug_and_spoken(ice_breaking_ment)

        try:
            if str_working is None:
                with sr.Microphone() as source:
                    # recognizer.adjust_for_ambient_noise(source, duration=1.0)  # 주변 소음 보정 # adjust_for_ambient_noise no attribution
                    while 1:
                        try:
                            logging.debug("지금 말씀하실것을 추천드립니다.")
                            # audio = recognizer.listen(source, phrase_time_limit=10)  # 음성 듣기
                            str_working = recognizer.recognize_google(audio, language="ko")  # Google STT
                            break
                        except sr.UnknownValueError:
                            logging.debug(f"UnknownValueError {str_working}")
                        except sr.RequestError as e:
                            logging.debug(f"Google Speech Recognition service access")
            str_working = str_working.replace(' ', '')
            logging.debug(rf"{str_working}")
            if any(keyword in str_working for keyword in ["ipdb"]):
                import ipdb
                ipdb.set_trace()
            elif any(keyword in str_working for keyword in ["테스트", "test"]):
                ensure_not_prepared_yet_guided()
            elif any(keyword in str_working for keyword in ["휴지통비워", "휴지통정리", "empty_trash_bin"]):
                empty_recycle_bin()
                logging.debug_and_spoken("I have emptied the trash bin")
            elif any(keyword in str_working for keyword in ["플레인", "플래인"]):
                logging.debug_and_spoken("yes. i am here")
            elif any(keyword in str_working for keyword in ["영어공부"]):
                logging.debug_and_spoken("What is the weather like?")
                ensure_slept(seconds=random.randint(a=200, b=500))
                logging.debug_and_spoken(
                    "I can't directly access weather information, but if you share your location, I can guide you!")
                ensure_slept(seconds=random.randint(a=200, b=500))
                logging.debug_and_spoken("Quit")
                ensure_slept(seconds=random.randint(a=200, b=500))
                logging.debug_and_spoken("Ending the conversation. Goodbye!")
            elif any(keyword in str_working for keyword in ["업무_d_생성", '업무_d_']):
                # ensure_directory_created_with_timestamp(d_nx=rf"생산관리", dst=rf"{D_PK_WORKING}")
                ensure_work_directory_created()
            elif any(keyword in str_working for keyword in ["sound interactive mode"]):
                # ensure_todo_list_guided(days=1)  # todo : add : 등록된 스케쥴시간확인
                logging.debug("Please give a cmd")
                # print_and_speak("시키실 일 없으신가요.", after_delay=1.0) #random
                with sr.Microphone() as source:
                    # recognizer.adjust_for_ambient_noise(source)
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    # audio=recognizer.listen(source, time_limit=15, phrase_time_limit=10)
                    audio = recognizer.listen(source,
                                              phrase_time_limit=10)  # phrase_time_limit: Limit the maximum length of a phrase.
                    str_working = recognizer.recognize_google(audio, language="ko")
            elif any(keyword in str_working for keyword in ["버전자동업데이트", '버저닝']):
                make_version_new(via_f_txt=True)
            elif any(keyword in str_working for keyword in ["프로젝트백업", "백업", "백업해라"]):

                ensure_py_system_processes_restarted([rf"{D_TASK_ORCHESTRATOR_CLI_RESOURCES}/pk_kill_cmd_exe.py"])
            elif any(keyword in str_working for keyword in ["프로젝트백업", "백업", "백업해라"]):

                ensure_py_system_processes_restarted([rf"{D_TASK_ORCHESTRATOR_CLI_RESOURCES}/pk_back_up_project.py"])
            elif any(keyword in str_working for keyword in ["텔레그램으로 백업"]):
                import nest_asyncio
                import asyncio
                f = ensure_pnx_backed_up(pnx_working=D_TASK_ORCHESTRATOR_CLI, d_dst=D_ARCHIVED)
                nest_asyncio.apply()
                # asyncio.run(send_f_via_telegram_bot(f)) #  --> limit discovered : 단일파일 50MB 이상은 전송 불가 --> send_f_via_telegram_bot_v2(f)
                # send_f_via_telegram_bot_v2(f) # -->  fail --> timeout
                asyncio.run(move_f_via_telegram_bot_v2(f))  # -->
                # change_os_mode_to_power_saving_mode_as_s4()
                return  # return is necceary code, 처리 안시키면 PC 부팅 시 최대절전모드로 무한 진입, 컴퓨터 전원 재연결해야 된다 -> keyword = '' and use continue -> 시도하면 아마될듯
                keyword = ''
                continue
            elif any(keyword in str_working for keyword in ["퇴근해", "자자"]):

                ensure_py_system_processes_restarted([rf"{D_TASK_ORCHESTRATOR_CLI_RESOURCES}/pk_자자.py"])
                keyword = ''
                continue
            elif any(keyword in str_working for keyword in ["트리정리"]):

                ensure_py_system_processes_restarted([rf"{D_TASK_ORCHESTRATOR_CLI_RESOURCES}/pk_ensure_tree_organized.py"])
                keyword = ''
                continue
            elif any(keyword in str_working for keyword in ["피케이"]):
                cmd_f_in_cmd_exe_like_human(cmd_prefix='python', f=rf"{D_TASK_ORCHESTRATOR_CLI}/ensure_task_orchestrator_cli_started")
            elif any(keyword in str_working for keyword in ["할일", "스케쥴러", "스케쥴가이드"]):
                ensure_todo_list_guided()
            elif any(keyword in str_working for keyword in ["토렌트", "토렌트다운로드"]):
                pass
            elif any(keyword in str_working for keyword in ["유튜브다운로드"]):
                pass
            elif any(keyword in str_working for keyword in ["youtube channel download", "유튜브채널다운로드"]):
                pass
            elif any(keyword in str_working for keyword in
                     ["ytctd", "youtube channel thumbnail download", "유튜브채널썸네일다운로드"]):
                youtube_channel_main_page_url = input('youtube_channel_main_page_url=')
                youtube_channel_main_page_url = youtube_channel_main_page_url.strip()
                download_youtube_thumbnails_from_youtube_channel_main_page_url(youtube_channel_main_page_url)
            elif any(keyword in str_working for keyword in ["오늘무슨날", "무슨날"]):
                ensure_spoken('today is christmas. happy christmas')
                ensure_spoken('today is newyear')
            elif any(keyword in str_working for keyword in ["오늘날짜", "날짜"]):
                speak_today_info_as_korean()
            elif any(keyword in str_working for keyword in ["요일", "오늘요일", "몇요일"]):
                ensure_spoken(f'{get_weekday()}')
            elif any(keyword in str_working for keyword in ["시간", "몇시야", "몇시"]):
                HH = get_time_as_('%H')
                mm = get_time_as_('%M')
                ensure_spoken(f'{int(HH)} hour {int(mm)} minutes')
            elif any(keyword in str_working for keyword in ["몇분이야", "몇분", "몇분"]):
                mm = get_time_as_('%M')
                ensure_spoken(f'{int(mm)} minutes')
            elif any(keyword in str_working for keyword in ["몇초야", "몇초"]):
                server_seconds = get_time_as_('%S')
                ensure_spoken(f'{server_seconds} seconds')
            elif any(keyword in str_working for keyword in ["날씨"]):
                logging.debug_and_spoken("Searching for weather...")
                get_comprehensive_weather_information_from_web()
            elif any(keyword in str_working for keyword in ["음악"]):
                ensure_sound_track_played()
                logging.debug_and_spoken("Playing music...")
            elif any(keyword in str_working for keyword in ["게임", "미니게임"]):
                run_up_and_down_game()
                logging.debug_and_spoken("Playing mini game...")
            elif any(keyword in str_working for keyword in ["exit"]):
                raise
            elif any(keyword in str_working for keyword in ["비디오"]):
                play_my_video_track()
                logging.debug_and_spoken("Playing video...")
            elif any(keyword in str_working for keyword in ["최대절전모드", "powersave", "sleep"]):
                ensure_power_saved_as_s4()
                return  # return is necceary code, 처리 안시키면 PC 부팅 시 최대절전모드로 무한 진입, 컴퓨터 전원 재연결해야 된다.
            elif any(keyword in str_working for keyword in ["화면보호기", "화면보호"]):
                ensure_screen_saved()
            else:
                logging.debug(rf"it was Unknown command")  # woas
        except:
            logging.debug_and_spoken(f'''{__file__} 코드 exec 중 오류가 발생했습니다" ''')
            logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
            if not is_mic_device_connected():
                logging.debug(f'''mic is disconnected. {'%%%FOO%%%' if LTA else ''}''')
        loop_cnt += 1
        ensure_slept(milliseconds=200)
