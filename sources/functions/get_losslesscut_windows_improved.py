"""
LosslessCut 창 감지 함수
"""
import logging
import logging

import logging
from sources.functions.collect_losslesscut_patterns import ensure_losslesscut_window_patterns_collected
from sources.functions.ensure_seconds_measured import ensure_seconds_measured
from sources.functions.get_window_titles import get_window_titles


def is_losslesscut_window(title):
    """
    주어진 창 제목이 LosslessCut 창인지 판단

    Args:
        title: 창 제목

    Returns:
        bool: LosslessCut 창이면 True, 아니면 False
    """
    if not title:
        return False

    title_lower = title.lower()

    # n. 정확한 기본 창 제목
    if title_lower == "losslesscut":
        return True

    # n. LosslessCut으로 시작하고 끝나는 패턴
    if (title_lower.startswith("losslesscut") and
            title_lower.endswith("losslesscut") and
            " - " in title):
        return True

    # n. "LosslessCut - [내용] - LosslessCut" 형태
    if (title_lower.startswith("losslesscut - ") and
            title_lower.endswith(" - losslesscut")):
        return True

    # n. "Loading file - [filename] - LosslessCut" 형태
    if (title_lower.startswith("loading file - ") and
            title_lower.endswith(" - losslesscut")):
        return True

    # n. "Exporting - [filename] - LosslessCut" 형태
    if (title_lower.startswith("exporting - ") and
            title_lower.endswith(" - losslesscut")):
        return True

    # 6. 기타 LosslessCut 관련 패턴들
    losslesscut_keywords = [
        "losslesscut",
        "로딩 중",
        "loading",
        "exporting",
        "출력 중",
        "불러오는 중"
    ]

    # LosslessCut 키워드가 포함되고 창 제목에 "LosslessCut"이 포함된 경우
    if any(keyword in title_lower for keyword in losslesscut_keywords) and "losslesscut" in title_lower:
        return True

    return False


@ensure_seconds_measured
@ensure_losslesscut_window_patterns_collected()
def get_losslesscut_windows_improved(verbose=True):
    """개선된 LosslessCut 창 감지 - 무조건 엄격한 패턴 매칭"""
    try:
        from sources.functions.get_window_titles import get_window_titles
        window_titles = get_window_titles()
    except Exception as e:
        logging.debug(f"윈도우 제목 가져오기 실패: {e}")
        return []

    losslesscut_titles = []

    # 윈도우 창 이름을 디버깅하기 좋게 출력 (verbose가 True일 때만)
    if verbose:
        try:
            logging.debug(f"현재 윈도우 창 {len(window_titles)}개 감지됨")
            # LosslessCut 관련 창만 필터링하여 출력
            losslesscut_related = [title for title in window_titles if "LosslessCut" in title]
            if losslesscut_related:
                logging.debug(f"LosslessCut 관련 창 {len(losslesscut_related)}개: {losslesscut_related}")
            else:
                logging.debug("LosslessCut 관련 창 없음")
        except Exception as e:
            logging.debug(f"윈도우 정보 출력 실패: {e}")

    for title in window_titles:
        title_lower = title.lower()

        # 무조건 엄격한 LosslessCut 창 검색 - 정확한 패턴만 허용
        if title_lower == "losslesscut":  # 정확한 기본 창 제목만
            losslesscut_titles.append(title)
            if verbose:
                logging.debug(f"LosslessCut 기본 창 감지됨: {title}")
        elif (title_lower.startswith("losslesscut") and
              title_lower.endswith("losslesscut") and
              title_lower.count(" - ") == 2):  # "LosslessCut - filename - LosslessCut" 형태만, 정확히 2개의 " - " 구분자
            losslesscut_titles.append(title)
            if verbose:
                logging.debug(f"LosslessCut 파일 로드 창 감지됨: {title}")
        # 다른 모든 패턴은 무시

    if not losslesscut_titles and verbose:
        logging.debug("LosslessCut 창이 감지되지 않음")

    return losslesscut_titles


@ensure_seconds_measured
def get_losslesscut_windows_with_info():
    """
    LosslessCut 창 정보와 함께 반환

    Returns:
        list: LosslessCut 창 정보 딕셔너리 리스트 (title, process_id 등)
    """
    try:
        window_titles = get_window_titles()
        losslesscut_windows = []

        for title in window_titles:
            if is_losslesscut_window(title):
                # 창 정보 구성 (향후 확장 가능)
                window_info = {
                    'title': title,
                    'is_losslesscut': True,
                    'pattern_type': analyze_losslesscut_pattern(title)
                }
                losslesscut_windows.append(window_info)

        return losslesscut_windows

    except Exception as e:
        logging.error(f"LosslessCut 창 정보 수집 중 오류: {e}")
        return []


def analyze_losslesscut_pattern(title):
    """
    LosslessCut 창 제목의 패턴을 분석

    Args:
        title: 창 제목

    Returns:
        str: 패턴 타입
    """
    if not title:
        return "UNKNOWN"

    title_lower = title.lower()

    if title_lower == "losslesscut":
        return "IDLE"
    elif "loading" in title_lower or "로딩" in title_lower or "불러오는" in title_lower:
        return "LOADING"
    elif "exporting" in title_lower or "출력" in title_lower:
        return "EXPORTING"
    elif " - " in title_lower and title_lower.count(" - ") >= 2:
        return "FILE_LOADED"
    else:
        return "UNKNOWN"
