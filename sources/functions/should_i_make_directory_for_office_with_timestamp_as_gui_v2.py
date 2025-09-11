def should_i_make_directory_for_office_with_timestamp_as_gui_v2():
    from sources.functions import ensure_pnx_made, get_time_as_
    from sources.functions.is_pnx_required import is_pnx_required
    from sources.objects.pk_gui_util import should_i_do

    from sources.objects.pk_local_test_activate import LTA
    from sources.functions.ensure_command_executed import ensure_command_executed
    import logging
    from pathlib import Path
    import traceback

    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    try:
        work_n = None
        pnx = None
        txt_clicked = None
        function = None
        txt_written = None
        txt_clicked, function, txt_written = should_i_do(
            prompt="업무명을 입력해주세요",
            btn_list=["입력", "n"],
            function=None,
            auto_click_negative_btn_after_seconds=30,
            title=f"{func_n}()",
            input_box_mode=True,
        )
        if txt_clicked != "입력":
            return
        work_n = txt_written
        work_n = work_n.strip()
        work_n = work_n.replace("\"", "")
        logging.debug(f'''[ {get_time_as_('now')} ] work_ns={work_n}  {'%%%FOO%%%' if LTA else ''}''')
        if work_n == "":
            logging.debug(    f'''[ {get_time_as_('now')} ] work_n가 입력되지 않았습니다  {'%%%FOO%%%' if LTA else ''}''')
            return

        txt_clicked, function, txt_written = should_i_do(
            prompt="어느 경로에 만들까요?",
            btn_list=["입력", "n"],
            function=None,
            auto_click_negative_btn_after_seconds=30,
            title=f"{func_n}()",
            input_box_mode=True,
        )
        if txt_clicked != "입력":
            return
        pnx = txt_written
        pnx = Path(pnx)
        if is_pnx_required(pnx):
            return
        logging.debug(rf'''pnx="{pnx}"  {'%%%FOO%%%' if LTA else ''}''')
        logging.debug(rf'''work_n="{work_n}"  {'%%%FOO%%%' if LTA else ''}''')
        timestamp = get_time_as_("yyyy MM dd (weekday) HH mm")
        pnx_new = rf"{pnx}\{timestamp} {work_n}"
        logging.debug(rf'''pnx_new="{pnx_new}"  {'%%%FOO%%%' if LTA else ''}''')
        ensure_pnx_made(pnx=pnx_new, mode="d")
        pnx = pnx_new
        cmd = rf'explorer "{pnx}"'
        ensure_command_executed(cmd=cmd, mode="a")
        return
    except:
        logging.debug(f"{traceback.format_exc()}")
