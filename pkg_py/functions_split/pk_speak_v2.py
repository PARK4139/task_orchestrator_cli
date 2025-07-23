def pk_speak_v2(working_str, comma_delay=1.00, thread_join_mode=False):
    import inspect
    from pkg_py.functions_split.is_containing_special_characters_with_thread import is_containing_special_characters_with_thread
    from pkg_py.functions_split.pk_speak import pk_speak
    from pkg_py.functions_split.remove_special_characters import remove_special_characters
    from pkg_py.pk_system_object.etc import PLAYING_SOUNDS

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

    async def process_thread_speak(working_str):
        # while not exit_event.is_set(): # 쓰레드 이벤트 제어
        func_n = inspect.currentframe().f_code.co_name
        working_str = str(working_str)
        working_str = working_str.strip()
        if working_str == "":
            return None
        if is_containing_special_characters_with_thread(text=working_str):
            working_str = remove_special_characters(text=working_str)
        while 1:
            working_list = [x.strip() for x in working_str.replace(".", ",").split(
                ",")]  # from "abc,abc.abc,abc." to ["abc","abc","abc","abc"] # , or . 를 넣으면 나누어 읽도록 업데이트
            working_list = [x for x in working_list if x.strip()]  # 리스트 요소 "" remove,  from ["", A] to [A]
            for working_str in working_list:
                pk_speak(working_str, after_delay=comma_delay)
                pass
            return None

    # 비동기 이벤트 루프 설정 (simple for void async processing)
    def process_thread_loop(ment):
        import asyncio
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(process_thread_speak(ment))

    # 비동기 이벤트 루프 exec 할 쓰레드 설정 (simple for void async processing)
    thread = threading.Thread(target=partial(process_thread_loop, working_str),
                              name="thread_for_speak")  # Q: 왜 thread.name 의 case 는 다른거야 ?  wrtn: 네, 스레드의 이름은 일반적으로 대소문자를 구분하지 않습니다.
    thread.start()
    if thread_join_mode == 1:
        thread.join()
