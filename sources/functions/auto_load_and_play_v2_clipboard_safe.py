#!/usr/bin/env python3
"""
클립보드 보존 기능이 적용된 LosslessCut 자동 로드 및 재생 함수
"""

import time
from pathlib import Path
from sources.functions.get_window_titles import get_window_titles

from sources.functions.ensure_video_playied_at_losslesscut_v2 import ensure_video_playied_at_losslesscut_v2
import logging
from sources.functions.is_losslesscut_playing import is_losslesscut_playing
from sources.functions.ensure_clipboard_preserved import ClipboardPreserver, preserve_clipboard_during_operation


def is_editing_or_exporting(titles):
    """편집/출력 중인지 확인"""
    for title in titles:
        if "출력" in title or "Export" in title or "편집" in title or "Edit" in title:
            return True
    return False


def is_losslesscut_ready_for_video():
    """LosslessCut이 비디오 로드 준비가 되었는지 확인"""
    titles = get_window_titles()
    for title in titles:
        if "LosslessCut" in title and ("불러오는 중" not in title and "Loading" not in title):
            return True
    return False


def auto_load_and_play_v2_clipboard_safe(video_path, max_attempts=5, check_interval=2.0, timeout=60):
    """
    클립보드 보존 기능이 적용된 개선된 비디오 자동 로드 및 재생 함수
    
    Args:
        video_path: 비디오 파일 경로
        max_attempts: 최대 시도 횟수
        check_interval: 상태 확인 간격 (초)
        timeout: 전체 작업 타임아웃 (초)
    
    Returns:
        bool: 성공 여부
    """

    def _auto_load_and_play_operation():
        """실제 자동 로드 및 재생 작업"""
        from sources.objects.pk_local_test_activate import LTA

        start_time = time.time()
        attempt_count = 0

        logging.debug(f"비디오 자동 로드 및 재생을 시작합니다: {video_path}")

        while attempt_count < max_attempts:
            # 타임아웃 체크
            if time.time() - start_time > timeout:
                logging.debug(f"작업이 타임아웃되었습니다 ({timeout}초)")
                return False

            attempt_count += 1
            logging.debug(f"시도 {attempt_count}/{max_attempts}")

            try:
                # 현재 창 상태 확인
                titles = get_window_titles()

                if is_editing_or_exporting(titles):
                    logging.debug("편집/출력 중이므로 대기...")
                    time.sleep(check_interval)
                    continue

                # LosslessCut이 준비되었는지 확인
                if not is_losslesscut_ready_for_video():
                    logging.debug("LosslessCut이 준비되지 않았습니다. 비디오를 로드합니다...")
                    ensure_f_video_loaded_on_losslesscut(video_path)
                    time.sleep(2)  # 로드 대기 시간 증가

                # 비디오 재생 시도
                logging.debug("비디오 재생을 시도합니다...")
                if ensure_video_playied_at_losslesscut_v2():
                    logging.debug("비디오 로드 및 재생이 성공적으로 완료되었습니다!")
                    return True
                else:
                    logging.debug("비디오 재생에 실패했습니다. 재시도합니다...")
                    time.sleep(check_interval)

            except Exception as e:
                logging.debug(f"오류 발생: {str(e)}")
                time.sleep(check_interval)

        logging.debug(f"최대 시도 횟수({max_attempts})에 도달했습니다. 작업을 중단합니다.")
        return False

    # 클립보드 보존하면서 작업 실행
    return preserve_clipboard_during_operation(_auto_load_and_play_operation)


def auto_load_and_play_safe_clipboard_safe(video_path, **kwargs):
    """
    클립보드 보존 기능이 적용된 안전한 비디오 자동 로드 및 재생 (기본값 사용)
    """
    return auto_load_and_play_v2_clipboard_safe(video_path, **kwargs)


