import os
import traceback

from colorama import init as pk_colorama_init

#
# from pkg_py.system_object.500_live_logic import ensure_pnx_made, get_value_completed, get_values_from_historical_file, get_n
# from pkg_py.system_object.500_live_logic import ensure_files_organized_by_ngram
# from pkg_py.system_object.static_logic import D_DOWNLOADS, D_PK_WORKING
#, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED, D_PKG_TXT

if __name__ == "__main__":
    try:
        ensure_colorama_initialized_once()

        f_historical = rf'{D_PKG_TXT}/historical_{get_n(__file__)}.txt'
        historical_d_workings = get_values_from_historical_file(f_historical=f_historical)

        d_working = get_value_completed(key_hint='d_working=', values=[os.getcwd(), D_PK_WORKING, D_PROJECT, D_DOWNLOADS])
        token_splitter_pattern = get_value_completed(key_hint='token_splitter_pattern=', values=[
            r"\s+",  # 공백
            r"[_]",  # 언더바(_)만 기준으로 나눔
            r"[-]",  # 하이픈(-)만 기준으로 나눔
            r"[ _\-]+",  # 공백, 언더바(_), 하이픈(-) 중 하나 이상이 연속되면 분리
            r"[ _\-]+",  # 공백, 언더바, 하이픈
            r"[\[\]_\\-]+",  # 대괄호([, ]), 언더바(_), 하이픈(-) 중 하나 이상 기준 (기호까지 포함)
            r"[\W_]+",  # 영문자/숫자 외 모든 문자(기호 포함) 및 언더바(_) 기준으로 분리
            r"\.",  # 마침표(.) 기준으로 분리 (확장자나 버전 구분에 유용)
        ])
        pk_ensure_files_organized_by_ngram(token_splitter_pattern, d_working)

    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        
