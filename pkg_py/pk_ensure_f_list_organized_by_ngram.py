from pkg_py.functions_split.get_value_completed import get_value_completed

if __name__ == "__main__":
    try:
        import os
        # from pkg_py.system_object.500_live_logic import copy, pk_ensure_f_list_organized_by_ngram, get_value_completed
        #, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
        #
        # from pkg_py.system_object.static_logic import D_DOWNLOADS, D_PROJECT, D_PK_WORKING

        d_working = get_value_completed(key_hint ='d_working=', values=[os.getcwd(), D_PK_WORKING, D_PROJECT, D_DOWNLOADS])
        token_splitter_pattern = get_value_completed(key_hint='token_splitter_pattern=', values=[
            r"\s+",  # 공백 기준으로 나눔
            r"[_]",  # 언더바(_) 기준으로 나눔
            r"[-]",  # 하이픈(-) 기준으로 나눔
            r"[ _\-]+",  # 공백, 언더바(_), 하이픈(-) 중 하나 이상이 연속되면 분리
            r"[ _\-]+",  # 공백, 언더바, 하이픈
            r"[\[\]_\\-]+",  # 대괄호([, ]), 언더바(_), 하이픈(-) 중 하나 이상 기준 (기호까지 포함)
            r"[\W_]+",  # 영문자/숫자 외 모든 문자(기호 포함) 및 언더바(_) 기준으로 분리
            r"\.",  # 마침표(.) 기준으로 분리 (확장자나 버전 구분에 유용)
        ])
        while 1:
            pk_ensure_f_list_organized_by_ngram(token_splitter_pattern, d_working)

    except:
        import traceback

        traceback_format_exc_list = traceback.format_exc().split("\n")
        ensure_printed(str_working=f'{PK_UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            # ensure_printed(str_working=f'{STAMP_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
            ensure_printed(str_working=f'{STAMP_UNIT_TEST_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        ensure_printed(str_working=f'{PK_UNDERLINE}', print_color='red')

    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        
