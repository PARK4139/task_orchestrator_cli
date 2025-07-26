def kill_us_keyboard():
    """
    프로세스 간 공유 메모리를 내부에서 초기화하고 사용하도록 변경
    """
    import threading
    from multiprocessing import shared_memory, Lock

    colorama_init_once()

    if get_os_n() == 'windows':
        chcp_65001()

    shm_name = "flag_to_detect_enter"
    lock = Lock()

    try:
        # 기존 공유 메모리 존재 여부 확인
        shm = shared_memory.SharedMemory(name=shm_name, create=False)
        ensure_printed(rf"기존 공유 메모리 발견, 초기화 생략 shm_name={shm_name}", print_color="green")
    except FileNotFoundError:
        ensure_printed(rf"새로운 공유 메모리 생성 shm_name={shm_name}", print_color="green")
        shm = shared_memory.SharedMemory(create=True, size=1, name=shm_name)
        shm.buf[0] = 0  # 초기값 False (0)

    def listen_enter():
        """사용자가 Enter 키를 입력하면 flag를 True로 설정"""
        try:
            existing_shm = shared_memory.SharedMemory(name=shm_name)
            flag = existing_shm.buf
        except FileNotFoundError:
            ensure_printed("listen_enter: 공유 메모리가 존재하지 않음. 종료.", print_color='red')
            return

        while 1:
            input()  # Enter 입력 대기
            with lock:
                flag[0] = 1  # flag를 True로 변경
                ensure_printed("Enter detected! flag 업데이트됨.", print_color="blue")

        existing_shm.close()

    def main_loop():
        """flag 값이 True가 되면 특정 작업 수행 후 다시 False로 초기화"""
        try:
            existing_shm = shared_memory.SharedMemory(name=shm_name)
            flag = existing_shm.buf
        except FileNotFoundError:
            ensure_printed("main_loop: 공유 메모리가 존재하지 않음. 종료.", print_color='red')
            return

        while 1:
            # exec 할 명령
            f_cmd = rf"{D_PKG_WINDOWS}/pk_kill_us_keyboard.cmd"
            f_cmd = get_pnx_os_style(pnx=f_cmd)
            cmd_to_os(cmd=rf'"{f_cmd}"', encoding=Encoding.CP949)

            # sleep
            sleep_seconds = 3
            for _ in range(sleep_seconds):
                with lock:
                    if flag[0]:  # flag가 True면 리셋 후 루프 재시작
                        ensure_printed("Enter detected! Restarting loop...", print_color="white")

                        # pk_system_kill_us_keyboard.cmd (run)
                        f_cmd = rf"{D_PKG_WINDOWS}/pk_kill_us_keyboard.cmd"
                        f_cmd = get_pnx_os_style(pnx=f_cmd)
                        cmd_to_os(cmd=rf'"{f_cmd}"', encoding='utf-8')

                        flag[0] = 0  # flag를 다시 False로 초기화
                        ensure_printed(f"wait for enter  {'%%%FOO%%%' if LTA else ''}", print_color='white')
                        break
                ensure_slept(seconds=1)

        existing_shm.close()

    # thread run (in background)
    thread = threading.Thread(target=listen_enter, daemon=True)
    thread.start()

    # main loop run
    main_loop()

    # 공유 메모리 해제 (필요하면 exec )
    shm.close()
    # shm.unlink()  # 주석 해제하면 공유 메모리 삭제됨 (프로세스 간 공유 유지하려면 유지)


