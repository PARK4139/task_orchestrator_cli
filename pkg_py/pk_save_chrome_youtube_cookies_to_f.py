import traceback

# , D_PROJECT
#  import deprecated_get_d_current_n_like_person, get_f_current_n, ensure_slept
from pkg_py.functions_split.ensure_printed import ensure_printed

# pkg_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
# if pkg_path not in sys.path:
#     sys.path.append(pkg_path)
# from pkg_py.system_object.500_live_logic import save_chrome_youtube_cookies_to_f

if __name__ == "__main__":
    try:
        save_chrome_youtube_cookies_to_f()

        while 1:
            ensure_slept(hours=24)
    except Exception as e:
        traceback.print_exc()
        # 예외 처리
        ensure_printed(str_working=f'{PK_UNDERLINE}예외발생 s\n\n', print_color='red')
        ensure_printed(str_working=f'{traceback.format_exc()}\n', print_color='red')
        ensure_printed(str_working=f'{PK_UNDERLINE}예외발생 e\n\n', print_color='red')

        # 디버깅 노트 출력
        f_current= get_f_current_n()
        d_current=pk_deprecated_get_d_current_n_like_person()
        ensure_printed(str_working=f'{PK_UNDERLINE}[Debugging Note] s\n', print_color="yellow")
        ensure_printed(str_working=f'f_current={f_current}\nd_current={d_current}\n', print_color="yellow")
        ensure_printed(str_working=f'{PK_UNDERLINE}[Debugging Note] e\n', print_color="yellow")
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        ensure_printed(script_to_run_python_program_in_venv)
