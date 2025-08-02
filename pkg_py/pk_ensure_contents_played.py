import os
import sys

#  import sleep, add_to_potplayer_playlist
from pkg_py.functions_split.ensure_printed import ensure_printed
# from pkg_py.system_object.500_live_logic import get_pnxs_from_d_working
from pkg_py.pk_core_class import PkSqlite3DB

from colorama import init as pk_colorama_init

#, D_PROJECT

pkg_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if pkg_path not in sys.path:
    sys.path.append(pkg_path)

if __name__ == "__main__":
    try:
        ensure_colorama_initialized_once()

        pk_db = PkSqlite3DB()
        db_id = 'working_directory_to_ensure_contents_played'
        pk_db.reset_values(db_id=db_id)
        working_directory_to_ensure_contents_played = pk_db.get_values(db_id=db_id)
        pk_db.save_answer(question="Select a directory to play the contents.", options=working_directory_to_ensure_contents_played, db_id=db_id)

        if not working_directory_to_ensure_contents_played or not os.path.isdir(working_directory_to_ensure_contents_played):
            print(f"[오류] 유효한 디렉토리가 선택되지 않았습니다: {working_directory_to_ensure_contents_played}")
            sys.exit("pk system quit")

        # 초기 상태 설정
        previous_state = get_pnxs_from_d_working(d_working=working_directory_to_ensure_contents_played)
        loop_cnt = 0
        while True:
            loop_cnt += 1
            if loop_cnt == 1:
                print(f"[{loop_cnt}] 첫 실행 - 전체 파일 재생")
                for file_path in previous_state:
                    add_to_potplayer_playlist(file_path)
            else:
                print(f"[{loop_cnt}] 변경 사항 확인 중...")

                # 현재 파일 상태 조회
                new_state = get_pnxs_from_d_working(working_directory_to_ensure_contents_played)

                # 추가된 파일만 추출
                added_files = list(set(new_state) - set(previous_state))
                if added_files:
                    print(f"[{loop_cnt}] 새로 추가된 파일 감지됨: {added_files}")
                    for file_path in added_files:
                        add_to_potplayer_playlist(file_path)
                else:
                    print(f"[{loop_cnt}] 변화 없음.")

                previous_state = new_state

            ensure_slept(minutes=5)  # 5분 대기

    except Exception as e:
        import traceback

        traceback.print_exc()
        # 예외 처리
        ensure_printed(f'{UNDERLINE}예외발생 s\n\n', print_color='red')
        ensure_printed(f'{traceback.format_exc()}\n', print_color='red')
        ensure_printed(f'{UNDERLINE}예외발생 e\n\n', print_color='red')
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        ensure_printed(script_to_run_python_program_in_venv)
