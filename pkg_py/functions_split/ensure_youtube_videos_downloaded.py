
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.download_youtube_videos import download_youtube_videos
from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
from pkg_py.functions_split.get_list_from_f import get_list_from_f
from pkg_py.functions_split.get_list_removed_by_removing_runtine import get_list_removed_by_removing_runtine
from pkg_py.functions_split.get_list_removed_element_contain_prompt import get_list_removed_element_contain_prompt
from pkg_py.functions_split.get_list_via_user_input import get_list_via_user_input
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.local_test_activate import LTA


def ensure_youtube_videos_downloaded(via_f_txt=None, video_url_list=None):
    import inspect
    from urllib.parse import quote

    func_n = inspect.currentframe().f_code.co_name
    f_func_n_txt = rf'{D_PROJECT}\pkg_txt\{func_n}.txt'
    ensure_pnx_made(pnx=f_func_n_txt, mode="f")

    if via_f_txt is None and video_url_list is None:
        ensure_printed(rf"{func_n}() 동작 조건 불충족")
        return

    if via_f_txt is True and video_url_list is None:
        if not is_window_opened(window_title_seg=func_n):
            ensure_command_excuted_to_os(cmd=rf"explorer {f_func_n_txt}")
        video_url_list = get_list_from_f(f=f_func_n_txt)
        video_url_list = get_list_removed_element_contain_prompt(working_list=video_url_list, prompt="#")

    elif via_f_txt is None and video_url_list is None:
        video_url_list = get_list_via_user_input(ment=rf"다운로드할 유튜브 리스트를 \n 단위로 입력하세요", func_n=func_n)

    elif video_url_list is not None:
        video_url_list = video_url_list
    else:
        ensure_printed(f'''  {'%%%FOO%%%' if LTA else ''} ''', print_color='red')
        return

    video_url_list = get_list_removed_by_removing_runtine(working_list=video_url_list)
    ensure_iterable_printed_as_vertical(item_iterable=video_url_list, item_iterable_n="urls")
    ensure_printed(rf'''len(urls)="{len(video_url_list)}"''')
    if len(video_url_list) == 0:
        return
    string_playlist_positive = 'list='
    for url in video_url_list:
        if string_playlist_positive in url:
            encoded_url = quote(url, safe=':/?&=')
            from pytube import Playlist
            playlist = Playlist(encoded_url)
            ensure_printed(str_working=rf'''playlist="{playlist}"  {'%%%FOO%%%' if LTA else ''}''')
            ensure_printed(str_working=rf'''playlist.title="{playlist.title}"  {'%%%FOO%%%' if LTA else ''}''')
            ensure_printed(
                str_working=rf'''len(playlist.video_urls)="{len(playlist.video_urls)}"  {'%%%FOO%%%' if LTA else ''}''')
            for index, video in enumerate(playlist.videos, start=1):
                ensure_printed(str_working=rf'''video.watch_url="{video.watch_url}"  {'%%%FOO%%%' if LTA else ''}''')
                download_youtube_videos(urls=[video.watch_url])
        else:
            download_youtube_videos(urls=[url])
