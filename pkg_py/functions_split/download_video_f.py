def download_video_f(url: str):
    from pkg_py.functions_split.cmd_to_os import cmd_to_os
    from pkg_py.functions_split.cmd_to_os_like_person_as_admin import cmd_to_os_like_person_as_admin
    from pkg_py.functions_split.is_pattern_in_prompt import is_pattern_in_prompt
    from pkg_py.functions_split.move_pnx import move_pnx
    from pkg_py.functions_split.parse_youtube_video_id import parse_youtube_video_id
    from pkg_py.functions_split.pk_speak_v2 import pk_speak_v2
    from pkg_py.functions_split.print_magenta import print_magenta
    from pkg_py.pk_interface_graphic_user import GuiUtil
    from pkg_py.pk_system_object.directories import D_DOWNLOADING
    from pkg_py.pk_system_object.files import F_YT_DLP_EXE

    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.pk_system_object.local_test_activate import LTA

    import os
    import traceback

    while 1:
        if url.strip() == "":
            pk_print(f'''  {'%%%FOO%%%' if LTA else ''} {url}" ''', print_color='red')
            break

        pk_print(working_str=rf'''url="{url}"  {'%%%FOO%%%' if LTA else ''}''')

        # 유튜브 다운로더 업데이트 # 다운로드가 안되면 주석 풀어 시도
        # os.system(rf'{YT_DLP_CMD} -U')

        video_id = ''
        # lines=subprocess.check_output(rf'{YT_DLP_CMD} -F {url}', shell=True).decode('utf-8').split("\n")

        cmd = rf'{F_YT_DLP_EXE} -F {url}'
        # lines=cmd_to_os_like_person_as_admin(cmd=cmd)
        lines = cmd_to_os(cmd=cmd)
        # 순서는 우선순위에 입각해 설정되었다. 순서를 바꾸어서는 안된다.

        video_ids_allowed = VIDEO_IDS_ALLOWED
        audio_ids_allowed = AUDIO_IDS_ALLOWED
        audio_id = ""
        for line in lines:
            if 'video only' in line or 'audio only' in line:
                pk_print(line, print_color='blue')
                # video_id 설정
                for id in video_ids_allowed:
                    if id in line:
                        video_id = id
                        if video_id.strip() == "":
                            pk_print(rf"다운로드 할 수 있는 video_id가 아닙니다 {video_id.strip()}", print_color='blue')
                            break
                # audio_id 설정
                for id in audio_ids_allowed:
                    if id in line:
                        audio_id = id
                        if audio_id.strip() == "":
                            pk_print(rf"다운로드 할 수 있는 audio_id가 아닙니다 {audio_id.strip()}", print_color='blue')
                            break
                        break

        # 다운로드 가능 옵션 ID 설정
        # if video_id not in video_ids and audio_id not in audio_ids:
        #     video_id=str(input('video option:'))
        #     audio_id=str(input('audio option:'))
        #     pk_print(rf'video option: {video_id}  audio option: {audio_id}')
        #     speak(rf'video option: {video_id}  audio option: {audio_id}')
        # else:
        #     pass

        # directories=["storage"]
        # for directory in directories:
        #     if not is_d(rf'{os.getcwd()}\{directory}'):
        #         print(rf'storage d 생성 중...')
        #         os.makedirs(rf'{directory}')

        # 2023년 12월 12일 (화) 16:02:06
        # 다운로드의 최고 품질이 아닐 수 있다. 그래도
        # 차선책으로 두는 것이 낫겠다
        # cmd=rf'{YT_DLP_CMD} -f best "{url}"'
        # cmd=rf'{YT_DLP_CMD} -f {video_id}+{audio_id} {url}' # 초기에 만든 선택적인 방식
        # cmd=rf'{YT_DLP_CMD} -f "best[ext=webm]" {url}' # 마음에 안드는 결과
        cmd = rf'{F_YT_DLP_EXE} -f "bestvideo[ext=webm]+bestaudio[ext=webm]" {url}'  # 지금 가장 마음에 드는 방법 근데 webm 없는 경우가 많음
        # cmd=rf'{YT_DLP_CMD} -f "bestvideo[ext=webm]+bestaudio[ext=webm]/best[ext=webm]/best" {url}' # 아직 시도하지 않은 방법
        # cmd=rf'{YT_DLP_CMD} x+x "{url}"' # --list-formats 해서 다운로드
        if video_id == "" or audio_id == "" == 1:
            # text="다운로드를 진행할 수 없습니다\n다운로드용 video_id 와 audio_id를 설정 후\nurl을 다시 붙여넣어 다운로드를 다시 시도하세요\n{url}"
            pk_print(working_str="불완전한 다운로드 명령어가 감지되었습니다....")
            pk_speak_v2(working_str="불완전한 다운로드 명령어가 감지되었습니다", comma_delay=0.98)
            dialog = GuiUtil.CustomQdialog(
                prompt=f"에러코드[E004]\n아래의 비디오 아이디를 저장하고 에러코드를 관리자에게 문의해주세요\nvideo id: {url}",
                btn_list=["확인"],
                input_box_mode=True,
                input_box_text_default=url,
            )
            dialog.exec()
            print(cmd)
            break

        try:
            lines = cmd_to_os_like_person_as_admin(cmd=cmd)
        except:
            print_magenta("except:2024-04-12 1750")
            print_magenta(rf'''cmd : {cmd}''')

        if not os.path.exists(D_DOWNLOADING):
            os.makedirs(D_DOWNLOADING)

        pk_print(working_str="다운로드 f 이동 시도 중...")
        file = ""
        try:
            clip_id = parse_youtube_video_id(url)
            if clip_id is None:
                clip_id = url

            lines = os.listdir()
            for line in lines:
                if is_pattern_in_prompt(str(line), str(clip_id)):
                    file = line

            src = os.path.abspath(file)
            src_renamed = rf"{D_DOWNLOADING}\{os.path.basename(file)}"

            pk_print(f'src_renamed : {src_renamed}', print_color='blue')
            if src == os.getcwd():  # 여기 또 os.getcwd() 있는 부분 수정하자..
                # E001 : exec 불가능한 명령어입력 감지
                # S001 : 다운로드 가능한 video_id 와 audio_id 를 가용목록에 추가해주세요.
                dialog = GuiUtil.CustomQdialog(
                    prompt=f"에러코드[E001]\n아래의 비디오 아이디를 저장하고 에러코드를 관리자에게 문의해주세요\nvideo id: {url}",
                    btn_list=["확인"],
                    input_box_mode=True,
                    input_box_text_default=url, )
                dialog.exec()
                pk_print("cmd", print_color='blue')
                pk_print(cmd, print_color='blue')
                break
            # shutil.move(src, storage)
            if src != os.getcwd():  # 여기 또 os.getcwd() 있는 부분 수정하자..
                move_pnx(src, src_renamed)

        except:
            pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        print(rf'다운로드 결과 확인 중...')
        try:
            src_moved = rf'{D_DOWNLOADING}\{file}'
            pk_print(rf'''src_moved : {src_moved}''', print_color='blue')

            # 재생할까요? 불필요하면 주석
            # dialog=GuiUtil.CustomQdialog(ment="다운로드된 영상을 재생할까요?", btns=["재생하기", "재생하지 않기"], auto_click_negative_btn_after_seconds=10)
            # dialog=GuiUtil.CustomQdialog(ment="다운로드된 영상을 재생할까요?", btns=["재생하기", "재생하지 않기"], auto_click_negative_btn_after_seconds=3600)
            # dialog.exec()
            # if dialog.btn_txt_clicked == "재생하기":
            #     open_pnx(pnx_todo=src_moved)

            # 무조건 재생
            text_editor = 'explorer.exe'
            cmd = f'{text_editor} "{src_moved}" '
            cmd_to_os(cmd=cmd)

            # GuiUtil.pop_up_as_complete(title="작업성공보고", ment=f"다운로드가 성공되었습니다\n{src_moved}", auto_click_positive_btn_after_seconds=2) # 성공 뜨는게 귀찮아서 주석처리함,

        except Exception:
            pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

        # 다운로드 로깅 처리
        # cmd=f'echo "{url}" >> success_yt_dlp.log'
        # run_via_cmd_exe(cmd=cmd)
        break
