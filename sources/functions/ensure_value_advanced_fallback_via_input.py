from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_value_advanced_fallback_via_input(pk_file_list: list[str], last_selected: str | None):
    import logging

    import os
    logging.debug("※ fzf 미설치 → fallback 선택 모드 사용")
    for idx, fpath in enumerate(pk_file_list):
        fname = os.path.basename(fpath)
        mark = " <- 최근 실행" if fpath == last_selected else ""
        logging.debug(f"[{idx}] {fname}{mark}")
    try:
        choice = input("실행할 번호를 입력하세요 (Enter로 취소): ").strip()
        if not choice:
            return None
        return pk_file_list[int(choice)]
    except (ValueError, IndexError):
        return None
