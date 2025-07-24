



from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style


def should_i_make_directory_for_a2z_with_timestamp_as_gui_v2():
    import traceback

    import inspect

    func_n = inspect.currentframe().f_code.co_name

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
        pk_print(
            f'''[ {get_time_as_('now')} ] work_ns={work_n}  {'%%%FOO%%%' if LTA else ''}''')
        if work_n == "":
            pk_print(
                f'''[ {get_time_as_('now')} ] work_n가 입력되지 않았습니다  {'%%%FOO%%%' if LTA else ''}''')
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
        pnx = get_pnx_os_style(pnx)
        if is_pnx_required(pnx):
            return
        pk_print(str_working=rf'''pnx="{pnx}"  {'%%%FOO%%%' if LTA else ''}''')
        pk_print(str_working=rf'''work_n="{work_n}"  {'%%%FOO%%%' if LTA else ''}''')
        timestamp = get_time_as_("yyyy MM dd (weekday) HH mm")
        pnx_new = rf"{pnx}\{timestamp} {work_n}"
        pk_print(str_working=rf'''pnx_new="{pnx_new}"  {'%%%FOO%%%' if LTA else ''}''')
        ensure_pnx_made(pnx=pnx_new, mode="d")
        pnx = pnx_new
        cmd = rf'explorer "{pnx}"'
        cmd_to_os(cmd=cmd, mode="a")
        return
    except:
        pk_print(f"{traceback.format_exc()}")
