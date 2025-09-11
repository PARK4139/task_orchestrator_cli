import time
from sources.functions.get_window_titles import get_window_titles

from sources.functions.ensure_video_playied_at_losslesscut_v2 import ensure_video_playied_at_losslesscut_v2
import logging
from sources.functions.is_losslesscut_playing import is_losslesscut_playing


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


def auto_load_and_play_v2(video_path, max_attempts=5, check_interval=2.0, timeout=60):
    """
    개선된 비디오 자동 로드 및 재생 함수
    
    Args:
        video_path: 비디오 파일 경로
        max_attempts: 최대 시도 횟수
        check_interval: 상태 확인 간격 (초)
        timeout: 전체 작업 타임아웃 (초)
    
    Returns:
        bool: 성공 여부
    """
    import logging
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


def auto_load_and_play_safe(video_path, **kwargs):
    """
    안전한 비디오 자동 로드 및 재생 (기본값 사용)
    """
    return auto_load_and_play_v2(video_path, **kwargs)

# example
# auto_load_and_play_v2(r"C:\path\to\your\video.mp4")
# auto_load_and_play_safe(r"C:\path\to\your\video.mp4")  # 기본값 사용
