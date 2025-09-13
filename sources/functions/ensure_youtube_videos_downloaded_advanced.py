import logging
import os
import sys
import textwrap
from pathlib import Path

from functions.backup_successful_cookies import backup_successful_cookies
from functions.ensure_youtube_cookies_created import ensure_youtube_cookies_created
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.ensure_pnx_made import ensure_pnx_made
from sources.functions.ensure_pnx_opened_by_ext import ensure_pnx_opened_by_ext
from sources.functions.ensure_seconds_measured import ensure_seconds_measured
from sources.functions.ensure_ubuntu_pkg_enabled import ensure_ubuntu_pkg_enabled
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.get_historical_list import get_historical_list
from sources.functions.get_p import get_p
from sources.functions.get_pnx_ubuntu_pkg_enabled import get_pnx_ubuntu_pkg_enabled
from sources.functions.get_str_from_clipboard import get_str_from_clipboard
from sources.functions.get_youtube_clip_id import get_youtube_clip_id
from sources.functions.is_f_contained_feature_str import is_f_contained_feature_str
from sources.functions.is_os_windows import is_os_windows
from sources.functions.is_url import is_url
from sources.functions.remove_lines_within_keyword_from_f import remove_lines_within_keyword_from_f
from sources.objects.pk_etc import PK_BLANK
from sources.objects.pk_local_test_activate import LTA
from sources.objects.pk_map_texts import PkTexts
from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.task_orchestrator_cli_files import F_DOWNLOAD_YOUTUBE_VIDEOS_HISTORY, F_YOUTUBE_COOKIES_TXT
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE


