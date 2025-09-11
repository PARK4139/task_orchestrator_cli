#!/usr/bin/env python3
"""
LosslessCut 창 제목 패턴 수집 및 분석
"""

import logging
import logging
from datetime import datetime
from functools import wraps
from pathlib import Path
from typing import Callable

from sources.functions.get_window_titles import get_window_titles
from sources.objects.pk_etc import PK_UNDERLINE


def ensure_losslesscut_window_patterns_collected():
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 메인 로그 파일 경로 (하나의 파일에 통합)
            try:
                from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_LOGS
                from datetime import datetime
                timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
                main_log_file = Path(D_TASK_ORCHESTRATOR_CLI_LOGS) / f"losslesscut_window_pattern_{timestamp}.log"
            except Exception as e:
                logging.debug(f"[AUTO_PATTERN] 메인 로그 파일 경로 생성 실패: {e}")
                main_log_file = "losslesscut_window_ pattern_main.log"

            # 함수 실행 전 패턴 수집
            try:
                collect_losslesscut_patterns()
            except Exception as e:
                logging.debug(f"[AUTO_PATTERN]  실행 전 패턴 수집 실패: {func.__name__} - {e}")

            # 원본 함수 실행
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                logging.debug(f"[AUTO_PATTERN]  함수 실행 실패: {func.__name__} - {e}")
                raise

            # 함수 실행 후 패턴 수집
            try:
                collect_losslesscut_patterns()
            except Exception as e:
                logging.debug(f"[AUTO_PATTERN]  실행 후 패턴 수집 실패: {func.__name__} - {e}")

            return result

        return wrapper

    return decorator


def ensure_losslesscut_window_patterns_collected_before_after():
    """
    컨텍스트 매니저로 LosslessCut 창 패턴 수집을 자동화
    - 하나의 메인 로그 파일에 모든 기록
    - 기본 수집 시간: 5초, 기본 간격: 0.5초
    - 인자 없이 사용: ensure_losslesscut_window_patterns_collected_before_after()
    """

    class PatternCollector:
        def __init__(self):
            # 메인 로그 파일 경로 자동 생성
            try:
                from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_LOGS
                from datetime import datetime
                timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
                self.log_file = str(Path(D_TASK_ORCHESTRATOR_CLI_LOGS) / f"losslesscut_window_pattern_{timestamp}.log")
            except Exception as e:
                logging.debug(f"[AUTO_PATTERN] 메인 로그 파일 경로 생성 실패: {e}")
                self.log_file = "losslesscut_window_pattern_main.log"

            self.duration = 5  # 기본값: 5초
            self.interval = 0.5  # 기본값: 0.5초
            self.function_name = "unknown"

        def __enter__(self):
            # 시작 시 패턴 수집
            try:
                logging.debug(f"[AUTO_PATTERN] 동작 시작 전 패턴 수집: {self.function_name}")
                collect_losslesscut_patterns()
            except Exception as e:
                logging.debug(f"[AUTO_PATTERN] 시작 전 패턴 수집 실패: {e}")
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            # 종료 시 패턴 수집
            try:
                logging.debug(f"[AUTO_PATTERN] 동작 완료 후 패턴 수집: {self.function_name}")
                collect_losslesscut_patterns()
            except Exception as e:
                logging.debug(f"[AUTO_PATTERN] 완료 후 패턴 수집 실패: {e}")

            # 예외가 발생했으면 False 반환 (예외 전파)
            return exc_type is None

        def set_function_name(self, name: str):
            """함수 이름 설정"""
            self.function_name = name
            return self

    return PatternCollector()  # 모든 기본값 사용


def collect_losslesscut_patterns():
    """
    LosslessCut 창 이름 패턴을 수집하여 로깅 파일에 저장 (1번만 실행)
    
    Args:
        output_file: 출력 파일 경로
        duration: 사용하지 않음 (하위 호환성을 위해 유지)
        interval: 사용하지 않음 (하위 호환성을 위해 유지)
    """
    try:
        # 현재 창 제목들 가져오기 (1번만)
        window_titles = get_window_titles()
        # 전체 창 제목 수 및 상세 내용 로깅 제거

        # LosslessCut 관련 창들만 필터링
        losslesscut_windows = []
        for title in window_titles:
            if "LosslessCut" in title:
                losslesscut_windows.append(title)
                logging.debug(f"LosslessCut 포함 창 발견: '{title}'")

        # LosslessCut 포함된 창들만 출력
        if losslesscut_windows:
            logging.debug(f"LosslessCut 포함된 창들: {losslesscut_windows}")

            # LosslessCut 예약 패턴만 필터링
            real_losslesscut_windows = []
            for title in losslesscut_windows:
                logging.debug(f"패턴 분석 중: '{title}'")

                # 각 패턴 조건별로 체크
                is_basic = title == "LosslessCut"
                is_ends_with = title.endswith(" - LosslessCut")
                is_starts_with = title.startswith("LosslessCut - ")

                logging.debug(f"- 기본 창 패턴 ('LosslessCut'): {is_basic}")
                logging.debug(f"- 끝 패턴 (' - LosslessCut'): {is_ends_with}")
                logging.debug(f"- 시작 패턴 ('LosslessCut - '): {is_starts_with}")

                if (is_basic or is_ends_with or is_starts_with):
                    real_losslesscut_windows.append(title)
                    logging.debug(f"패턴 매칭 성공: '{title}'")
                else:
                    logging.debug(f"패턴 매칭 실패: '{title}'")

            logging.debug(f"LosslessCut 예약 패턴: {real_losslesscut_windows}")

            # 실제 패턴이 있으면 수집 완료 메시지
            if real_losslesscut_windows:
                logging.debug(f"{PK_UNDERLINE}")
                logging.debug(f"LosslessCut 창 {len(real_losslesscut_windows)}개 감지됨")
            else:
                logging.debug("️ LosslessCut 창은 감지되었지만 유효한 패턴이 없음")
                logging.debug(f"감지된 창들: {losslesscut_windows}")
                logging.debug("패턴 매칭 실패 원인 분석:")
                for title in losslesscut_windows:
                    logging.debug(f"'{title}' - 길이: {len(title)}, 포함 문자: {[c for c in title]}")
        else:
            logging.debug("LosslessCut 창이 감지되지 않음")

    except Exception as e:
        logging.error(f"창 제목 수집 중 오류: {e}")


