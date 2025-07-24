# from pkg_py.system_object.500_live_logic import ensure_dummy_file_exists, ensure_pnx_made, add_to_potplayer_playlist, ensure_func_info_loaded
from pkg_py.system_object.directories import D_PKG_MP4
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.functions_split.part_827_add_to_potplayer_playlist import add_to_potplayer_playlist
from pkg_py.functions_split.part_828_ensure_dummy_file_exists import ensure_dummy_file_exists
from pkg_py.functions_split.part_830_ensure_func_info_loaded import ensure_func_info_loaded


def test_add_to_potplayer_playlist_2025():
    import os
    import inspect

    func_n = inspect.currentframe().f_code.co_name

    ensure_dummy_file_exists(f"{D_PKG_MP4}/test.mp4")
    state = ensure_func_info_loaded(func_n="ensure_dummy_file_exists")["state"]
    f_dummy = ensure_func_info_loaded(func_n="ensure_dummy_file_exists")["file_pnx"]

    if state is not PkMessages2025.success:
        return

    try:
        if not os.path.isfile(F_POT_PLAYER_MINI_64_EXE):
            print(f"[{PkMessages2025.fail}] PotPlayer 실행 파일 없음: {F_POT_PLAYER_MINI_64_EXE}")
            return

        add_to_potplayer_playlist(f_dummy)
        print(f"[{PkMessages2025.success}] {func_n}() 호출 완료")

        # test_result = {
        #
        # }
        # TBD : report_test_result_to_database(test_result)
    finally:
        if os.path.exists(f_dummy):
            os.remove(f_dummy)
