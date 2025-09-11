from sources.objects.task_orchestrator_cli_files import F_DOWNLOAD_YOUTUBE_VIDEOS_HISTORY


def ensure_youtube_videos_downloaded(video_urls=None):
    from sources.functions.ensure_command_executed import ensure_command_executed
    from sources.functions.ensure_youtube_videos_downloaded_v3 import ensure_youtube_videos_downloaded_v3
    from sources.functions.ensure_pnx_made import ensure_pnx_made
    from sources.functions.get_list_from_f import get_list_from_f
    from sources.functions.get_list_removed_by_removing_runtine import get_list_removed_by_removing_runtine
    from sources.functions.get_list_removed_element_contain_prompt import get_list_removed_element_contain_prompt
    from sources.functions.get_list_via_user_input import get_list_via_user_input
    from sources.functions.is_window_opened import is_window_opened
    import logging
    from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI
    from sources.objects.pk_local_test_activate import LTA

    import inspect
    from urllib.parse import quote

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    f_video_to_download =F_DOWNLOAD_YOUTUBE_VIDEOS_HISTORY
    via_f_txt =F_DOWNLOAD_YOUTUBE_VIDEOS_HISTORY
    ensure_pnx_made(pnx=f_video_to_download, mode="f")

    if not is_window_opened(window_title_seg=func_n):
        ensure_command_executed(cmd=rf"explorer {f_video_to_download}")

    if via_f_txt is None and video_urls is None:
        logging.debug(rf"{func_n}() 동작 조건 불충족")
        return

    if via_f_txt is True and video_urls is None:
        video_urls = get_list_from_f(f=f_video_to_download)
        video_urls = get_list_removed_element_contain_prompt(working_list=video_urls, prompt="#")

    elif via_f_txt is None and video_urls is None:
        video_urls = get_list_via_user_input(ment=rf"다운로드할 유튜브 리스트를 \n 단위로 입력하세요", func_n=func_n)

    elif video_urls is not None:
        video_urls = video_urls
    else:
        logging.debug(f'''{'%%%FOO%%%' if LTA else ''} ''')
        return

    video_urls = get_list_removed_by_removing_runtine(working_list=video_urls)
    ensure_iterable_log_as_vertical(item_iterable=video_urls, item_iterable_n="urls")
    logging.debug(rf'''len(urls)="{len(video_urls)}"''')
    if len(video_urls) == 0:
        return
    playlist_url_parameter = 'list='
    for url in video_urls:
        if playlist_url_parameter in url:
            encoded_url = quote(url, safe=':/?&=')
            from pytube import Playlist
            playlist = Playlist(encoded_url)
            logging.debug(rf'''playlist="{playlist}"  {'%%%FOO%%%' if LTA else ''}''')
            logging.debug(rf'''playlist.title="{playlist.title}"  {'%%%FOO%%%' if LTA else ''}''')
            logging.debug(    str_working=rf'''len(playlist.video_urls)="{len(playlist.video_urls)}"  {'%%%FOO%%%' if LTA else ''}''')
            for index, video in enumerate(playlist.videos, start=1):
                logging.debug(rf'''video.watch_url="{video.watch_url}"  {'%%%FOO%%%' if LTA else ''}''')
                ensure_youtube_videos_downloaded_v3(urls=[video.watch_url])
        else:
            ensure_youtube_videos_downloaded_v3(urls=[url])
