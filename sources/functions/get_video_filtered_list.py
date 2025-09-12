from objects.pk_map_texts import PkTexts
from objects.pk_ttl_cache_manager import ensure_function_return_ttl_cached


@ensure_function_return_ttl_cached(ttl_seconds=60 * 30, maxsize=16)  # 5분 캐시 활성화 # task_orchestrator_cli_option
# @ensure_function_return_ttl_cached(ttl_seconds=60 * 1, maxsize=10)
def get_video_filtered_list(d_working, ext_allowed_list, video_name_parts_to_ignore, video_ignored_regex_patterns=None):
    import re
    import os
    from sources.functions.is_os_wsl_linux import is_os_wsl_linux
    import logging
    from sources.functions.get_pk_wsl_mount_d import get_pk_wsl_mount_d

    # 기본값 설정
    if video_ignored_regex_patterns is None:
        video_ignored_regex_patterns = []

    logging.debug(f"get_video_filtered_list_v5 called with:")
    logging.debug(f"d_working: {d_working}")
    logging.debug(f"ext_allowed_list: {ext_allowed_list}")
    logging.debug(f"video_name_parts_to_ignore: {video_name_parts_to_ignore}")
    logging.debug(f"video_ignored_regex_patterns: {video_ignored_regex_patterns}")

    # --- WSL 경로 대응 ---
    if is_os_wsl_linux():
        original_d_working = d_working
        d_working = get_pk_wsl_mount_d(windows_path=d_working, path_to_mount='Downloads/pk_working')
        logging.debug(f"WSL detected, d_working transformed from {original_d_working} to {d_working}")

        # --- 파일 목록 가져오기 ---
    try:
        all_files_in_dir = os.listdir(d_working)  # Changed variable name for clarity
        file_list = [os.path.join(d_working, f) for f in all_files_in_dir]
        logging.debug(f"Found {len(all_files_in_dir)} files/directories in {d_working}")
        # logging.debug(f"Raw file list: {file_list}")
    except Exception as e:
        logging.error(f"Failed to read files from {d_working}: {e}")
        return []

    ext_set = set(ext.lower() for ext in ext_allowed_list)
    filtered_list = []

    compiled_regex_patterns = []
    for pattern in video_ignored_regex_patterns:
        try:
            compiled_regex_patterns.append(re.compile(pattern))
        except re.error as e:
            logging.debug(f"{PkTexts.WARNING} Invalid regex pattern '{pattern}': {e}")
            logging.warning(f"Invalid regex pattern '{pattern}': {e}")

    for f in file_list:
        base = os.path.basename(f)
        ext = os.path.splitext(f)[1].lower()

        if not os.path.isfile(f):
            logging.debug(f"Skipping '{base}': Not a file.")
            continue
        if ext not in ext_set:
            logging.debug(f"Skipping '{base}': Extension not in allowed list {ext_allowed_list}.")
            continue
        if base.startswith("#"):
            logging.debug(f"Skipping '{base}': Starts with '#'.")
            continue

        # 기존 키워드 필터링
        if any(keyword in base for keyword in video_name_parts_to_ignore):
            logging.debug(f"Skipping '{base}': Contains ignored keyword from {video_name_parts_to_ignore}.")
            continue

        # 정규표현식 패턴 필터링
        if any(pattern.search(base) for pattern in compiled_regex_patterns):
            logging.debug(f"Skipping '{base}': Matches ignored regex pattern.")
            continue

        filtered_list.append(f)
        logging.debug(f"Including '{base}' in filtered list.")

    logging.debug(f"filtered videos (count: {len(filtered_list)}): {filtered_list}")

    return filtered_list
