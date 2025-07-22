def get_video_filtered_list_v4(
        d_working,
        ext_allowed_list,
        video_ignored_keyword_list,
        cache_ttl=60,
        verbose=True,
        skip_hash_prefix=True,
        use_cache=True
):
    import hashlib
    import inspect
    import os
    import pickle
    import time

    from pkg_py.pk_system_object.directories import D_PKG_PKL
    from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.functions_split.get_pk_wsl_mount_d import get_pk_wsl_mount_d
    func_n = inspect.currentframe().f_code.co_name

    # --- WSL 경로 대응 ---
    if is_os_wsl_linux():
        d_working = get_pk_wsl_mount_d(windows_path=d_working, path_to_mount='Downloads/pk_working')

    # --- 캐시 경로 생성 ---
    key_src = f"{d_working}|{sorted(ext_allowed_list)}|{sorted(video_ignored_keyword_list)}|{skip_hash_prefix}"
    key_hash = hashlib.md5(key_src.encode()).hexdigest()
    f_cache = os.path.join(D_PKG_PKL, f"{func_n}_{key_hash}.pkl")

    # --- 캐시 로드 시도 ---
    if use_cache and os.path.exists(f_cache):
        try:
            with open(f_cache, "rb") as f:
                cache = pickle.load(f)
            if time.time() - cache.get("timestamp", 0) < cache_ttl:
                if verbose:
                    pk_print(f"[CACHE] using video list cache from {f_cache}", print_color='cyan')
                return cache["video_list"]
        except Exception as e:
            if verbose:
                pk_print(f"[CACHE] failed to load cache ({e}), will refresh", print_color='yellow')

    # --- 파일 목록 가져오기 ---
    try:
        file_list = [os.path.join(d_working, f) for f in os.listdir(d_working)]
    except Exception as e:
        pk_print(f"[ERROR] Failed to read files from {d_working}: {e}", print_color='red')
        return []

    ext_set = set(ext.lower() for ext in ext_allowed_list)
    filtered_list = []

    for f in file_list:
        base = os.path.basename(f)
        ext = os.path.splitext(f)[1].lower()

        if not os.path.isfile(f):
            continue
        if ext not in ext_set:
            continue
        if skip_hash_prefix and base.startswith("#"):
            continue
        if any(keyword in base for keyword in video_ignored_keyword_list):
            continue

        filtered_list.append(f)

    # --- 캐시 저장 ---
    if use_cache:
        try:
            os.makedirs(os.path.dirname(f_cache), exist_ok=True)
            with open(f_cache, "wb") as f:
                pickle.dump({
                    "timestamp": time.time(),
                    "video_list": filtered_list
                }, f)
            if verbose:
                pk_print(f"[CACHE] refreshed video list and saved to {f_cache}", print_color='green')
        except Exception as e:
            if verbose:
                pk_print(f"[CACHE] failed to save cache ({e})", print_color='red')

    return filtered_list
