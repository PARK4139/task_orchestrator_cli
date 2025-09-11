from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_token_file_generated(f, token_id):
    from sources.functions.ensure_window_minimized import ensure_window_minimized
    from sources.functions.ensure_window_to_front import ensure_window_to_front
    import inspect

    from sources.functions import ensure_spoken
    from sources.functions.ensure_task_orchestrator_cli_enabled import PkTexts
    from sources.functions.ensure_window_title_replaced import ensure_window_title_replaced
    from sources.functions.ensure_task_orchestrator_cli_wrapper_window_title_replaced import ensure_task_orchestrator_cli_wrapper_window_title_replaced

    from sources.functions.get_window_title import get_window_title

    from sources.functions.ensure_text_decoded import get_text_decoded
    from sources.functions.get_master_pw import get_master_pw
    from sources.functions.does_pnx_exist import is_pnx_existing
    from sources.functions.ensure_pnx_made import ensure_pnx_made
    import logging
    from sources.functions.ensure_str_writen_to_f import ensure_str_writen_to_f
    from sources.functions.get_list_from_f import get_list_from_f
    from sources.functions.get_list_removed_by_removing_runtine import get_list_removed_by_removing_runtine
    from sources.objects.pk_local_test_activate import LTA
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    window_title_backup = get_window_title()

    try:
        ensure_window_title_replaced(window_title=func_n)
        if not is_pnx_existing(pnx=f):
            ensure_pnx_made(pnx=f, mode="f")
        logging.debug(f'''f={f}  {'%%%FOO%%%' if LTA else ''}''')
        line_list = get_list_from_f(f=f)
        line_list = get_list_removed_by_removing_runtine(working_list=line_list)
        if len(line_list) == 0:
            msg = "토큰 초기값 콘솔 입력 요청"
            ensure_spoken(msg)
            logging.debug(f'''{msg} {'%%%FOO%%%' if LTA else ''}''')

            ensure_window_to_front(func_n)
            logging.debug(f'''token_id={token_id} {'%%%FOO%%%' if LTA else ''}''')
            initial_str = input(f"initial_str({token_id})=")
            token = initial_str

            if initial_str != "":
                # 암호화된 텍스트인지 확인
                if initial_str.startswith("SECURE_"):
                    # 암호화된 텍스트인 경우 복호화 시도
                    text_decoded = get_text_decoded(text=initial_str, master_password=get_master_pw())
                    if text_decoded is not None:
                        # 복호화 성공
                        ensure_str_writen_to_f(msg=f"{text_decoded}\n", f=f, mode="w")
                        logging.debug(rf'''token({token}) is decoded and saved at {f} {'%%%FOO%%%' if LTA else ''}''')
                    else:
                        # 복호화 실패 시 원본 저장
                        ensure_str_writen_to_f(msg=f"{initial_str}\n", f=f, mode="w")
                        logging.debug(rf'''token({token}) is saved as original (decoding failed) at {f} {'%%%FOO%%%' if LTA else ''}''')
                else:
                    # 일반 텍스트인 경우 그대로 저장
                    ensure_str_writen_to_f(msg=f"{initial_str}\n", f=f, mode="w")
                    logging.debug(rf'''token({token}) is saved as plain text at {f} {'%%%FOO%%%' if LTA else ''}''')

    finally:
        ensure_window_title_replaced(window_title=window_title_backup)
        ensure_window_minimized(window_title=func_n)
