import traceback

from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE


def ensure_spoken_v2(str_working, comma_delay=1.00, thread_join_mode=False):
    try:
        import inspect
        from pkg_py.functions_split.is_containing_special_characters_with_thread import is_containing_special_characters_with_thread
        from pkg_py.functions_split.ensure_spoken import ensure_spoken
        from pkg_py.functions_split.remove_special_characters import remove_special_characters
        from pkg_py.system_object.etc import PLAYING_SOUNDS

        import threading
        from functools import partial
        import pyglet

        def stop_all_sounds():
            playing_sounds = PLAYING_SOUNDS
            for player in playing_sounds:
                player.pause()  # 또는 player.stop()

        stop_all_sounds()
        PYGLET_PLAYER = None
        if PYGLET_PLAYER is not None:
            pass
        else:
            PYGLET_PLAYER = pyglet.media.Player()
            if PYGLET_PLAYER.playing:
                PYGLET_PLAYER.pause()

        async def process_thread_speak(str_working):
            # while not exit_event.is_set(): # 쓰레드 이벤트 제어
            func_n = inspect.currentframe().f_code.co_name
            str_working = str(str_working)
            str_working = str_working.strip()
            if str_working == "":
                return None
            if is_containing_special_characters_with_thread(text=str_working):
                str_working = remove_special_characters(text=str_working)
            while 1:
                working_list = [x.strip() for x in str_working.replace(".", ",").split(
                    ",")]  # from "abc,abc.abc,abc." to ["abc","abc","abc","abc"] # , or . 를 넣으면 나누어 읽도록 업데이트
                working_list = [x for x in working_list if x.strip()]  # 리스트 요소 "" remove,  from ["", A] to [A]
                for str_working in working_list:
                    ensure_spoken(str_working, after_delay=comma_delay)
                    pass
                return None

        # 비동기 이벤트 루프 설정 (simple for void async processing)
        def process_thread_loop(ment):
            import asyncio
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(process_thread_speak(ment))

        # 비동기 이벤트 루프 exec 할 쓰레드 설정 (simple for void async processing)
        thread = threading.Thread(target=partial(process_thread_loop, str_working),
                                  name="thread_for_speak")  # Q: 왜 thread.name 의 case 는 다른거야 ?  wrtn: 네, 스레드의 이름은 일반적으로 대소문자를 구분하지 않습니다.
        thread.start()
        if thread_join_mode == 1:
            thread.join()
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
