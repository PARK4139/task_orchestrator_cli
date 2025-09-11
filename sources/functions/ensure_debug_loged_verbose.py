from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_debug_loged_verbose(traceback):
    import logging
    import tempfile

    from sources.functions.get_text_red import get_text_red
    from sources.functions.ensure_pnx_opened_by_ext import ensure_pnx_opened_by_ext

    text_to_print_raw = rf"traceback.format_exc()={traceback.format_exc()}"

    # temp 파일에 저장
    with tempfile.NamedTemporaryFile(delete=False, suffix=".log", mode="w", encoding="utf-8") as tmp_file:
        tmp_file.write(text_to_print_raw)
        tmp_path = tmp_file.name
        logging.debug(rf"tmp_path={tmp_path}")
    ensure_pnx_opened_by_ext(tmp_path)  # 파일을 기본 프로그램으로 열기

    # 콘솔 로그 출력
    text_to_print = get_text_red(text_to_print_raw)
    logging.debug(text_to_print)
