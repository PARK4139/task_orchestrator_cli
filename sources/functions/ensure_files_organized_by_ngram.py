def ensure_files_organized_by_ngram(d_working, token_splitter_pattern, min_support, max_n, f_to_organize_list, allowed_extension_tuple=None):
    from sources.functions import ensure_value_completed
    from sources.functions.move_f_list_by_category import move_f_list_by_category
    from sources.functions.get_categorized_f_dict_by_priority_ngrams import get_categorized_f_dict_by_priority_ngrams
    from sources.functions.print_preview import print_preview
    from pathlib import Path
    import logging
    import logging
    import os

    # 디버깅: 입력 파라미터 확인
    logging.debug(f"=== Ngram 파일 정리 시작 ===")
    logging.debug(f"작업 디렉토리: {d_working}")
    logging.debug(f"토큰 분리 패턴: {token_splitter_pattern}")
    logging.debug(f"최소 지원도: {min_support}")
    logging.debug(f"최대 n-gram: {max_n}")
    logging.debug(f"정리할 파일 수: {len(f_to_organize_list)}")
    logging.debug(f"정리할 파일들: {[f.nick_name for f in f_to_organize_list[:5]]}...")
    if allowed_extension_tuple:
        logging.debug(f"허용된 확장자: {allowed_extension_tuple}")

    # 파일명 전처리 함수
    def preprocess_file_list(file_list, working_dir, allowed_exts=None):
        """타임스탬프가 포함된 파일명을 원본 파일명으로 매핑하고 실제 존재하는 파일만 반환"""
        import re
        from pathlib import Path

        processed_files = []
        timestamp_pattern = r'_\d{8}_\d{6}(\.\d+)?$'

        for file_path in file_list:
            # Path 객체로 변환
            path_obj = Path(file_path) if not isinstance(file_path, Path) else file_path

            # 디렉토리는 건너뛰기
            if path_obj.is_dir():
                logging.debug(f"디렉토리 건너뛰기: {path_obj.name}")
                continue

            # 파일이 아닌 경우 건너뛰기
            if not path_obj.is_file():
                logging.debug(f"파일이 아닌 항목 건너뛰기: {path_obj.name}")
                continue

            # 확장자 필터링 적용
            if allowed_exts and path_obj.suffix.lower() not in allowed_exts:
                logging.debug(f"확장자 필터링 제외: {path_obj.name} (확장자: {path_obj.suffix})")
                continue

            file_name = path_obj.name

            # 타임스탬프가 포함된 파일명인지 확인
            if re.search(timestamp_pattern, file_name):
                # 타임스탬프 제거하여 원본 파일명 찾기
                original_name = re.sub(timestamp_pattern, '', file_name)
                original_path = Path(working_dir) / original_name

                if original_path.exists():
                    logging.debug(f"타임스탬프 파일명 매핑: {file_name} → {original_name}")
                    processed_files.append(original_name)
                else:
                    # 확장자가 다른 경우도 확인
                    name_without_ext = Path(original_name).stem
                    for existing_file in Path(working_dir).iterdir():
                        if (existing_file.is_file() and
                                existing_file.stem == name_without_ext and
                                not re.search(timestamp_pattern, existing_file.name)):
                            logging.debug(f"확장자 변경 파일명 매핑: {file_name} → {existing_file.name}")
                            processed_files.append(existing_file.name)
                            break
                    else:
                        logging.warning(f"원본 파일을 찾을 수 없음: {file_name}")
            else:
                # 타임스탬프가 없는 경우 그대로 사용
                if Path(working_dir) / file_name:
                    processed_files.append(file_name)
                else:
                    logging.warning(f"파일이 존재하지 않음: {file_name}")

        # 중복 제거
        processed_files = list(set(processed_files))
        logging.info(f"전처리 완료: {len(file_list)}개 → {len(processed_files)}개")

        return processed_files

    # 파일명 전처리: 타임스탬프가 포함된 파일명을 원본 파일명으로 매핑
    processed_files = preprocess_file_list(f_to_organize_list, d_working, allowed_extension_tuple)
    logging.debug(f"전처리 후 파일 수: {len(processed_files)}")

    categorized_f_dict = get_categorized_f_dict_by_priority_ngrams(processed_files, min_support=min_support,
                                                                   max_n=max_n,
                                                                   token_splitter_pattern=token_splitter_pattern)

    # 디버깅: 분류 결과 확인
    logging.debug(f"분류 결과 카테고리 수: {len(categorized_f_dict)}")
    for category, files in categorized_f_dict.items():
        logging.debug(f"카테고리 '{category}': {len(files)}개 파일")

    print_preview(categorized_f_dict)

    ans = ensure_value_completed(key_hint="위와 같이 파일을 분류할까요? (o/x):", options=["o", "x"])
    ans = ans.strip()
    ans = ans.lower()
    should_proceed = ans in ['o', 'ok', 'yes', 'y']

    if should_proceed:
        logging.debug(f"파일 분류 실행 시작...")

        # 실행 전 파일 상태 기록
        before_files = {}
        for category, files in categorized_f_dict.items():
            if category == "기타":
                continue
            before_files[category] = [f for f in files if Path(f).exists()]

        # 실제 파일 이동 실행
        move_result = move_f_list_by_category(categorized_f_dict, base_p=d_working)

        # move_f_list_by_category의 결과 활용
        moved_files_count = move_result.get('moved_count', 0)
        total_files = move_result.get('total_files', 0)
        error_count = move_result.get('error_count', 0)

        # 추가 검증: 실제 파일 시스템 상태 확인
        actual_moved_count = 0
        failed_moves = []

        for category, files in categorized_f_dict.items():
            if category == "기타":
                continue

            d_n = category.replace(" ", "_")
            category_d = os.path.join(d_working, d_n)

            # 카테고리 디렉토리 존재 확인
            if not os.path.exists(category_d):
                logging.warning(f"카테고리 디렉토리가 생성되지 않음: {category_d}")
                continue

            # 각 파일의 이동 상태 확인
            for f_nx in files:
                src = os.path.join(d_working, f_nx)
                dst = os.path.join(category_d, f_nx)

                if os.path.exists(dst):
                    # 성공적으로 이동됨
                    actual_moved_count += 1
                    logging.debug(f"파일 이동 확인됨: {f_nx} → {category_d}")
                elif os.path.exists(src):
                    # 원본은 있지만 이동되지 않음
                    failed_moves.append(f"{f_nx} (원본 위치에 여전히 존재)")
                    logging.warning(f" 파일 이동 실패: {f_nx} - 원본 위치에 여전히 존재")
                else:
                    # 원본 파일을 찾을 수 없는 경우 - 타임스탬프 제거하여 원본 파일명 찾기
                    original_filename = find_original_filename(f_nx, d_working)
                    if original_filename and os.path.exists(os.path.join(d_working, original_filename)):
                        failed_moves.append(f"{f_nx} (원본 파일명: {original_filename})")
                        logging.warning(f"️  타임스탬프가 포함된 파일명: {f_nx} → 원본: {original_filename}")
                    else:
                        failed_moves.append(f"{f_nx} (원본 파일을 찾을 수 없음)")
                        logging.warning(f" 파일 이동 실패: {f_nx} - 원본 파일을 찾을 수 없음")

        # 원본 파일명 찾기 함수
        def find_original_filename(timestamped_filename, working_dir):
            """타임스탬프가 포함된 파일명에서 원본 파일명을 찾기"""
            import re

            # 타임스탬프 패턴: _YYYYMMDD_HHMMSS.xxx 또는 _YYYYMMDD_HHMMSS
            timestamp_pattern = r'_\d{8}_\d{6}(\.\d+)?$'

            # 타임스탬프 제거
            original_name = re.sub(timestamp_pattern, '', timestamped_filename)

            # 원본 파일명이 실제로 존재하는지 확인
            original_path = os.path.join(working_dir, original_name)
            if os.path.exists(original_path):
                return original_name

            # 확장자가 다른 경우도 확인 (예: .mkv → .jpg)
            name_without_ext = os.path.splitext(original_name)[0]
            for file in os.listdir(working_dir):
                if file.startswith(name_without_ext) and not re.search(timestamp_pattern, file):
                    return file

            return None

        # 결과 요약 출력
        print(f"\n=== 파일 분류 결과 ===")
        print(f"예상 이동 파일: {total_files}개")
        print(f"move_f_list_by_category 보고: {moved_files_count}개 성공, {error_count}개 실패")
        print(f"실제 파일 시스템 확인: {actual_moved_count}개 이동됨")

        if failed_moves:
            print(f"이동 실패한 파일: {len(failed_moves)}개")
            for failed in failed_moves[:10]:  # 최대 10개만 출력
                print(f"  - {failed}")
            if len(failed_moves) > 10:
                print(f"  ... 및 {len(failed_moves) - 10}개 더")

        # 실제 이동된 파일이 있을 때만 "분류 완료" 메시지 출력
        if actual_moved_count > 0:
            print(f"\n 분류 완료! {actual_moved_count}개 파일이 성공적으로 정리되었습니다.")
        else:
            print(f"\n️  분류 작업이 실행되었지만 실제로 이동된 파일이 없습니다.")
            if failed_moves:
                print(f"   실패 원인을 확인해주세요.")
            if error_count > 0:
                print(f"   move_f_list_by_category에서 {error_count}개 오류가 발생했습니다.")

        logging.debug(f"파일 분류 완료 - 예상: {total_files}개, 보고: {moved_files_count}개, 실제: {actual_moved_count}개, 실패: {len(failed_moves)}개")

    else:
        print("\n 분류를 취소했습니다.")
        logging.debug(f"사용자가 파일 분류를 취소함")
