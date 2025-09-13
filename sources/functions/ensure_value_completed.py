def ensure_value_completed(key_hint, options):
    """
    자동입력 방지 버전 - 사용자가 엔터를 쳐야만 입력이 완료되지만 자동완성 기능은 유지
    Path 객체를 문자열로 변환하여 prompt_toolkit 오류 방지

    TODO :ensure_value_completed 함수에서 key_hint 에 '?' 가 포함이 되면 tab 키로 자동완성이 안되는 이슈가 있음.
    """
    from prompt_toolkit import prompt
    from prompt_toolkit.completion import WordCompleter, FuzzyCompleter
    from prompt_toolkit.history import InMemoryHistory
    import logging
    from pathlib import Path

    from functions.get_text_cyan import get_text_cyan
    from objects.pk_etc import PK_BLANK

    from sources.functions.ensure_task_orchestrator_cli_exit_silent import ensure_task_orchestrator_cli_exit_silent
    from sources.objects.pk_map_texts import PkTexts
    from sources.functions.ensure_spoken import ensure_spoken
    from sources.functions.is_path_like import is_path_like

    # from functions.get_caller_n import get_caller_n
    # func_n = get_caller_n()
    # if key_hint.strip() == "x":
    #     ensure_spoken(f"{func_n}() exited(intended)")
    #     return None

    seen = set()
    deduped = []
    options = options + [PkTexts.SHUTDOWN]

    for option in options:
        # None 값은 건너뛰기
        if option is None:
            continue

        # 모든 타입을 안전하게 문자열로 변환
        try:
            if isinstance(option, Path):
                styled = str(option)
            elif isinstance(option, str):
                if is_path_like(option):
                    styled = Path(option)
                else:
                    styled = option
            else:
                # 기타 타입도 문자열로 변환
                styled = str(option)

            # styled가 여전히 Path 객체인 경우 추가 변환
            if hasattr(styled, 'lower') and callable(getattr(styled, 'lower')):
                # styled가 lower() 메서드를 가진 객체인 경우 (문자열 등)
                pass
            else:
                # styled가 lower() 메서드를 가지지 않은 객체인 경우 (Path 등)
                styled = str(styled)

        except Exception as e:
            # 변환 중 오류가 발생하면 문자열로 강제 변환
            logging.warning(f"Option conversion failed: {option} -> {e}")
            styled = str(option)

        if styled not in seen:
            seen.add(styled)
            deduped.append(styled)

    # fzf 스타일 실시간 검색 완성 기능 유지
    completer = FuzzyCompleter(WordCompleter(deduped, ignore_case=True))

    logging.debug(f"")
    logging.debug(f"[자동완성 사용 가이드]")
    logging.debug(f"{get_text_cyan("tab")}->자동완성")
    logging.debug(f"{get_text_cyan("방향키")}->이동")
    logging.debug(f"{get_text_cyan("Enter")}->선택")
    logging.debug(f"")
    message = rf"{key_hint}={PK_BLANK}"
    # ensure_spoken(rf"{get_easy_speakable_text(message)} 를 입력해주세요")

    option_selected = prompt(
        message=message,
        completer=completer,
        history=InMemoryHistory(),  # 빈 history 사용으로 자동입력 방지
        complete_in_thread=False,  # 백그라운드 완성 비활성화
        complete_while_typing=False,  # 타이핑 중 자동완성 비활성화
        enable_history_search=False,  # history 검색 비활성화
        mouse_support=False,  # 마우스 지원 비활성화
        multiline=False,  # 단일 라인 입력만 허용
        enable_suspend=False,  # suspend 기능 비활성화
        enable_open_in_editor=False,  # 에디터 열기 비활성화
        # complete_style="default",      # 기본 자동완성 스타일 유지
    )

    if option_selected.strip() == PkTexts.SHUTDOWN:
        ensure_task_orchestrator_cli_exit_silent()
        return
    return option_selected
