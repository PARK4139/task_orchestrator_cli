def ensure_work_directory_created():
    import textwrap
    import traceback

    from functions import get_time_as_
    from functions.ensure_embeded_script_created import ensure_embeded_script_created
    from functions.ensure_pnx_opened_by_ext import ensure_pnx_opened_by_ext
    from functions.get_caller_n import get_caller_n
    from functions.get_nx import get_nx
    from objects.pk_map_texts import PkTexts
    from objects.task_orchestrator_cli_directories import D_PK_WORKING

    import inspect
    import logging

    from functions.ensure_value_completed_advanced import ensure_value_completed_advanced

    try:
        from functions.get_caller_n import get_caller_n
        func_n = get_caller_n()

        loop_cnt = 1
        while 1:
            if loop_cnt == 1:
                key_name = "진행여부"
                selected = ensure_value_completed_advanced(key_name=key_name, func_n=func_n, options=[PkTexts.YES, PkTexts.NO])
                ok = selected
                if not ok == PkTexts.YES:
                    return

            d_destination_emergency = D_PK_WORKING / "급한일"
            d_destination_emergency_todo = D_PK_WORKING / "급한일" / "덜한일"
            d_destination_done = D_PK_WORKING / "급한일" / "처리한일"
            d_destination_not_emergency = D_PK_WORKING / "안급한일"

            key_name = "업무종류"
            options = [get_nx((d_destination_emergency)), get_nx((d_destination_emergency_todo)), get_nx((d_destination_done)), get_nx((d_destination_not_emergency)), ]
            selected = ensure_value_completed_advanced(key_name=key_name, func_n=func_n, options=options)
            work_type = selected

            key_name = "업무명"
            from functions.get_caller_n import get_caller_n
            func_n = get_caller_n()
            selected = ensure_value_completed_advanced(key_name=key_name, func_n=func_n)
            work_name = selected

            # key_name = "생성경로"
            # from functions.get_caller_n import get_caller_n
        func_n = get_caller_n()
            # selected = ensure_value_completed_advanced(key_name=key_name, func_n=func_n)
            # d_destination = selected

            # 생성경로
            d_destination = None
            if work_type == get_nx(d_destination_emergency):
                d_destination = d_destination_emergency
            elif work_type == get_nx(d_destination_emergency_todo):
                d_destination = d_destination_emergency_todo
            elif work_type == get_nx(d_destination_done):
                d_destination = d_destination_done
            elif work_type == get_nx(d_destination_not_emergency):
                d_destination = d_destination_not_emergency

            # timestamp = get_time_as_("yyyy MM dd weekday HHmm")
            timestamp = get_time_as_("yyyy MM dd weekday")
            d_working_destinaion_with_time_stamp = None
            try:
                work_name = work_name.strip()

                if not d_destination.exists():
                    d_destination.mkdir()
                d_work_directory_destination = d_destination / rf"{timestamp}_{work_name}"
                logging.info(f"work_name={work_name}")
                logging.info(f"d_work_directory_destination={d_work_directory_destination}")
                if d_work_directory_destination.exists():
                    d_working_destinaion_with_time_stamp = d_work_directory_destination
                else:
                    d_work_directory_destination.mkdir()

                d_working_destinaion_with_time_stamp = d_work_directory_destination
            except Exception as e:
                logging.debug(f"Error: {str(e)}")
                logging.debug(f"traceback.print_exc()={traceback.print_exc()}")

            if d_working_destinaion_with_time_stamp.exists():
                ensure_pnx_opened_by_ext(d_working_destinaion_with_time_stamp)

            key_name = "메모파일생성여부"
            selected = ensure_value_completed_advanced(key_name=key_name, func_n=func_n, options=[PkTexts.YES, PkTexts.NO])
            ok = selected
            if not ok == PkTexts.YES:
                break

            f_work_memo = None
            if d_working_destinaion_with_time_stamp is not None:
                if d_working_destinaion_with_time_stamp.exists():
                    f_work_memo = d_working_destinaion_with_time_stamp / f"{work_type}.txt"
                else:
                    f_work_memo = d_destination / f"{work_type}.txt"
            batch_content = textwrap.dedent(f'''
                 # 할일
                 n. 
                 n. 
                 n. 
                 
                               ''').lstrip()
            ensure_embeded_script_created(script_file=f_work_memo, script_content=batch_content)
            if f_work_memo.exists():
                ensure_pnx_opened_by_ext(f_work_memo)

    except Exception as e:
        logging.debug(f"e={str(e)}")
        logging.debug(f"traceback.print_exc()={traceback.print_exc()}")