def auto_load_and_play_by_creation_date_clipboard_safe(d_working, ext_list_allowed, max_attempts=5, timeout=300, check_interval=2.0):
    """
    클립보드 보존 기능이 적용된 생성일자 순 비디오 자동 로드 및 재생
    """

    def _auto_load_by_creation_date_operation():
        """실제 생성일자 순 자동 로드 작업"""
        from sources.functions.get_f_video_of_d_working_by_creation_date import get_f_video_of_d_working_by_creation_date

        logging.debug(f"생성일자 순으로 비디오 자동 로드/재생을 시작합니다...")
        logging.debug(f"작업 디렉토리: {d_working}")
        logging.debug(f"허용 확장자: {ext_list_allowed}")

        # 비디오 파일들을 생성일자 순으로 정렬
        videos_sorted = get_f_video_of_d_working_by_creation_date(
            d_working,
            ext_list_allowed,
            sort_by='creation_time',
            reverse=True  # 최신순
        )

        if not videos_sorted:
            logging.debug("정렬할 비디오 파일을 찾을 수 없습니다.")
            return False

        logging.debug(f"총 {len(videos_sorted)}개의 비디오 파일을 생성일자 순으로 정렬했습니다.")

        # 각 비디오 파일에 대해 처리
        for idx, video_path in enumerate(videos_sorted):
            video_name = video_path.nick_name
            logging.debug(f"\n[{idx + 1}/{len(videos_sorted)}] {video_name} 처리 중...")

            # 클립보드 보존하면서 개별 비디오 처리
            success = preserve_clipboard_during_operation(
                auto_load_and_play_v2_clipboard_safe,
                video_path,
                max_attempts,
                check_interval,
                timeout
            )

            if success:
                logging.debug(f"{video_name} 처리 완료!")

                # 사용자에게 다음 비디오로 넘어갈지 확인
                if idx < len(videos_sorted) - 1:
                    next_video = videos_sorted[idx + 1].nick_name
                    logging.debug(f"다음 비디오: {next_video}")
                    logging.debug("계속하려면 아무 키나 누르세요...")

                    # 간단한 대기 (실제로는 사용자 입력을 받을 수 있음)
                    time.sleep(3)
            else:
                logging.debug(f"{video_name} 처리 실패")

        logging.debug("모든 비디오 처리 완료!")
        return True

    # 클립보드 보존하면서 작업 실행
    return preserve_clipboard_during_operation(_auto_load_by_creation_date_operation)


def auto_load_and_play_latest_video_clipboard_safe(d_working, ext_list_allowed, max_attempts=5, timeout=300):
    """
    클립보드 보존 기능이 적용된 최신 비디오 자동 로드 및 재생
    """

    def _auto_load_latest_video_operation():
        """실제 최신 비디오 자동 로드 작업"""
        from sources.functions.get_f_video_of_d_working_by_creation_date import get_f_video_of_d_working_by_creation_date

        # 가장 최근 비디오 파일 가져오기
        latest_video = get_f_video_of_d_working_by_creation_date(
            d_working,
            ext_list_allowed,
            sort_by='creation_time',
            reverse=True
        )

        if not latest_video or len(latest_video) == 0:
            logging.debug("최신 비디오 파일을 찾을 수 없습니다.")
            return False

        video_path = latest_video[0]
        video_name = video_path.nick_name

        logging.debug(f"최신 비디오 파일: {video_name}")

        # 단일 비디오 처리
        return auto_load_and_play_v2_clipboard_safe(
            video_path,
            max_attempts,
            1.0,  # check_interval
            timeout
        )

    # 클립보드 보존하면서 작업 실행
    return preserve_clipboard_during_operation(_auto_load_latest_video_operation)


# 사용 예제
if __name__ == "__main__":
    # 단일 비디오 테스트
    # auto_load_and_play_v2_clipboard_safe(r"C:\path\to\your\video.mp4")

    # 생성일자 순 테스트
    # auto_load_and_play_by_creation_date_clipboard_safe(
    #     "resources",
    #     ['.mp4', '.avi', '.mkv']
    # )

    # 최신 비디오 테스트
    # auto_load_and_play_latest_video_clipboard_safe(
    #     "resources",
    #     ['.mp4', '.avi', '.mkv']
    # )

    logging.debug("클립보드 보존 기능이 적용된 LosslessCut 자동화 함수가 준비되었습니다.")
