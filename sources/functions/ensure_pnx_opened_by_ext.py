from sources.objects.task_orchestrator_cli_files import F_VSCODE_LNK



def ensure_pnx_opened_by_ext(pnx):
    from sources.functions.is_os_windows import is_os_windows
    from sources.objects.task_orchestrator_cli_files import F_PYCHARM64_EXE
    from sources.functions.ensure_command_executed import ensure_command_executed
    from sources.functions.get_pnx_windows_style import get_pnx_windows_style
    import logging
    from sources.functions.get_os_n import get_os_n
    try:
        logging.debug(rf"pnx={pnx}")
        # 수정: pnx가 None인 경우 체크 추가
        if pnx is None:
            logging.debug("파일 경로가 None입니다. 파일을 열 수 없습니다.")
            return

        pnx = str(pnx)

        # TBD : tab 으로 뭘로 열지 설정하도록 ?
        if is_os_windows():
            import os

            # x = get_x(pnx).replace('.', '')
            x = os.path.splitext(pnx)[1].lower().replace('.', '')
            text_editor = None
            ext_to_program = None
            if get_os_n() == 'windows':
                # ext_to_program = ensure_value_completed(message="ext_to_program=", option_values=['xc', 'nx', 'no'])
                                ext_to_program = {
                    '': ('explorer.exe', 'directory, opening in windows explorer'),
                    'log': (f'{F_VSCODE_LNK}', 'log file, opening in VS Code'),
                    'py': (str(F_PYCHARM64_EXE), 'python file, opening in PyCharm'),
                    'bat': (str(F_PYCHARM64_EXE), 'batch file, opening in PyCharm'),
                }
            program, description = ext_to_program.get(x, (None, None))
            if program:
                text_editor = program
                pnx = get_pnx_windows_style(pnx=pnx)
                logging.debug(f"ensure_pnx_opened_by_ext: {pnx} is a {description}")

            # text_editor가 None이면 os.startfile() 시도
            if text_editor is None:
                try:
                    os.startfile(pnx)
                    logging.debug(f"'{pnx}' 파일을 시스템 기본 프로그램으로 열었습니다.")
                except OSError as e:
                    logging.error(f"'{pnx}' 파일을 열 수 없습니다: {e}. 확장자 '{x}'에 대한 기본 프로그램이 설정되지 않았을 수 있습니다.")
                    logging.debug("파일을 수동으로 열거나, 해당 확장자에 대한 기본 프로그램을 설정해주세요.")
            else:
                # text_editor가 설정된 경우, 기존 ensure_command_executed 로직 사용
                cmd = f'"{text_editor}" "{pnx}"'
                ensure_command_executed(cmd=cmd, mode='a')
        else:
            try:
                from functions.ensure_guided_not_prepared_yet import ensure_not_prepared_yet_guided

                ensure_not_prepared_yet_guided()
            except ImportError:
                # fallback: 간단한 메시지 출력
                print("Linux 환경에서는 파일 열기 기능이 아직 구현되지 않았습니다.")
            # if x == '':  # d 인 경우
            #     text_editor = 'explorer.exe'
            # elif x == 'txt':
            #     text_editor = 'gedit' # nvim, nano, vim, code
            # # elif x == 'csv':
            # #     text_editor = 'explorer.exe'
            # # elif x == 'xlsx':
            # #     text_editor = 'explorer.exe'
            # # elif x == 'xls':
            # #     text_editor = 'explorer.exe'
            # pnx = get_pnx_unix_style(pnx=pnx)
    except:
        logging.debug("❌ An unexpected error occurred")
