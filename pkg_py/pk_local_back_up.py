if __name__ == "__main__":
    try:
        import traceback

        from colorama import init as pk_colorama_init

        # from pkg_py.system_object.500_live_logic import pk_deprecated_get_d_current_n_like_person, get_f_current_n, pk_copy, assist_to_upload_pnx_to_git, get_time_as_, get_pk_token, kill_os, does_pnx_exist, LTA, get_value_completed
        #
        # from pkg_py.system_object.static_logic import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED, D_PKG_TOML, D_PK_MEMO
        # from pkg_py.system_object.static_logic import D_ARCHIVED
        # from pkg_py.system_object.500_live_logic import pk_back_up_pnx_without_venv_and_idea
        # from pkg_py.system_object.500_live_logic import pk_copy, pk_back_up_pnx, is_day
        # from pkg_py.system_object.500_live_logic import pk_back_up_pnx
        # from pkg_py.system_object.static_logic import D_PROJECT, D_DOWNLOADS

        pk_colorama_init_once()

        # 백업 정책
        # .venv 데이터 특성은 용량 큼, 자주 바뀌지 않음.-> uv + pyproject.toml + uv.lock 으로 대체
        # ; half_month : 매월 15일마다 저빈도로 백업을 수행한다.

        pnx_working = get_value_completed(key_hint='pnx_working=', values=[D_PROJECT, D_PK_MEMO])

        # 로컬백업
        f = pk_back_up_pnx_without_venv_and_idea(pnx_working=pnx_working, d_dst=D_ARCHIVED, with_timestamp=1)
        if not does_pnx_exist(f):
            pk_print(f'''데일리 로컬백업 {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        elif does_pnx_exist(f):
            pk_print(f'''데일리 로컬백업 {'%%%FOO%%%' if LTA else ''}''', print_color='green')

        # 로컬백업
        # if is_day(dd=15):
        #     f = pk_back_up_pnx(pnx_working=pnx_working, d_dst=D_ARCHIVED)
        #     if not does_pnx_exist(f):
        #         pk_print(f'''15일 전체 로컬백업 {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        #     elif does_pnx_exist(f):
        #         pk_print(f'''15일 전체 로컬백업 {'%%%FOO%%%' if LTA else ''}''', print_color='green')

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)

    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        
