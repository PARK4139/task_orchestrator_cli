from functions.ensure_spoken import ensure_spoken
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


# @ensure_function_return_ttl_cached(ttl_seconds=5, maxsize=64)
@ensure_seconds_measured
def is_gemini_installed():
    import logging
    from sources.functions.get_gemini_version_installed import get_gemini_version_installed

    stdout_lines, stderr_lines = get_gemini_version_installed()  # 튜플 언패킹

    # stdout_lines 처리
    for std_str in stdout_lines:
        if isinstance(std_str, str) and "gemini" in std_str.lower() and "not recognized" in std_str.lower():  # 더 견고한 확인
            logging.debug(f'gemini is not installed')
            ensure_spoken(f'gemini 가 설치되지 않았습니다.')
            return False

    # stdout_lines에서 버전 확인
    for std_str in stdout_lines:
        if isinstance(std_str, str) and len(std_str.split(".")) >= 2:
            logging.debug(f'gemini is installed')
            ensure_spoken(f'gemini 가 설치되어 있습니다.')
            return True  # 버전을 찾으면 즉시 True 반환

    # stdout이나 stderr 모두 설치 또는 오류를 명확히 나타내지 않으면 설치되지 않은 것으로 간주
    logging.debug(f'gemini installation status inconclusive.')
    ensure_spoken(f'gemini 설치 상태를 확인할 수 없습니다.')
    return False  # 명확한 표시가 없으면 기본적으로 False 반환
