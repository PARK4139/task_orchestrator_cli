import os
import sys

from pkg_py.functions_split.download_youtube_video import download_youtube_video
from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.state_via_database import PkSqlite3DB

#  import download_youtube_video
# from pkg_py.system_object.static_logic import D_PKG_DB, UNDERLINE, D_PROJECT

pkg_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if pkg_path not in sys.path:
    sys.path.append(pkg_path)

if __name__ == "__main__":
    try:
        ensure_colorama_initialized_once()

        pk_db = PkSqlite3DB()
        db_id = 'download_option'
        pk_db.reset_values(db_id=db_id)
        pk_db.save_answer(question="play or skip video after download?", options=[PkMessages2025.SKIP, PkMessages2025.play], db_id=db_id)

        pk_db = PkSqlite3DB()
        db_id = 'open historical f'  # failed list, 재시도하기 좋도록 이력을 남긴다. 성공한것은 삭제한다.
        pk_db.reset_values(db_id=db_id)
        pk_db.save_answer(question="open historical file?", options=[PkMessages2025.NO, PkMessages2025.YES], db_id=db_id)

        while 1:
            download_youtube_video()
    except Exception as e:
        import traceback

        traceback.print_exc()
