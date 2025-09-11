def get_image_names_from_tasklist():
    import re
    import subprocess

    import logging

    from sources.functions.get_list_deduplicated import get_list_deduplicated
    from sources.functions.get_list_removed_element_empty import get_list_removed_empty
    from sources.functions.get_list_striped_element import get_list_striped_element
    from sources.functions.is_os_linux import is_os_linux
    from sources.functions.is_os_windows import is_os_windows

    """
    tasklist/ps 명령어의 결과에서 이미지명을 수집하고 중복을 제거한 리스트를 반환
    
    Returns:
        list: 이미지명 리스트 (중복 제거됨)
    """
    try:
        if is_os_windows():
            # Windows tasklist 명령어 실행
            try:
                result = subprocess.run(['tasklist', '/FO', 'CSV'],
                                        capture_output=True,
                                        text=True,
                                        encoding='cp949')  # Windows 한국어 인코딩
            except UnicodeDecodeError:
                # cp949 실패 시 기본 인코딩으로 재시도
                result = subprocess.run(['tasklist', '/FO', 'CSV'],
                                        capture_output=True,
                                        text=True,
                                        encoding='utf-8',
                                        errors='ignore')

            if result.returncode != 0:
                logging.debug(f"tasklist 명령어 실행 실패: {result.stderr}")
                return []

            if not result.stdout:
                logging.debug("️ tasklist 명령어 결과가 비어있습니다.")
                return []

            lines = result.stdout.strip().split('\n')

            # 첫 번째 줄은 헤더이므로 제외
            if lines and lines[0].startswith('"Image Name"'):
                lines = lines[1:]

            image_names = []

            for line in lines:
                if line.strip():
                    # CSV 형식에서 첫 번째 컬럼(이미지명) 추출
                    parts = re.findall(r'"([^"]*)"', line)
                    if parts:
                        image_name = parts[0].strip()  # 첫 번째 컬럼이 이미지명
                        if image_name and image_name.lower() != 'image name':
                            image_names.append(image_name)

        elif is_os_linux():
            # Linux ps 명령어 실행
            try:
                result = subprocess.run(['ps', 'aux'],
                                        capture_output=True,
                                        text=True,
                                        encoding='utf-8')
            except Exception as e:
                logging.debug(f"ps 명령어 실행 실패: {e}")
                return []

            if result.returncode != 0:
                logging.debug(f"ps 명령어 실행 실패: {result.stderr}")
                return []

            if not result.stdout:
                logging.debug("️ ps 명령어 결과가 비어있습니다.")
                return []

            lines = result.stdout.strip().split('\n')

            # 첫 번째 줄은 헤더이므로 제외
            if lines and 'USER' in lines[0]:
                lines = lines[1:]

            image_names = []

            for line in lines:
                if line.strip():
                    # ps aux 형식에서 마지막 컬럼(명령어) 추출
                    parts = line.split()
                    if len(parts) >= 11:
                        command = parts[10]  # 마지막 컬럼이 명령어
                        if command and command != 'COMMAND':
                            # 경로에서 파일명만 추출
                            import os
                            image_name = os.path.basename(command)
                            if image_name:
                                image_names.append(image_name)

        else:
            # macOS ps 명령어 실행
            try:
                result = subprocess.run(['ps', 'aux'],
                                        capture_output=True,
                                        text=True,
                                        encoding='utf-8')
            except Exception as e:
                logging.debug(f"ps 명령어 실행 실패: {e}")
                return []

            if result.returncode != 0:
                logging.debug(f"ps 명령어 실행 실패: {result.stderr}")
                return []

            if not result.stdout:
                logging.debug("️ ps 명령어 결과가 비어있습니다.")
                return []

            lines = result.stdout.strip().split('\n')

            # 첫 번째 줄은 헤더이므로 제외
            if lines and 'USER' in lines[0]:
                lines = lines[1:]

            image_names = []

            for line in lines:
                if line.strip():
                    # ps aux 형식에서 마지막 컬럼(명령어) 추출
                    parts = line.split()
                    if len(parts) >= 11:
                        command = parts[10]  # 마지막 컬럼이 명령어
                        if command and command != 'COMMAND':
                            # 경로에서 파일명만 추출
                            import os
                            image_name = os.path.basename(command)
                            if image_name:
                                image_names.append(image_name)

        # 중복 제거 및 정렬
        if image_names:
            # 빈 문자열 제거
            image_names = get_list_removed_empty(image_names)

            # 앞뒤 공백 제거
            image_names = get_list_striped_element(image_names)

            # 중복 제거
            image_names = get_list_deduplicated(image_names)

            # 알파벳 순으로 정렬
            image_names.sort(key=str.lower)

            cmd_name = "tasklist" if is_os_windows() else "ps"
            logging.debug(f"{cmd_name}에서 {len(image_names)}개의 고유한 이미지명을 수집했습니다.")
        else:
            logging.debug("️ 프로세스 목록에서 이미지명을 찾을 수 없습니다.")

        return image_names

    except Exception as e:
        logging.debug(f"프로세스 목록 처리 중 오류 발생: {e}")
        return []


