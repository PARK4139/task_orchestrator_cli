from functions.ensure_spoken import ensure_spoken
from functions.ensure_popup_opened import ensure_popup_opened
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


def calculate_similarity(target: str, window_title: str) -> float:
    """창 제목과 타겟의 유사도 계산 - 완전히 동일한 파일명만 매칭"""
    import os

    target_lower = target.lower()
    title_lower = window_title.lower()

    # 파일명 (확장자 제외)
    target_name = os.path.splitext(target)[0].lower()

    # 가장 엄격한 매칭: 창 제목이 파일명과 정확히 일치하는 경우만
    # 1. 창 제목이 파일명과 정확히 일치 (확장자 포함)
    if title_lower == target_lower:
        return 1.0

    # 2. 창 제목이 파일명과 정확히 일치 (확장자 제외)
    if title_lower == target_name:
        return 1.0

    # 그 외의 경우는 모두 0.0 (매칭하지 않음)
    # 이전의 광범위한 매칭 제거:
    # - 파일명이 창 제목의 단어 중 하나와 일치하는 경우
    # - 창 제목이 파일명으로 시작/끝나는 경우
    # - 부분 문자열 매칭
    return 0.0


def kill_pid_psutil(pid):
    import psutil

    import logging
    try:
        proc = psutil.Process(pid)
        proc.kill()
    except Exception as e:
        logging.debug(f"PK KILL ERROR PID={pid} : {e}")
        return False
    return True


def monitor_process_state(proc, max_sec=2.5, interval=0.5):
    import time

    import logging
    start = time.time()
    steps = int(max_sec / interval)
    logging.debug(f"️ Start monitoring PID={proc.pid}")

    for _ in range(steps):
        try:
            if not proc.is_running():
                break
            cpu = proc.cpu_percent()
            mem = proc.memory_info().rss / (1024 * 1024)
            th = proc.num_threads()
            logging.debug(f"PID={proc.pid} CPU={cpu:.1f}% MEM={mem:.1f}MB TH={th}")
            time.sleep(interval)
        except Exception:
            break

    elapsed = time.time() - start
    logging.debug(f"️ End monitoring PID={proc.pid}")

    if proc.is_running():
        logging.debug(f"‼️ FORCED TIMEOUT: PID={proc.pid} took {elapsed:.2f}s")
    elif elapsed > max_sec:
        logging.debug(f"️ PK KILL PID={proc.pid} TIMEOUT_ELAPSED={elapsed:.2f}s")





@ensure_seconds_measured
def ensure_process_killed_by_window_title(window_title: str):
    import win32process

    import logging
    from sources.functions.get_window_titles_matches import get_window_titles_matches
    from sources.objects.pk_local_test_activate import LTA
    matches = get_window_titles_matches(window_title)
    if not matches:
        logging.debug(f"No window found '{window_title}'")
        return

    logging.debug(f"Found {len(matches)} window(s). Similarity check:")
    for hwnd, title, is_similar in matches:
        sim_mark = "" if is_similar else "  "
        logging.debug(f"{sim_mark} hwnd={hwnd} title={title}")

    # 창 핸들을 기준으로 중복 제거 (동일한 창은 하나만 선택)
    # 모든 창이 같은 PID를 공유하므로 창 핸들로 구분
    unique_windows = {}
    for hwnd, title, similarity in matches:
        if hwnd not in unique_windows:
            unique_windows[hwnd] = (hwnd, title, similarity)

    if not unique_windows:
        logging.debug(f"windows not found to kill")
        return

    # 가장 오래된 창 1개만 선택 (첫 번째 창 핸들)
    first_hwnd = list(unique_windows.keys())[0]
    best_match_hwnd, best_match_title, _ = unique_windows[first_hwnd]
    _, pid = win32process.GetWindowThreadProcessId(best_match_hwnd)

    logging.debug(f"Using best match title: {best_match_title} (HWND={first_hwnd}, PID={pid}, 1개만 종료) {'%%%FOO%%%' if LTA else ''}")

    # 특정 창만 닫기 (PID로 프로세스 종료하지 않음)
    try:
        import win32gui
        import win32con

        # 창을 직접 닫기
        win32gui.PostMessage(best_match_hwnd, win32con.WM_CLOSE, 0, 0)
        logging.debug(f"창 닫기 요청 완료: {best_match_title} (HWND={first_hwnd})")

    except Exception as e:
        logging.debug(f"창 닫기 실패: {e}")
