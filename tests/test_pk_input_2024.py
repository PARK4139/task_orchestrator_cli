

if __name__ == "__main__":
    try:
        import traceback

        from colorama import init as pk_colorama_init

        # from pkg_py.system_object.500_live_logic import copy, kill_self_pk_program, LTA, assist_to_load_video_at_losslesscut, pk_input_v33_nvim_theme, pk_input_v44_uv_theme
        # from pkg_py.system_object.static_logic import UNDERLINE, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED, D_PK_WORKING
        # from pkg_py.system_object.print_util import print

        colorama_init_once()

        output = pk_input_v33_nvim_theme(
            str_working="위와 같이 파일을 분류할까요? (o/x):",
            limit_seconds=5,
            return_default="o",
            fuzzy_accept=[("o", "ok", "yes", "y"), ("x", "no", "n")],
            validator=lambda s: s.lower() in {"o", "x", "yes", "no", "y", "n"},
            masked=False,
        )
        output2 = pk_input_v44_uv_theme(
            str_working="위와 같이 파일을 분류할까요? (o/x):",
            limit_seconds=5,
            return_default="o",
            fuzzy_accept=[("o", "ok", "yes", "y"), ("x", "no", "n")],
            validator=lambda s: s.lower() in {"o", "x", "yes", "no", "y", "n"},
            masked=False,
        )
        assert output==output2 , "assert error"


    except:
        # from pkg_py.system_object.print_red import print_red
        traceback_format_exc_list = traceback.format_exc().split("\n")
        print_red(UNDERLINE)
        for line in traceback_format_exc_list:
            print_red(f'{STAMP_UNIT_TEST_EXCEPTION_DISCOVERED} {line}')
        print_red(UNDERLINE)

    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        
