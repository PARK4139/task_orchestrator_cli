def kill_process_v16(window_title: str, exact: bool = True):
    import psutil
    import logging
    from concurrent.futures import ThreadPoolExecutor

    window_title = window_title.strip()

    try:
        import win32gui
        import win32process
    except ImportError as e:
        logging.error(f"[IMPORT ERROR] {e}. Please install pywin32.")
        return

    def enum_handler(hwnd, matched_hwnds):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd).strip()
            if not title:
                return
            logging.debug(f"[ENUM] hwnd={hwnd}, title='{title}', target='{window_title}'")
            if exact:
                if title.lower() == window_title.lower():
                    matched_hwnds.append((hwnd, title))
                    logging.info(f"[MATCHED:EXACT] '{title}'")
            else:
                if window_title.lower() in title.lower():
                    matched_hwnds.append((hwnd, title))
                    logging.info(f"[MATCHED:PARTIAL] '{title}'")

    matched_hwnds = []
    try:
        win32gui.EnumWindows(lambda h, _: enum_handler(h, matched_hwnds), None)
    except Exception as e:
        logging.error(f"[EnumWindows ERROR] {e}")
        return

    if not matched_hwnds:
        logging.warning(f"[SKIP] No window matched for: '{window_title}' (exact={exact})")
        return

    logging.info(f"[INFO] Found {len(matched_hwnds)} matched window(s) for '{window_title}'")

    matched_pids = set()
    for hwnd, title in matched_hwnds:
        try:
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            logging.info(f"[HWND->PID] title='{title}' → pid={pid}")
            matched_pids.add(pid)
        except Exception as e:
            logging.warning(f"[WARN] Failed to get PID from hwnd={hwnd}: {e}")

    if not matched_pids:
        logging.error(f"[ERROR] No valid PID found for window title: '{window_title}'")
        return

    failed_pids = []

    def try_kill_pid(pid):
        try:
            proc = psutil.Process(pid)
            exe = proc.name().lower()
            if exe == "cmd.exe":
                logging.warning(f"[SKIP] Not killing cmd.exe (PID={pid})")
                return

            # ✅ 종료 전에 실행
            # ensure_pk_system_exit_silent()

            proc.terminate()
            try:
                proc.wait(timeout=1)
            except psutil.TimeoutExpired:
                proc.kill()
                proc.wait(timeout=1)
            logging.info(f"[KILLED] PID={pid} ('{window_title}') exe='{exe}'")
        except Exception as e:
            failed_pids.append(pid)
            logging.error(f"[FAILED] PID={pid} error: {e}")

    with ThreadPoolExecutor(max_workers=min(4, len(matched_pids))) as executor:
        executor.map(try_kill_pid, matched_pids)

    if failed_pids:
        logging.error(f"[FAILED PIDs] {sorted(failed_pids)}")
    # ipdb.set_trace()  # 🔍 디버깅 시작 지점


