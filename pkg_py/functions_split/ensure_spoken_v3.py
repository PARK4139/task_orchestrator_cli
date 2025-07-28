def ensure_spoken_v3(str_working, segment_delay=0.90, queue_mode=False):
    import inspect
    import traceback

    from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
    from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE

    from pkg_py.functions_split.debug_call_depth import debug_call_depth
    import threading
    import queue

    from pkg_py.functions_split.is_containing_special_characters_with_thread import is_containing_special_characters_with_thread
    from pkg_py.functions_split.ensure_spoken import ensure_spoken
    from pkg_py.functions_split.remove_special_characters import remove_special_characters
    from pkg_py.system_object.etc import PLAYING_SOUNDS

    func_n = inspect.currentframe().f_code.co_name
    depth = debug_call_depth(func_n)
    limit_of_call_depth = 10

    if limit_of_call_depth >= depth:
        print(f"[ERROR] Too deep: depth={depth}")
        return

    try:
        # 전역 음성 큐 및 재생 쓰레드 (초기화 1회만)
        if not hasattr(ensure_spoken_v3, "_queue"):
            ensure_spoken_v3._queue = queue.Queue()
            ensure_spoken_v3._thread_started = False

        def stop_all_sounds():
            for player in PLAYING_SOUNDS:
                try:
                    player.pause()
                    player.delete()
                except Exception:
                    pass
            PLAYING_SOUNDS.clear()

        def process_queue():
            while True:
                try:
                    seg, delay = ensure_spoken_v3._queue.get()
                    ensure_spoken(seg, after_delay=delay)
                except Exception:
                    pass
                ensure_spoken_v3._queue.task_done()

        # 최초 1회만 큐 소비 쓰레드 시작
        if queue_mode and not ensure_spoken_v3._thread_started:
            threading.Thread(
                target=process_queue,
                name="thread_speak_queue",
                daemon=True
            ).start()
            ensure_spoken_v3._thread_started = True

        # 문자열 전처리
        str_working = str(str_working).strip()
        if not str_working:
            return

        if is_containing_special_characters_with_thread(text=str_working):
            str_working = remove_special_characters(text=str_working)

        working_list = [x.strip() for x in str_working.replace(".", ",").split(",") if x.strip()]

        if queue_mode:
            # 큐 모드: 순서대로 재생
            for seg in working_list:
                ensure_spoken_v3._queue.put((seg, segment_delay))
        else:
            # 즉시 모드: 기존 재생 중단 후 바로 실행
            stop_all_sounds()
            for seg in working_list:
                ensure_spoken(seg, after_delay=segment_delay)

    except Exception as e:
        ensure_do_exception_routine(traceback=traceback, exception=e)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
