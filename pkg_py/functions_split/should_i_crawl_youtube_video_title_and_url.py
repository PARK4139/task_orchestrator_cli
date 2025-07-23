from pkg_py.pk_system_object.map_massages import PkMessages2025


def should_i_crawl_youtube_video_title_and_url():
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    while 1:

        # 테스트용
        keyword = 'blahblah'
        url = f'https://www.youtube.com/results?search_query={keyword}'

        dialog = GuiUtil.CustomQdialog(prompt="해당 페이지의 video title, video url을 크롤링할까요?", btn_list=[YES, NO],
                                       input_box_mode=True, input_box_text_default=url)
        dialog.exec()
        btn_txt_clicked = dialog.btn_txt_clicked

        if btn_txt_clicked == PkMessages2025.YES:
            crawl_youtube_video_title_and_url(url=dialog.input_box.text())
            break
        else:
            break
