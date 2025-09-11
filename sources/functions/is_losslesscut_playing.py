import logging


def is_losslesscut_playing(threshold=5.0, check_duration=3, second_interval=1):
    """
    LosslessCut에서 비디오 재생 상태를 간단하게 확인하는 함수
    - 스페이스바를 누른 후 상태 변화를 통해 유추
    """
    import time
    from sources.functions.get_window_titles import get_window_titles
    
    def check_losslesscut_ready():
        """LosslessCut이 재생 준비가 되었는지 확인"""
        try:
            titles = get_window_titles()
            for title in titles:
                if "LosslessCut" in title:
                    # 로딩 중이 아닌지 확인
                    loading_patterns = ["불러오는 중", "Loading", "로딩 중", "Processing"]
                    if not any(pattern in title for pattern in loading_patterns):
                        return True
        except Exception as e:
            logging.debug(f"창 제목 확인 오류: {str(e)}")
        return False
    
    # LosslessCut이 준비되었는지 확인
    if check_losslesscut_ready():
        logging.debug("LosslessCut이 재생 준비되었습니다.")
        return True
    else:
        logging.debug("LosslessCut이 준비되지 않았습니다.")
        return False


def is_losslesscut_ready_for_playback(timeout=5, check_interval=0.5):
    """
    LosslessCut이 재생 준비가 되었는지 확인하는 함수
    """
    import time
    from sources.functions.get_window_titles import get_window_titles
    import logging
    
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            titles = get_window_titles()
            for title in titles:
                if "LosslessCut" in title:
                    # 로딩 중이 아닌지 확인
                    loading_patterns = ["불러오는 중", "Loading", "로딩 중", "Processing"]
                    if not any(pattern in title for pattern in loading_patterns):
                        # 파일명이 포함되어 있는지 확인 (비디오가 로드되었는지)
                        if any(char.isalnum() for char in title if char not in "LosslessCut -"):
                            logging.debug("LosslessCut이 재생 준비되었습니다.")
                            return True
            
            time.sleep(check_interval)
            
        except Exception as e:
            logging.debug(f"재생 준비 상태 확인 오류: {str(e)}")
            time.sleep(check_interval)
    
    logging.debug(f"재생 준비 대기 타임아웃 ({timeout}초)")
    return False
