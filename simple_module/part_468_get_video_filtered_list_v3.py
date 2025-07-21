from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux

from pkg_py.pk_system_layer_directories import D_PKG_PKL
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_014_pk_print import pk_print


def get_video_filtered_list_v3(d_working, ext_allowed_list, video_ignored_keyword_list):
    import os
    import pickle
    import hashlib
    import inspect
    import time

    func_n = inspect.currentframe().f_code.co_name

    # --- 캐시 파일 경로 ---
    # 키가 되는 인자를 해시 처리
    key_src = f"{d_working}|{sorted(ext_allowed_list)}|{sorted(video_ignored_keyword_list)}"
    key_hash = hashlib.md5(key_src.encode()).hexdigest()
    F_CACHE = f"{D_PKG_PKL}/{func_n}_{key_hash}.pkl"
    CACHE_TTL_SECONDS = 60  # 60초 이내라면 캐시 사용

    # --- WSL 경로 처리 ---
    if is_os_wsl_linux():
        d_working = get_pk_wsl_mount_d(windows_path=d_working, path_to_mount='Downloads/pk_working')

    # --- 캐시 로드 시도 ---
    if os.path.exists(F_CACHE):
        try:
            with open(F_CACHE, "rb") as f:
                cache = pickle.load(f)
            if time.time() - cache["timestamp"] < CACHE_TTL_SECONDS:
                pk_print(f"[CACHE] using video list cache from {F_CACHE}", print_color='cyan')
                return cache["video_list"]
        except Exception:
            pass  # 손상된 캐시는 무시

    # --- 파일 목록 생성 ---
    try:
        f_list = [os.path.join(d_working, f) for f in os.listdir(d_working)]
    except Exception as e:
        pk_print(f"[ERROR] Failed to read files from {d_working}: {e}", print_color='red')
        return []

    filtered = [
        f for f in f_list
        if os.path.splitext(f)[1].lower() in ext_allowed_list
           and os.path.isfile(f)
           and not any(keyword in os.path.basename(f) for keyword in video_ignored_keyword_list)
    ]

    # --- 캐시 저장 ---
    os.makedirs(os.path.dirname(F_CACHE), exist_ok=True)
    with open(F_CACHE, "wb") as f_obj:
        pickle.dump({
            "timestamp": time.time(),
            "video_list": filtered
        }, f_obj)

    pk_print(f"[CACHE] refreshed video list and saved to {F_CACHE}", print_color='green')
    return filtered