def get_tasklist_with_pid():
    import re
    import subprocess

    import logging

    from sources.functions.is_os_windows import is_os_windows

    """
    tasklist/ps 명령어의 결과에서 이미지명과 PID를 함께 수집
    
    Returns:
        list: (이미지명, PID) 튜플 리스트
    """
    try:
        if is_os_windows():
            # Windows tasklist 명령어 실행
            try:
                result = subprocess.run(['tasklist', '/FO', 'CSV'],
                                        capture_output=True,
                                        text=True,
                                        encoding='cp949')
            except UnicodeDecodeError:
                result = subprocess.run(['tasklist', '/FO', 'CSV'],
                                        capture_output=True,
                                        text=True,
                                        encoding='utf-8',
                                        errors='ignore')

            if result.returncode != 0:
                logging.debug(f"tasklist 명령어 실행 실패: {result.stderr}")
                return []

            if not result.stdout:
                logging.debug("️ tasklist 명령어 결과가 비어있습니다.")
                return []

            lines = result.stdout.strip().split('\n')

            # 첫 번째 줄은 헤더이므로 제외
            if lines and lines[0].startswith('"Image Name"'):
                lines = lines[1:]

            processes = []

            for line in lines:
                if line.strip():
                    parts = re.findall(r'"([^"]*)"', line)
                    if len(parts) >= 2:
                        image_name = parts[0].strip()
                        pid = parts[1].strip()
                        if image_name and image_name.lower() != 'image name' and pid.isdigit():
                            processes.append((image_name, int(pid)))

        else:
            # Linux/macOS ps 명령어 실행
            try:
                result = subprocess.run(['ps', 'aux'],
                                        capture_output=True,
                                        text=True,
                                        encoding='utf-8')
            except Exception as e:
                logging.debug(f"ps 명령어 실행 실패: {e}")
                return []

            if result.returncode != 0:
                logging.debug(f"ps 명령어 실행 실패: {result.stderr}")
                return []

            if not result.stdout:
                logging.debug("️ ps 명령어 결과가 비어있습니다.")
                return []

            lines = result.stdout.strip().split('\n')

            # 첫 번째 줄은 헤더이므로 제외
            if lines and 'USER' in lines[0]:
                lines = lines[1:]

            processes = []

            for line in lines:
                if line.strip():
                    parts = line.split()
                    if len(parts) >= 2:
                        try:
                            pid = int(parts[1])
                            command = parts[10] if len(parts) >= 11 else parts[1]
                            if command and command != 'PID':
                                import os
                                image_name = os.path.basename(command)
                                if image_name:
                                    processes.append((image_name, pid))
                        except (ValueError, IndexError):
                            continue

        if processes:
            cmd_name = "tasklist" if is_os_windows() else "ps"
            logging.debug(f"{cmd_name}에서 {len(processes)}개의 프로세스를 수집했습니다.")
        else:
            logging.debug("️ 프로세스 목록을 찾을 수 없습니다.")


        return processes

    except Exception as e:
        logging.debug(f"프로세스 목록 처리 중 오류 발생: {e}")
        return []


def get_pids_by_process_name(process_img_n):
    import logging

    """
    프로세스명으로 PID 리스트를 반환 (기존 get_pids 함수 개선)
    
    Args:
        process_img_n (str): 프로세스 이미지명
    
    Returns:
        list: PID 리스트
    """
    try:
        import re
        from sources.functions.ensure_command_executed import ensure_command_executed
        from sources.functions.get_list_leaved_element_pattern import get_list_leaved_element_pattern

        cmd = f"tasklist | findstr {process_img_n}"
        std_list = ensure_command_executed(cmd=cmd)
        pids = get_list_leaved_element_pattern(items=std_list, pattern=r'^\S+\s+(\d+)\s+[A-Za-z]')

        logging.debug(f"프로세스 '{process_img_n}'에서 {len(pids)}개의 PID를 찾았습니다.")
        return pids

    except Exception as e:
        logging.debug(f"PID 검색 중 오류 발생: {e}")
        return []


def get_pid_by_window_title(window_title_seg):
    import logging

    from sources.functions.ensure_command_executed import ensure_command_executed

    """
    윈도우 타이틀로 PID를 찾는 함수 (기존 get_pid_by_window_title_via_tasklist 함수 개선)
    
    Args:
        window_title_seg (str): 윈도우 타이틀 일부
    
    Returns:
        str or list: PID 또는 PID 리스트
    """
    try:
        cmd = rf'tasklist'
        lines = ensure_command_executed(cmd=cmd)
        matching_lines = None

        for line in lines:
            if window_title_seg in line:
                matching_lines = line
                break

        if not matching_lines:
            logging.debug(f"️ 윈도우 타이틀 '{window_title_seg}'을 포함하는 프로세스를 찾을 수 없습니다.")
            return None

        pids = []
        parts = matching_lines.split()
        if len(parts) > 1 and window_title_seg in parts[0]:
            pids.append(parts[1])

        if len(pids) == 1:
            logging.debug(f"윈도우 타이틀 '{window_title_seg}'의 PID: {pids[0]}")
            return pids[0]
        else:
            logging.debug(f"윈도우 타이틀 '{window_title_seg}'의 PID들: {pids}")
            return pids

    except Exception as e:
        logging.debug(f"윈도우 타이틀 PID 검색 중 오류 발생: {e}")
        return None




def get_process_info_by_window_title(window_title_seg):
    import logging

    from sources.functions.get_process_info_by_pid import get_process_info_by_pid
    try:
        pid = get_pid_by_window_title(window_title_seg)
        if not pid:
            return []

        if isinstance(pid, list):
            # 여러 PID가 있는 경우
            process_info_list = []
            for p in pid:
                process_info = get_process_info_by_pid(p)
                if process_info:
                    process_info_list.append(process_info)
            return process_info_list
        else:
            # 단일 PID인 경우
            process_info = get_process_info_by_pid(pid)
            return [process_info] if process_info else []

    except Exception as e:
        logging.debug(f"윈도우 타이틀 프로세스 정보 검색 중 오류 발생: {e}")
        return []
