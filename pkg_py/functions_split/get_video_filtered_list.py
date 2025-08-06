from pkg_py.functions_split.get_video_filtered_list_v5 import get_video_filtered_list_v5
from pkg_py.system_object.ttl_cache_manager import ensure_function_ttl_cached


@ensure_function_ttl_cached(ttl_seconds=300, maxsize=16)  # 5분 캐시 활성화 # pk_*
def get_video_filtered_list(d_working, ext_allowed_list, video_name_parts_to_ignore, video_ignored_regex_patterns=None):
    # return get_video_filtered_list_v3(d_working, ext_allowed_list, video_name_parts_to_ignore)
    # return get_video_filtered_list_v4(d_working, ext_allowed_list, video_name_parts_to_ignore)
    return get_video_filtered_list_v5(d_working, ext_allowed_list, video_name_parts_to_ignore, video_ignored_regex_patterns)