@ensure_seconds_measured
def ensure_youtube_videos_downloaded_advanced():
    try:
        d_pnx = D_PK_WORKING
        logging.debug("YouTube 쿠키 관리 시스템 초기화 중...")

        try:
            cookie_management_success = ensure_youtube_cookies_created()
            if not cookie_management_success:
                logging.debug("️ 쿠키 관리에 실패했습니다. 기본 모드로 진행합니다.")
                cookie_exists = False
            else:
                cookie_path = Path(F_YOUTUBE_COOKIES_TXT)
                cookie_exists = cookie_path.exists() and cookie_path.stat().st_size > 0

        except ImportError:
            logging.debug("️ 새로운 쿠키 관리 시스템을 사용할 수 없습니다. 기존 방식으로 진행합니다.")
            cookie_path = Path(F_YOUTUBE_COOKIES_TXT)
            cookie_exists = cookie_path.stat().st_size > 0

        if not cookie_exists:
            logging.debug("️ 쿠키 파일이 없습니다. 연령 제한 동영상은 다운로드할 수 없을 수 있습니다.")
            logging.debug(f"쿠키 파일 경로: {F_YOUTUBE_COOKIES_TXT}")
            logging.debug("자동 쿠키 관리를 위해 'ensure_youtube_cookies_created()' 함수를 실행해주세요.")

            cookie_guide = textwrap.dedent(f"""
                쿠키 파일 생성 방법:
                1. Chrome에서 YouTube에 로그인
                2. 확장 프로그램 'Get cookies.txt' 설치
                3. YouTube 페이지에서 쿠키 내보내기
                4. 파일명을 'youtube_cookies.txt'로 저장
                5. {D_TASK_ORCHESTRATOR_CLI_SENSITIVE} 폴더에 복사
                
                또는 자동 관리:
                python -m resources.functions.ensure_youtube_cookies_created
            """).lstrip()

            logging.debug(cookie_guide)

            # 쿠키 없이 계속 진행할지 확인
            question = rf"쿠키 없이 계속 진행하시겠습니까"
            ok = ensure_value_completed(key_hint=question, options=[PkTexts.YES, PkTexts.NO])
            if ok != PkTexts.YES:
                return

        if is_os_windows():
            ffmpeg_location = rf'{Path(get_p(F_FFMPEG_EXE))}'
        else:
            ensure_ubuntu_pkg_enabled('ffmpeg')
            ffmpeg_location = get_pnx_ubuntu_pkg_enabled('ffmpeg')

        # ydl_opts 구성 (쿠키 파일 존재 여부에 따라)
        ydl_opts = {
            'ffmpeg_location': ffmpeg_location,
            'format': 'bestvideo+bestaudio/best',  # 최상의 비디오 & 오디오 선택
            'outtmpl': os.path.join(d_pnx, '%(title)s [%(id)s].%(ext)s'),
            'quiet': False,
            'noplaylist': True,
            'merge_output_format': 'mp4',  # 병합 시 MP4로 저장
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'  # 변환 후 MP4로 저장
            }],
            'geo_bypass': True,  # 지역 제한 우회
        }

        # 쿠키 파일이 존재하는 경우에만 추가
        if cookie_exists:
            ydl_opts['cookiefile'] = str(F_YOUTUBE_COOKIES_TXT)
            ydl_opts['extractor_args'] = ['youtube:player_client=web']
            ydl_opts['user_agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140 Safari/537.36'
            logging.debug("쿠키 파일을 사용하여 연령 제한 동영상도 다운로드할 수 있습니다.")
        else:
            # 쿠키 없이도 시도할 수 있는 옵션 추가
            ydl_opts.update({
                'no_check_certificate': True,
                'extractor_retries': 3,
                'fragment_retries': 3,
                'retries': 3,
            })

        f_historical = F_DOWNLOAD_YOUTUBE_VIDEOS_HISTORY
        ensure_pnx_made(pnx=f_historical, mode='f')

        pk_db = PkSqlite3DB()

        # 다운로드 모드 선택
        download_mode = pk_db.get_values(db_id='download_mode')
        if not download_mode:
            pk_db.reset_values(db_id='download_mode')
            pk_db.save_value_from_options(question="다운로드 모드를 선택하세요", options=["URL 입력 모드", "히스토리 URLs 다운로드 모드"], db_id='download_mode')
            download_mode = pk_db.get_values(db_id='download_mode')

        # 다운로드 후 동작 선택
        value = pk_db.get_values(db_id='download_option')
        if not value:
            pk_db.reset_values(db_id='download_option')
            pk_db.save_value_from_options(question="다운로드 후 동영상을 재생할까요?", options=[PkTexts.SKIP, PkTexts.play], db_id='download_option')
            value = pk_db.get_values(db_id='download_option')

        # 히스토리 파일 열기 옵션
        value_historical = pk_db.get_values(db_id='open historical f')
        if value_historical == PkTexts.YES:
            ensure_pnx_opened_by_ext(pnx=f_historical)
            pk_db.set_values(db_id="open historical f", values="YES, one time done")  # 프로그램 실행 중 1회만 실행제한

        if download_mode == "URL 입력 모드":
            logging.debug("URL 입력 모드 ===")
            _handle_url_input_mode_improved(f_historical, d_pnx, ydl_opts, pk_db, value, cookie_exists)
        else:
            logging.debug("히스토리 URLs 다운로드 모드 ===")
            _handle_history_download_mode_improved(f_historical, d_pnx, ydl_opts, pk_db, value, cookie_exists)

        return True

    except SystemExit as e:
        if e.code == 0:
            logging.debug(f'[{PkTexts.NORMAL_EXIT}: SystemExit(0)]')
            sys.exit(0)
        else:
            raise  # 비정상 종료는 그대로 propagate
    except Exception as e:
        import traceback
        logging.debug(f"예상치 못한 오류: {e}")
        traceback.print_exc()
        return False


def _handle_url_input_mode_improved(f_historical, d_pnx, ydl_opts, pk_db, play_option, cookie_exists):
    # 히스토리에서 URL 목록 가져오기
    historical_lines = get_historical_list(f=f_historical)

    if LTA:
        TEST_URL = "https://www.youtube.com/watch?v=6jQOQQA7-eA"  # 연령 제한 동영상 테스트용
        #  LTA 모드: 하드 코딩된 URL 사용
        url = TEST_URL
        logging.debug(f"LTA 모드: 하드 코딩된 URL 사용")
        logging.debug(f"다운로드할 URL: {url}")

        # 히스토리에 테스트 URL 추가
        ensure_list_written_to_f(f=f_historical, working_list=[url] + historical_lines, mode="w")
    else:
        #  일반 모드: 클립보드 + 히스토리에서 URL 가져오기
        youtube_video_url_from_clipboard = get_str_from_clipboard()
        marker_for_clipboard = f'{PK_BLANK}(url from clipboard)'
        youtube_video_url_from_clipboard = rf"{youtube_video_url_from_clipboard}{marker_for_clipboard}"

        # 옵션 구성 (클립보드 + 히스토리)
        option_values = []
        if youtube_video_url_from_clipboard and is_url(youtube_video_url_from_clipboard):
            option_values.append(youtube_video_url_from_clipboard)
        option_values.extend(historical_lines)

        # URL 입력 받기
        answer = ensure_value_completed(key_hint='YOUTUBE URL TO DOWNLOAD', options=option_values)
        answer = answer.strip()

        url = answer
        ensure_list_written_to_f(f=f_historical, working_list=[url] + historical_lines, mode="w")
        url = url.replace(marker_for_clipboard, "")

    # 단일 URL 다운로드 (개선된 에러 처리 포함)
    _download_single_url_improved(url, d_pnx, ydl_opts, f_historical, pk_db, play_option, cookie_exists)


def _handle_history_download_mode_improved(f_historical, d_pnx, ydl_opts, pk_db, play_option, cookie_exists):
    """개선된 히스토리 URLs 다운로드 모드 처리"""
    from sources.functions.get_historical_list import get_historical_list
    from sources.functions.get_list_deduplicated import get_list_deduplicated
    from sources.functions.get_list_from_f import get_list_from_f
    from sources.functions.get_list_removed_element_contain_prompt import get_list_removed_element_contain_prompt
    from sources.functions.get_list_striped_element import get_list_striped_element
    import logging
    from sources.functions.get_list_removed_element_empty import get_list_removed_empty

    # 히스토리에서 모든 URL 가져오기
    working_list = get_list_from_f(f=f_historical)
    working_list = get_list_removed_element_contain_prompt(working_list=working_list, prompt="#")
    working_list = get_list_deduplicated(working_list=working_list)
    working_list = get_list_removed_empty(working_list=working_list)
    working_list = get_list_striped_element(working_list=working_list)

    if len(working_list) == 0:
        logging.debug("히스토리에 다운로드할 URL이 없습니다.")
        return

    logging.debug(f"히스토리에서 {len(working_list)}개의 URL을 찾았습니다.")

    # 이미 다운로드된 URL들 처리
    _process_already_downloaded_urls_improved(working_list, d_pnx, f_historical, pk_db, play_option)

    # 남은 URL들 다운로드
    remaining_urls = get_historical_list(f=f_historical)
    if remaining_urls:
        logging.debug(f"다운로드할 URL 개수: {len(remaining_urls)}")
        for i, url in enumerate(remaining_urls, 1):
            logging.debug(f"{i}: {url}")

        # 배치 다운로드 (개선된 에러 처리 포함)
        _download_multiple_urls_improved(remaining_urls, d_pnx, ydl_opts, f_historical, pk_db, play_option, cookie_exists)
    else:
        logging.debug("모든 URL이 이미 다운로드되었습니다.")


def _download_single_url_improved(url, d_pnx, ydl_opts, f_historical, pk_db, play_option, cookie_exists):
    """개선된 단일 URL 다운로드 - 향상된 에러 처리 및 쿠키 관리"""
    from sources.functions.is_os_windows import is_os_windows
    from sources.functions.get_youtube_clip_id import get_youtube_clip_id
    from sources.functions.ensure_youtube_videos_downloaded_v2_via_yt_dlp import ensure_youtube_videos_downloaded_v2_via_yt_dlp
    import logging
    from sources.functions.normalize_youtube_url import normalize_youtube_url
    from sources.functions.is_f_contained_feature_str import is_f_contained_feature_str
    import yt_dlp

    if is_os_windows():
        try:
            youtube_clip_id = get_youtube_clip_id(url=url)
            ensure_youtube_videos_downloaded_v2_via_yt_dlp(url_list=[youtube_clip_id], d_pnx=d_pnx, f_func_n_txt=f_historical)

            youtube_clip_id_stamp = f"[{youtube_clip_id}]"
            if is_f_contained_feature_str(feature_str=youtube_clip_id_stamp, d_pnx=d_pnx):
                logging.debug(f"{youtube_clip_id_stamp} 다운로드 완료: {url}")

                # 연령 제한 동영상 다운로드 성공 시 쿠키 백업
                if cookie_exists:
                    try:
                        from sources.functions.ensure_youtube_cookies_created import backup_successful_cookies
                        if backup_successful_cookies():
                            logging.debug("성공한 쿠키를 백업했습니다.")
                        else:
                            logging.debug("️ 쿠키 백업에 실패했습니다.")
                    except ImportError:
                        logging.debug("️ 쿠키 백업 시스템을 사용할 수 없습니다.")

                _handle_post_download_action(youtube_clip_id, url, d_pnx, f_historical, pk_db, play_option)
            else:
                logging.debug(f"{youtube_clip_id_stamp} 다운로드 실패: {url}")
        except Exception as e:
            logging.debug(f"Windows 다운로드 오류: {url}\n{str(e)}")
            _handle_download_error_improved(url, str(e), cookie_exists)
    else:
        url = normalize_youtube_url(url)
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                youtube_clip_id = info.get('id', None)
                youtube_clip_id_stamp = f"[{youtube_clip_id}]"
                clip_title = info.get('title')

                logging.debug(f"다운로드 시작: {clip_title} ({youtube_clip_id})")

                # 이미 다운로드된 경우
                if is_f_contained_feature_str(feature_str=youtube_clip_id_stamp, d_pnx=d_pnx):
                    logging.debug(f"{youtube_clip_id_stamp} 이미 다운로드됨: {clip_title}")
                    _handle_post_download_action(youtube_clip_id, url, d_pnx, f_historical, pk_db, play_option)
                    return

                # 다운로드 실행
                ydl.download([url])

                # 다운로드 확인
                if is_f_contained_feature_str(feature_str=youtube_clip_id_stamp, d_pnx=d_pnx):
                    logging.debug(f"다운로드 완료: {clip_title}")

                    # 연령 제한 동영상 다운로드 성공 시 쿠키 백업
                    if cookie_exists:
                        try:
                            from sources.functions.ensure_youtube_cookies_created import backup_successful_cookies
                            if backup_successful_cookies():
                                logging.debug("성공한 쿠키를 백업했습니다.")
                            else:
                                logging.debug("️ 쿠키 백업에 실패했습니다.")
                        except ImportError:
                            logging.debug("️ 쿠키 백업 시스템을 사용할 수 없습니다.")

                    _handle_post_download_action(youtube_clip_id, url, d_pnx, f_historical, pk_db, play_option)
                else:
                    logging.debug(f"다운로드 실패: {clip_title}")

        except Exception as e:
            logging.debug(f"다운로드 오류: {url}\n{str(e)}")
            _handle_download_error_improved(url, str(e), cookie_exists)


def _handle_download_error_improved(url, error_msg, cookie_exists):
    """개선된 다운로드 오류 처리 - 더 구체적인 해결 방안 제시"""
    import logging

    logging.debug(f"다운로드 오류 분석 중...")

    if "Sign in to confirm your age" in error_msg or "age-restricted" in error_msg:
        logging.warning("연령 제한 동영상입니다.")

        if not cookie_exists:
            logging.debug("해결 방법:")
            logging.debug("  1. Chrome에서 YouTube에 로그인")
            logging.debug("  2. 확장 프로그램 'Get cookies.txt' 설치")
            logging.debug("  3. YouTube 페이지에서 쿠키 내보내기")
            logging.debug("  4. 자동 쿠키 관리 실행:")
            logging.debug("     python -m resources.functions.ensure_youtube_cookies_created")
        else:
            logging.debug("쿠키 파일이 있지만 인증에 실패했습니다.")
            logging.debug("  쿠키를 새로 내보내거나 자동 관리 시스템을 사용하세요:")
            logging.debug("  python -m resources.functions.ensure_youtube_cookies_created")

    elif "This video is unavailable" in error_msg:
        logging.debug("동영상을 사용할 수 없습니다. (삭제되었거나 비공개)")

    elif "Video unavailable" in error_msg:
        logging.debug("동영상을 사용할 수 없습니다.")

    elif "copyright" in error_msg.lower():
        logging.debug("️ 저작권 문제로 다운로드할 수 없습니다.")

    elif "network" in error_msg.lower() or "connection" in error_msg.lower():
        logging.debug("네트워크 연결 문제입니다.")
        logging.debug("  인터넷 연결을 확인하고 다시 시도해주세요.")

    else:
        logging.debug(f"알 수 없는 오류: {error_msg[:100]}...")

    logging.debug("다운로드를 건너뛰고 다음 URL로 진행합니다.")


def _download_multiple_urls_improved(urls, d_pnx, ydl_opts, f_historical, pk_db, play_option, cookie_exists):
    """개선된 여러 URL 배치 다운로드"""
    from sources.functions.is_f_contained_feature_str import is_f_contained_feature_str
    from sources.functions.is_os_windows import is_os_windows
    from sources.functions.normalize_youtube_url import normalize_youtube_url
    import logging
    import yt_dlp

    if is_os_windows():
        # Windows에서는 기존 방식 사용
        for url in urls:
            _download_single_url_improved(url, d_pnx, ydl_opts, f_historical, pk_db, play_option, cookie_exists)
    else:
        # Linux에서는 배치 다운로드
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                for url in urls:
                    url = normalize_youtube_url(url)
                    try:
                        info = ydl.extract_info(url, download=False)
                        youtube_clip_id = info.get('id', None)
                        youtube_clip_id_stamp = f"[{youtube_clip_id}]"
                        clip_title = info.get('title')

                        logging.debug(f"다운로드 시작: {clip_title} ({youtube_clip_id})")

                        # 이미 다운로드된 경우
                        if is_f_contained_feature_str(feature_str=youtube_clip_id_stamp, d_pnx=d_pnx):
                            logging.debug(f"{youtube_clip_id_stamp} 이미 다운로드됨: {clip_title}")
                            _handle_post_download_action(youtube_clip_id, url, d_pnx, f_historical, pk_db, play_option)
                            continue

                        # 다운로드 실행
                        ydl.download([url])

                        # 다운로드 확인
                        if is_f_contained_feature_str(feature_str=youtube_clip_id_stamp, d_pnx=d_pnx):
                            logging.debug(f"다운로드 완료: {clip_title}")

                            # 연령 제한 동영상 다운로드 성공 시 쿠키 백업
                            if cookie_exists:
                                try:

                                    if backup_successful_cookies():
                                        logging.debug("성공한 쿠키를 백업했습니다.")
                                    else:
                                        logging.debug("️ 쿠키 백업에 실패했습니다.")
                                except ImportError:
                                    logging.debug("️ 쿠키 백업 시스템을 사용할 수 없습니다.")

                            _handle_post_download_action(youtube_clip_id, url, d_pnx, f_historical, pk_db, play_option)
                        else:
                            logging.debug(f"다운로드 실패: {clip_title}")

                    except Exception as e:
                        logging.debug(f"다운로드 오류: {url}\n{str(e)}")
                        _handle_download_error_improved(url, str(e), cookie_exists)

        except Exception as e:
            logging.debug(f"배치 다운로드 오류: {str(e)}")


def _process_already_downloaded_urls_improved(urls, d_pnx, f_historical, pk_db, play_option):
    """개선된 이미 다운로드된 URL들 처리"""

    for url in urls:
        url = url.strip()
        if not url:
            continue

        youtube_clip_id = get_youtube_clip_id(url=url)
        youtube_clip_id_stamp = f"[{youtube_clip_id}]"

        if is_f_contained_feature_str(feature_str=youtube_clip_id_stamp, d_pnx=d_pnx):
            logging.debug(f"{youtube_clip_id_stamp} 이미 다운로드됨: {url}")
            _handle_post_download_action(youtube_clip_id, url, d_pnx, f_historical, pk_db, play_option)

            # 히스토리에서 제거
            remove_lines_within_keyword_from_f(f=f_historical, keyword=youtube_clip_id)

    # 히스토리 업데이트
    get_historical_list(f=f_historical)


def _handle_post_download_action(youtube_clip_id, url, d_pnx, f_historical, pk_db, play_option):
    """다운로드 후 동작 처리 (재생 또는 스킵)"""
    from sources.functions.get_f_contained_feature_str import get_f_contained_feature_str
    from sources.functions.ensure_pnx_opened_by_ext import ensure_pnx_opened_by_ext
    from sources.objects.pk_map_texts import PkTexts
    import logging

    if play_option == PkTexts.play:
        # 동영상 재생
        f_pnx_downloaded = get_f_contained_feature_str(feature_str=youtube_clip_id, d_pnx=d_pnx)
        if f_pnx_downloaded:
            logging.debug(f"동영상 재생: {f_pnx_downloaded}")
            ensure_pnx_opened_by_ext(pnx=f_pnx_downloaded)
    elif play_option == PkTexts.SKIP:
        logging.debug("️ 동영상 재생을 건너뜁니다.")
