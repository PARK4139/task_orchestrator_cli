from objects.task_orchestrator_cli_files import F_ENSURE_ARG_RECIEVED


def get_value_from_fzf_routine(file_id, editable, options, query=""):
    import logging
    import os
    import platform
    import subprocess
    import tempfile

    from functions.get_prompt_label import get_prompt_label
    from functions.get_prompt_label_guide_ment import get_prompt_label_guide_ment
    from objects.pk_map_texts import PkTexts
    from objects.task_orchestrator_cli_files import F_PK_ENSURE_GEMINI_CLI_LOCATED_TO_FRONT, F_PK_ENSURE_GEMINI_CLI_WHIP_KIT_ENABLED_INTERACTIVE
    from sources.functions.ensure_pnx_made import ensure_pnx_made
    from sources.functions.ensure_pnx_opened_by_ext import ensure_pnx_opened_by_ext
    from sources.functions.ensure_value_advanced_fallback_via_input import ensure_value_advanced_fallback_via_input
    from sources.functions.ensure_window_to_front import ensure_window_to_front
    from sources.functions.get_f_historical import ensure_history_file_pnx_return
    from sources.functions.get_fzf_command import get_fzf_command
    from sources.functions.get_nx import get_nx
    from sources.functions.is_os_windows import is_os_windows
    from sources.functions.is_os_wsl_linux import is_os_wsl_linux
    from sources.objects.pk_etc import PK_BLANK
    from sources.objects.pk_local_test_activate import LTA
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE

    ensure_pnx_made(pnx=D_TASK_ORCHESTRATOR_CLI_SENSITIVE, mode="f")

    history_file = ensure_history_file_pnx_return(file_id=file_id)
    if editable is True:
        ensure_pnx_opened_by_ext(pnx=history_file)
        ensure_window_to_front(get_nx(history_file))

    temp_file_path = None
    selected_value = None
    try:

        # 1) 옵션 임시 파일  # len(cmd) 가 길면 win
        with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8', newline="\n") as temp_f:
            temp_f.write("\n".join(options))
            temp_file_path = temp_f.name

        # 2) fzf 경로 확보 및 문자열화
        fzf_cmd = get_fzf_command()
        logging.debug(rf"fzf_cmd={fzf_cmd}")
        fzf_cmd = str(fzf_cmd) if fzf_cmd else None
        if not fzf_cmd:
            return ensure_value_advanced_fallback_via_input(options, query)

        # 3) OS별 커맨드들
        opening_command = 'xdg-open "{}"'
        copy_command = "xclip -selection clipboard"
        fzf_preview_option = 'bat --style=numbers --color=always "{}"'

        def is_os_macos():
            return platform.system().lower() == "darwin"

        if is_os_windows():
            # opening_command = 'start "" explorer.exe "{}"' # fail
            # opening_command = 'start "" explorer.exe "{{}}"' # fail
            # opening_command = 'start "" explorer.exe "{{}}"'
            copy_command = 'clip.exe'
            fzf_preview_option = 'type "{}"'
        elif is_os_wsl_linux():
            opening_command = 'explorer.exe "{}"'
            copy_command = 'clip.exe'
            fzf_preview_option = 'bat --style=numbers --color=always "{}"'
        elif is_os_macos():
            opening_command = 'open "{}"'
            copy_command = 'pbcopy'
            fzf_preview_option = 'cat "{}"'

        # 4) 너무 긴 초기 query 컷 (명령행/렌더 성능 보호)
        SAFE_QUERY_MAX = 512
        if query and len(query) > SAFE_QUERY_MAX:
            logging.warning(f"[WARN] query too long ({len(query)}), truncated to {SAFE_QUERY_MAX}")
            query = query[:SAFE_QUERY_MAX]

        bind_entries = [
            "tab:down",
            "shift-tab:up",

            # f"ctrl-o:execute({opening_command})", # fail : 이거 기능은  parsed list 기능 미사용설정에 의존
            # f'ctrl-o:execute(start "" explorer.exe "{{}}")', # fail
            # f'ctrl-o:execute-silent(cmd /c start "" "{+}")', # fail
            # f'ctrl-o:execute-silent(cmd /c start "" "{{}}")',  # fail
            # 'ctrl-o:execute-silent(cmd /c echo OPEN: { } & timeout /t 2 >nul)', # fail
            # f'ctrl-o:execute-silent(powershell -NoProfile -Command "Start-Process -FilePath ''{{}}''")', # fail
            # f'ctrl-o:execute-silent(powershell -NoProfile -Command "Start-Process -FilePath ''{}''")', # fail
            # f'ctrl-o:execute-silent(powershell -NoProfile -Command "Start-Process -FilePath ''{{}}''")', # fail
            # 'ctrl-o:execute-silent(cmd /c start "" explorer.exe {{}})', # 원인분석결과 fzf 에 parsed list 기능 추가가 문제가 되었음. 그 데이터까지 같이 들어가서 문제가 됨.
            # '''ctrl-o:select+execute-silent(powershell -NoProfile -Command "$p=''{}''; $p=$p -replace ''^\s*\d+\.\s*'',''''; Start-Process explorer.exe -ArgumentList $p")'"", # 현재 줄을 먼저 선택 → 숫자접두어 제거 → 열기 # fail

            # f'ctrl-o:select+execute-silent(python "{F_ENSURE_ARG_RECIEVED}" --sel "{{}}")',                    #  argv로 받기 (argparse).
            f'ctrl-o:select+execute-silent(cmd /c echo {{}} | python "{F_ENSURE_ARG_RECIEVED}" --from-stdin)'  # stdin으로 받기 (sys.stdin.read()).

            f"ctrl-y:execute-silent(echo {{}} | {copy_command})",
            "ctrl-p:toggle-preview",
            "ctrl-k:kill-line",

            "alt-d:page-down",  # Alt+d : 한 화면 아래
            "alt-u:page-up",  # Alt+u : 한 화면 위
            "alt-D:half-page-down",  # Alt+Shift+d
            "alt-U:half-page-up",  # Alt+Shift+u

            f'alt-`:execute(cmd /c start "" "{history_file}")',

            f'ALT-1:execute(start "" python "{F_PK_ENSURE_GEMINI_CLI_WHIP_KIT_ENABLED_INTERACTIVE})',
            f'ALT-2:execute(cmd /c start "" "{history_file}")',
            f'ALT-3:execute(start "" python "{F_PK_ENSURE_GEMINI_CLI_LOCATED_TO_FRONT})',
        ]

        def add_binds(cmd_list, entries, max_len=1500):
            # 한 인자에 몰아넣지 않도록 길이 기준으로 분할
            chunk = []
            length = 0
            for be in entries:
                add = ("," if chunk else "") + be
                if length + len(add) > max_len:
                    cmd_list += ["--bind", ",".join(chunk)]
                    chunk, length = [be], len(be)
                else:
                    chunk.append(be);
                    length += len(add)
            if chunk:
                cmd_list += ["--bind", ",".join(chunk)]
            return cmd_list

        # 6) 프롬프트/풋터 (개행 금지)
        prompt_label = get_prompt_label(file_id)
        prompt_label_guide_ment = get_prompt_label_guide_ment(prompt_label)
        footer_text = (
            f"# 단축키\n"
            f"CTRL-O: 열기\n"
            f"CTRL-Y: 복사\n"
            f"CTRL-P: 프리뷰 토글\n"
            f"CTRL-K: 커서의 뒤 삭제\n"
            f"CTRL-U: 커서의 앞 삭제\n"
            f"CTRL-A: 커서를 앞으로 이동(줄끝 단위)\n"
            f"CTRL-E: 커서를 뒤로 이동(줄끝 단위)\n"
            f"ALT-B: 커서를 앞으로 이동(단어 단위)\n"
            f"ALT-F: 커서를 뒤로 이동(단어 단위)\n"
            f"ALT-`: *히스토리 RAW 파일 수정(EDITABLE)\n"
            f"ALT-1: *GEMINI CLI WIP 재실행\n"
            f"ALT-2: *GEMINI CLI WIP 프롬프트 히스토리 RAW 파일 수정(EDITABLE)\n"
            f"ALT-3: *GEMINI CLI 창 앞으로 이동\n"
            f"\n"
            f"# 사용자 입력 가이드\n"
            f"{prompt_label_guide_ment}\n"
        )

        # 7) 최종 cmd argv
        cmd = [fzf_cmd, "--print-query"]
        if query:
            cmd += ["--query", query]
        cmd += [
            "--no-mouse",
            "--no-multi",
            f"--prompt={prompt_label}={PK_BLANK}{PK_BLANK}",
            "--pointer=▶",
            "--color=prompt:#ffffff,pointer:#4da6ff,hl:#3399ff,hl+:#3399ff,fg+:#3399ff",
            "--footer", footer_text,
            # "--height=90%", "--layout=reverse",
        ]
        cmd = add_binds(cmd, bind_entries)

        # 8) 디버그: 최종 커맨드라인 길이 경고
        try:
            from subprocess import list2cmdline
            cmdline_preview = list2cmdline(cmd)
            if len(cmdline_preview) > 7000:
                logging.warning(f"{PkTexts.WARNING} fzf command line length={len(cmdline_preview)} (>7000)")
        except Exception:
            pass

        logging.debug(rf"cmd={cmd}")

        # 9) 실행 (대화형 유지용: stdin=파일핸들, stdout=PIPE 허용 — fzf UI 정상 동작)
        with open(temp_file_path, 'r', encoding='utf-8') as stdin_file:
            proc = subprocess.Popen(
                cmd,
                stdin=stdin_file,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8',
                shell=False,
            )
            out, err = proc.communicate()

        if proc.returncode not in (0, 130):
            logging.error(f"[ERROR] fzf exited with code {proc.returncode}, stderr={(err or '').strip()}")

        # 10) 결과 파싱
        out = (out or "").strip()
        lines = out.split("\n") if out else []
        query_out = lines[0] if len(lines) > 0 else ""
        selection = lines[1] if len(lines) > 1 else ""

        selected_value = selection if selection in options else query_out

        # 11) 로그 포맷 버그 수정 (삼중따옴표 중첩 제거)
        logging.debug(f"selected_value={selected_value} {'%%%FOO%%%' if LTA else ''}")

        if not selected_value:
            logging.debug("Selection was cancelled.")
            return None

        return selected_value

    except Exception as e:
        logging.error(f"[ERROR] Failed to execute fzf: {e}")
        selected_value = ensure_value_advanced_fallback_via_input(options, query)
        return selected_value
    finally:
        if temp_file_path and os.path.exists(temp_file_path):
            try:
                os.remove(temp_file_path)
            except Exception as e:
                logging.warning(f"[WARN] failed to remove temp file {temp_file_path}: {e}")

    # 가드
    if selected_value not in options:
        logging.debug(f"[WARN] Entered value is not in the option list: {selected_value}")
    return selected_value
