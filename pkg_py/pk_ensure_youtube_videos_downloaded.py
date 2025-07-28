if __name__ == "__main__":
    try:

        import os
        import sys

        from pkg_py.functions_split.download_youtube_videos import download_youtube_videos
        from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
        from pkg_py.system_object.map_massages import PkMessages2025
        from pkg_py.system_object.state_via_database import PkSqlite3DB

        pkg_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
        if pkg_path not in sys.path:
            sys.path.append(pkg_path)

        ensure_colorama_initialized_once()


        db_id = 'download_option'
        pk_db = PkSqlite3DB()
        pk_db.reset_values(db_id=db_id)
        pk_db.save_answer(question="play or skip video after download?", options=[PkMessages2025.SKIP, PkMessages2025.play], db_id=db_id)

        while 1:
            download_youtube_videos()

    except Exception as e:
        import traceback

        traceback.print_exc()
