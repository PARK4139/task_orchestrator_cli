def ensure_memo_contents_found():
    from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
    from pkg_py.system_object.files import F_MEMO_HOW_PK
    from pkg_py.functions_split.get_os_n import get_os_n
    from pkg_py.functions_split.chcp_65001 import chcp_65001
    import re
    import subprocess
    import sys
    import locale
    from pkg_py.functions_split.get_fzf_command import get_fzf_command
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.encodings import Encoding

    if get_os_n() == 'windows':
        chcp_65001()
        # 추가 인코딩 설정
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
        # locale 설정
        try:
            locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')
        except:
            try:
                locale.setlocale(locale.LC_ALL, 'Korean_Korea.65001')
            except:
                pass

    f_memo = rf'{F_MEMO_HOW_PK}'
    if not does_pnx_exist(f_memo):
        ensure_printed(f'''{f_memo} does not exist %%%FOO%%%''', print_color='red')
        return

    # hey cursor! write here.
    # 검색 키워드 입력 (fzf 또는 직접 입력) - 다중 키워드 지원
    search_keywords = []

    # 메모 파일에서 자주 나오는 단어들 추출 (fzf 선택용)
    common_words = set()
    try:
        with open(file=f_memo, mode='r', encoding=Encoding.UTF8.value, errors='ignore') as file_obj:
            for line in file_obj:
                # 한글, 영문, 숫자로 구성된 단어들 추출
                words = re.findall(r'[가-힣a-zA-Z0-9]+', line)
                for word in words:
                    if len(word) >= 2:  # 2글자 이상만
                        common_words.add(word)
    except:
        pass

    # fzf로 키워드 선택 또는 직접 입력
    fzf_cmd = get_fzf_command()
    if fzf_cmd and common_words:
        try:
            # fzf로 단어 선택
            word_list = sorted(list(common_words))
            fzf_input = "\n".join(word_list)

            cmd = [fzf_cmd, "--height", "30%", "--layout=reverse", "--border", "--prompt", "검색할 키워드를 선택하세요 (공백으로 구분하여 여러 키워드 입력 가능): "]
            proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, encoding='utf-8')
            out, _ = proc.communicate(input=fzf_input)

            if out.strip():
                # 공백으로 구분된 키워드들을 리스트로 분리
                search_keywords = [kw.strip() for kw in out.strip().split() if kw.strip()]
                # Blue text on White background
                print(f'\033[34;47m선택된 키워드: {" ".join(search_keywords)}\033[0m')
        except Exception as e:
            ensure_printed(f"fzf 실행 오류: {str(e)}", print_color="yellow")

    # fzf가 없거나 실패한 경우 직접 입력
    if not search_keywords:
        try:
            keyword_input = input("검색할 키워드를 입력하세요 (공백으로 구분하여 여러 키워드 입력 가능): ").strip()
            if keyword_input:
                # 공백으로 구분된 키워드들을 리스트로 분리
                search_keywords = [kw.strip() for kw in keyword_input.split() if kw.strip()]
                print(f'\033[34;47m입력된 키워드: {" ".join(search_keywords)}\033[0m')
        except Exception as e:
            ensure_printed(f"키워드 입력 오류: {str(e)}", print_color="red")
            return

    if not search_keywords:
        ensure_printed("검색 키워드가 입력되지 않았습니다.", print_color="yellow")
        return

    # 검색 모드 선택
    search_mode = None
    fzf_cmd = get_fzf_command()

    if fzf_cmd:
        try:
            # fzf로 모드 선택
            mode_options = [
                "제목만 보기 (빠른 검색)",
                "전체 내용 보기 (상세 검색)"
            ]
            fzf_input = "\n".join(mode_options)

            cmd = [fzf_cmd, "--height", "30%", "--layout=reverse", "--border", "--prompt", "검색 모드를 선택하세요: "]
            proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, encoding='utf-8')
            out, _ = proc.communicate(input=fzf_input)

            if out.strip():
                selected_mode = out.strip()
                if "제목만 보기" in selected_mode:
                    search_mode = "title_only"
                elif "전체 내용 보기" in selected_mode:
                    search_mode = "full_content"
                ensure_printed(f"선택된 모드: {selected_mode}", print_color="green")
        except Exception as e:
            ensure_printed(f"fzf 실행 오류: {str(e)}", print_color="yellow")

    # fzf가 없거나 실패한 경우 직접 선택
    if not search_mode:
        ensure_printed("\n=== 검색 모드 선택 ===", print_color="green")
        ensure_printed("1. 제목만 보기 (빠른 검색)", print_color="cyan")
        ensure_printed("2. 전체 내용 보기 (상세 검색)", print_color="cyan")

        try:
            mode_choice = input("\n모드를 선택하세요 (1-2): ").strip()
            if mode_choice == "1":
                search_mode = "title_only"
            elif mode_choice == "2":
                search_mode = "full_content"
            else:
                ensure_printed("잘못된 선택입니다. 제목만 보기 모드로 진행합니다.", print_color="yellow")
                search_mode = "title_only"
        except Exception as e:
            ensure_printed(f"모드 선택 오류: {str(e)}", print_color="red")
            search_mode = "title_only"

    # 결과 저장
    found_contents = []
    current_content = []
    current_start_line = 1
    separator_pattern = r'^_{50,}$'

    try:
        with open(file=f_memo, mode='r', encoding=Encoding.UTF8.value, errors='ignore') as file_obj:
            for idx, line in enumerate(file_obj, 1):
                line_stripped = line.strip()

                if re.match(separator_pattern, line_stripped):
                    # 구분선이 나오면 이전 컨텐츠 저장
                    if current_content:
                        content_str = ''.join(current_content)
                        # 다중 키워드 AND 검색 (모든 키워드가 포함되어야 함)
                        content_lower = content_str.lower()
                        all_keywords_found = all(keyword.lower() in content_lower for keyword in search_keywords)
                        if all_keywords_found:
                            found_contents.append((current_start_line, content_str))
                        current_content = []
                    current_content.append(line)  # 구분선 포함
                    current_start_line = idx
                else:
                    current_content.append(line)
            # 마지막 컨텐츠도 검사
            if current_content:
                content_str = ''.join(current_content)
                # 다중 키워드 AND 검색 (모든 키워드가 포함되어야 함)
                content_lower = content_str.lower()
                all_keywords_found = all(keyword.lower() in content_lower for keyword in search_keywords)
                if all_keywords_found:
                    found_contents.append((current_start_line, content_str))
    except Exception as e:
        ensure_printed(f"파일 읽기 오류: {str(e)}", print_color="red")
        return

    # 결과가 없으면 종료
    if not found_contents:
        keyword_str = " ".join(search_keywords)
        ensure_printed(f"'{keyword_str}'가 모두 포함된 메모 컨텐츠를 찾을 수 없습니다.", print_color="yellow")
        return

    # fzf를 사용한 선택 기능
    fzf_cmd = get_fzf_command()
    selected_index = None

    # 전체 내용 보기 모드에서는 먼저 모든 내용을 출력
    if search_mode == "full_content":
        keyword_str = " ".join(search_keywords)
        ensure_printed(f"=== '{keyword_str}'가 모두 포함된 메모 컨텐츠 ({len(found_contents)}개) ===", print_color="green")

        # 최대 줄번호 길이 계산
        max_line_num_width = len(str(max([start_line for start_line, _ in found_contents])))
        max_index_width = len(str(len(found_contents)))

        for i, (start_line, content) in enumerate(found_contents, 1):
            # 제목 추출
            lines = content.split('\n')
            title = ""
            for line in lines:
                line_stripped = line.strip()
                if line_stripped and not re.match(separator_pattern, line_stripped):
                    title = line_stripped
                    break

            # 일정한 간격으로 정렬
            index_str = f"{i:>{max_index_width}}"
            line_num_str = f"{start_line:>{max_line_num_width}}"

            # divider, title, 내용 순서로 출력
            lines = content.split('\n')
            # divider가 첫 줄이면 먼저 출력
            if lines and re.match(separator_pattern, lines[0].strip()):
                print(f'\033[38;5;159m{lines[0]}\033[0m')
                lines = lines[1:]
            # title 컬러 및 다중 키워드 하이라이트 적용 (속도 최적화)
            from pkg_py.functions_split.get_keyword_colors import highlight_multiple_keywords_fast

            title_highlighted = highlight_multiple_keywords_fast(title, search_keywords)
            title_colored = f'\033[38;5;75m{title_highlighted}\033[0m'
            print(f"[{index_str}] (줄 {line_num_str}) {title_colored}")
            # 중복된 제목 제거: divider 다음 줄이 title과 같으면 생략
            if lines and lines[0].strip() == title:
                lines = lines[1:]
            # 나머지 내용 출력 (divider/중복제목은 이미 위에서 처리)
            out_lines = []
            for content_line in lines:
                if re.match(separator_pattern, content_line.strip()):
                    out_lines.append(f'\033[38;5;159m{content_line}\033[0m')
                else:
                    out_lines.append(highlight_multiple_keywords_fast(content_line, search_keywords))

            # 앞뒤 공백 제거 후 출력
            content_output = "\n".join(out_lines).strip()
            if content_output:
                print(content_output)
            print()  # 빈 줄 추가

    # fzf 사용 여부와 관계없이 전체 내용 보기 모드에서는 선택 과정 생략
    if search_mode == "full_content":
        ensure_printed("전체 내용이 출력되었습니다. 선택 과정을 건너뜁니다.", print_color="green")
        # 검색된 컨텐츠 수 출력
        keyword_str = " ".join(search_keywords)
        ensure_printed(f"검색 완료: '{keyword_str}'가 모두 포함된 메모 컨텐츠 {len(found_contents)}개를 찾았습니다.", print_color="green")
        return

    if fzf_cmd:
        try:
            # fzf용 입력 데이터 준비 (줄번호 + 제목 첫 줄)
            fzf_input_lines = []
            max_line_num_width = len(str(max([start_line for start_line, _ in found_contents])))

            for i, (start_line, content) in enumerate(found_contents):
                # 제목 추출 (구분선 다음 첫 번째 줄)
                lines = content.split('\n')
                title = ""
                for line in lines:
                    line_stripped = line.strip()
                    if line_stripped and not re.match(separator_pattern, line_stripped):
                        title = line_stripped
                        break

                # 일정한 간격으로 정렬
                line_num_str = f"{start_line:>{max_line_num_width}}"
                fzf_input_lines.append(f"[{i + 1:2d}] (줄 {line_num_str}) {title}")

            fzf_input = "\n".join(fzf_input_lines)

            # fzf 실행
            cmd = [fzf_cmd, "--height", "40%", "--layout=reverse", "--border"]
            proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, encoding='utf-8')
            out, _ = proc.communicate(input=fzf_input)

            if out.strip():
                # 선택된 결과에서 인덱스 추출
                selected_line = out.strip()
                match = re.search(r'\[(\d+)\]', selected_line)
                if match:
                    selected_index = int(match.group(1)) - 1  # 0-based index

        except Exception as e:
            ensure_printed(f"fzf 실행 오류: {str(e)}", print_color="yellow")
            selected_index = None

    # fzf가 없거나 실패한 경우 fallback 선택
    if selected_index is None:
        if search_mode == "title_only":
            keyword_str = " ".join(search_keywords)
            ensure_printed(f"=== '{keyword_str}'가 모두 포함된 메모 제목 ({len(found_contents)}개) ===", print_color="green")

            # 최대 줄번호 길이 계산
            max_line_num_width = len(str(max([start_line for start_line, _ in found_contents])))
            max_index_width = len(str(len(found_contents)))

            for i, (start_line, content) in enumerate(found_contents, 1):
                # 제목 추출
                lines = content.split('\n')
                title = ""
                for line in lines:
                    line_stripped = line.strip()
                    if line_stripped and not re.match(separator_pattern, line_stripped):
                        title = line_stripped
                        break

                # 일정한 간격으로 정렬
                index_str = f"{i:>{max_index_width}}"
                line_num_str = f"{start_line:>{max_line_num_width}}"
                ensure_printed(f"[{index_str}] (줄 {line_num_str}) {title}", print_color="cyan")

        # fallback 선택
        try:
            choice = input(f"\n보고 싶은 번호를 입력하세요 (1-{len(found_contents)}, Enter로 취소): ").strip()
            if choice:
                selected_index = int(choice) - 1
        except (ValueError, IndexError):
            ensure_printed("잘못된 선택입니다.", print_color="red")
            return
    else:
        ensure_printed(f"선택됨: {selected_index + 1}번", print_color="green")

    # 선택된 결과 출력 (전체 내용 보기 모드에서는 이미 출력했으므로 생략)
    if 0 <= selected_index < len(found_contents) and search_mode == "title_only":
        start_line, content = found_contents[selected_index]
        ensure_printed(f"\n=== 선택된 메모 컨텐츠 (줄 {start_line}) ===", print_color="green")

        # 내용 출력 (하이라이트 적용)
        from pkg_py.functions_split.get_keyword_colors import highlight_multiple_keywords_fast

        lines = content.split('\n')
        out_lines = []
        for content_line in lines:
            if re.match(separator_pattern, content_line.strip()):
                out_lines.append(f'\033[38;5;159m{content_line}\033[0m')
            else:
                out_lines.append(highlight_multiple_keywords_fast(content_line, search_keywords))

        # 앞뒤 공백 제거 후 출력
        content_output = "\n".join(out_lines).strip()
        if content_output:
            print(content_output)
    elif selected_index is None:
        ensure_printed("선택이 취소되었습니다.", print_color="yellow")

    # 검색된 컨텐츠 수 출력
    keyword_str = " ".join(search_keywords)
    ensure_printed(f"검색 완료: '{keyword_str}'가 모두 포함된 메모 컨텐츠 {len(found_contents)}개를 찾았습니다.", print_color="green")