def analyze_window_title_pattern(title):
    """
    창 제목을 분석하여 패턴 정보 반환
    
    Args:
        title: 창 제목
        
    Returns:
        패턴 분석 결과 딕셔너리
    """
    logging.debug(f"창 제목 패턴 분석 시작: '{title}'")
    title_lower = title.lower()
    logging.debug(f"소문자 변환: '{title_lower}'")

    # 기본 패턴 분석
    if title == "LosslessCut":
        pattern_type = "기본 창"
        filename = None
        state = "IDLE"
        logging.debug("  기본 창 패턴 매칭")
    elif title_lower.startswith("losslesscut - ") and title_lower.endswith(" - losslesscut"):
        pattern_type = "파일 로드된 창"
        # 중간 부분 추출 (파일명)
        parts = title.split(" - ")
        logging.debug(f"파일명 추출 시도: {parts}")
        if len(parts) >= 3:
            filename = parts[1]
            logging.debug(f"파일명 추출 성공: '{filename}'")
        else:
            filename = "추출 실패"
            logging.debug(f"파일명 추출 실패: parts 수 {len(parts)}")
        state = "FILE_LOADED"
        logging.debug("  파일 로드된 창 패턴 매칭")
    elif "exporting" in title_lower:
        pattern_type = "Export 진행 중"
        filename = None
        state = "EXPORTING"
        logging.debug("  Export 진행 중 패턴 매칭")
    elif any(pattern in title_lower for pattern in ["loading", "불러오는 중", "로딩 중", "processing"]):
        pattern_type = "로딩 중"
        filename = None
        state = "LOADING"
        logging.debug("  로딩 중 패턴 매칭")
    elif " - " in title:
        pattern_type = "기타 구분자 포함"
        filename = "분석 필요"
        state = "UNKNOWN"
        logging.debug(" ️ 기타 구분자 포함 패턴 매칭")
    else:
        pattern_type = "기타 패턴"
        filename = None
        state = "UNKNOWN"
        logging.debug("  기타 패턴으로 분류")

    result = {
        "pattern_type": pattern_type,
        "filename": filename,
        "state": state
    }

    logging.debug(f"최종 분석 결과: {result}")
    return result


def save_pattern_analysis(unique_patterns, pattern_frequency, output_file):
    """
    패턴 분석 결과를 별도 파일로 저장
    
    Args:
        unique_patterns: 고유 패턴 집합
        pattern_frequency: 패턴별 빈도수
        output_file: 원본 로그 파일 경로
    """
    analysis_file = output_file.with_suffix('.analysis.txt')

    with open(analysis_file, 'w', encoding='utf-8') as f:
        f.write("=== LosslessCut 창 이름 패턴 분석 결과 ===\n")
        f.write(f"생성 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"고유 패턴 수: {len(unique_patterns)}\n")
        f.write(PK_UNDERLINE + "\n\n")

        # 패턴별 상세 분석
        f.write("=== 패턴별 상세 분석 ===\n")
        for pattern in sorted(unique_patterns):
            pattern_info = analyze_window_title_pattern(pattern)
            f.write(f"패턴: {pattern}\n")
            f.write(f"  타입: {pattern_info['pattern_type']}\n")
            f.write(f"  파일명: {pattern_info['filename']}\n")
            f.write(f"  상태: {pattern_info['state']}\n")
            f.write(f"  빈도: {pattern_frequency[pattern]}\n")
            f.write(f"  길이: {len(pattern)}\n")
            f.write("")

        # 빈도수별 정렬
        f.write("=== 빈도수별 정렬 ===\n")
        sorted_patterns = sorted(pattern_frequency.items(), key=lambda x: x[1], reverse=True)
        for pattern, frequency in sorted_patterns:
            pattern_info = analyze_window_title_pattern(pattern)
            f.write(f"{frequency:3d}회: {pattern} ({pattern_info['pattern_type']})\n")

    logging.debug(f"패턴 분석 결과가 {analysis_file}에 저장되었습니다.")


def quick_pattern_check():
    """
    빠른 패턴 확인 (실시간)
    """
    logging.debug("LosslessCut 창 이름 빠른 확인 ===")

    try:
        window_titles = get_window_titles()
        losslesscut_windows = [title for title in window_titles if "LosslessCut" in title]

        if losslesscut_windows:
            logging.debug(f"LosslessCut 창 {len(losslesscut_windows)}개 감지:")
            for i, title in enumerate(losslesscut_windows, 1):
                pattern_info = analyze_window_title_pattern(title)
                logging.debug(f"{i}. {title}")
                logging.debug(f"패턴: {pattern_info['pattern_type']}")
                logging.debug(f"상태: {pattern_info['state']}")
                if pattern_info['filename']:
                    logging.debug(f"파일명: {pattern_info['filename']}")
        else:
            logging.debug("LosslessCut 창이 감지되지 않음")

    except Exception as e:
        logging.debug(f"확인 중 오류: {e}")
