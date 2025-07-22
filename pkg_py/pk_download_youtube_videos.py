import os
import sys

#  import download_youtube_videos
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.pk_core_class import PkMents2025, PkSqlite3DB

from colorama import init as pk_colorama_init

#, D_PROJECT

pkg_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if pkg_path not in sys.path:
    sys.path.append(pkg_path)

if __name__ == "__main__":
    try:
        pk_colorama_init_once()

        pk_db = PkSqlite3DB()
        db_id = 'download_option'
        pk_db.reset_values(db_id=db_id)
        pk_db.save_answer(question="play or skip video after download?", options=[PkMessages2025.skip, PkMessages2025.play], db_id=db_id)

        while 1:
            download_youtube_videos()

    except Exception as e:
        import traceback

        traceback.print_exc()
        # 예외 처리
        pk_print(f'{UNDERLINE}예외발생 s\n\n', print_color='red')
        pk_print(f'{traceback.format_exc()}\n', print_color='red')
        pk_print(f'{UNDERLINE}예외발생 e\n\n', print_color='red')
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        pk_print(script_to_run_python_program_in_venv)
