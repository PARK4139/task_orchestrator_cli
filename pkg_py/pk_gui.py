import sys
from functools import partial

from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_f_current_n import get_f_current_n
from pkg_py.functions_split.pk_deprecated_get_d_current_n_like_person import pk_deprecated_get_d_current_n_like_person

if __name__ == '__main__':
    debug_mode = True
    try:
        # todo : sample : gui component
        import pyautogui
        pyautogui.alert("{msg}")  # 예제 동작: 알림창 표시

        # todo : sample : gui component
        cmd = rf'explorer "{__file__}"'
        txt_clicked, function, txt_written = should_i_do(
            prompt=rf"___________",
            btn_list=[_2025.POSITIVE, _2025.NEGATIVE],
            function=partial(cmd_to_os, cmd),
            auto_click_negative_btn_after_seconds=30,
            title=f"___________",
            input_box_mode=True,
            input_box_text_default="______________",
        )
        if txt_clicked == _2025.NEGATIVE:
            pk_print(str_working=f'  for txt_clicked != _2025.POSITIVE', print_color='red')
            sys.exit(1)
        user_input = txt_written
        # ipdb.set_trace()

        # todo : sample : gui component 2
        question = get_txt_dragged()
        txt_clicked, function, txt_written = should_i_do(
            prompt=rf"드래그한 내용을 인터넷에 질문할까요?",
            btn_list=[_2025.POSITIVE, _2025.NEGATIVE],
            function=partial(ask_to_google, question=question),
            auto_click_negative_btn_after_seconds=30,
            title=f"___________",
            input_box_mode=True,
            input_box_text_default=question,
        )
        if txt_clicked == _2025.NEGATIVE:
            pk_print(f'''{_2025.NEGATIVE} pressed %%%FOO%%%''', print_color='red')
            sys.exit(1)
        if txt_clicked ==    _2025.POSITIVE:
            pk_print(f'''txt_clicked={txt_clicked} %%%FOO%%%''', print_color="blue")
            pk_print(f'''txt_written={txt_written} %%%FOO%%%''', print_color="blue")
        else:
            # break
            pass
        # previous_question = dialog.input_box.text()

        # move
        # friday.move_window_to_pycharm(debug_mode=debug_mode)

    except Exception as e:
        # red
        import traceback

        pk_print(str_working=f'{PK_UNDERLINE}예외발생 s\n\n', print_color='red')
        pk_print(str_working=f'{traceback.format_exc()}\n', print_color='red')
        pk_print(str_working=f'{PK_UNDERLINE}예외발생 e\n\n', print_color='red')

        # yellow
        f_current= get_f_current_n()
        d_current=pk_deprecated_get_d_current_n_like_person()
        pk_print(str_working=f'{PK_UNDERLINE}[Debugging Note] s\n', print_color="yellow")
        pk_print(str_working=f'f_current={f_current}\nd_current={d_current}\n', print_color="yellow")
        pk_print(str_working=f'{PK_UNDERLINE}[Debugging Note] e\n', print_color="yellow")
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        pk_print(script_to_run_python_program_in_venv)

        # debug
        import ipdb

        ipdb.set_trace()
