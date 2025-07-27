from pkg_py.functions_split.get_video_filtered_list_v5 import get_video_filtered_list_v5


def get_video_filtered_list(d_working, ext_allowed_list, video_ignored_keyword_list, video_ignored_regex_patterns=None):
    # return get_video_filtered_list_v3(d_working, ext_allowed_list, video_ignored_keyword_list)
    # return get_video_filtered_list_v4(d_working, ext_allowed_list, video_ignored_keyword_list)
    return get_video_filtered_list_v5(d_working, ext_allowed_list, video_ignored_keyword_list, video_ignored_regex_patterns)
