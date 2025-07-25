
if __name__ == "__main__":
    import traceback
    from pkg_py.functions_split.download_youtube_list import download_youtube_list
    from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
    from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
    from pkg_py.functions_split.get_videos_urls_from_youtube_channel_main_page import get_videos_urls_from_youtube_channel_main_page
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
    try:
        while 1:
            youtube_channel_main_page_url = input('youtube_channel_main_page_url=')
            youtube_channel_main_page_url = youtube_channel_main_page_url.strip()
            # download_youtube_list(via_f_txt=True, debug_mode=True)
            video_url_list = get_videos_urls_from_youtube_channel_main_page(youtube_channel_main_page_url=youtube_channel_main_page_url)
            download_youtube_list(video_url_list=video_url_list)
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
