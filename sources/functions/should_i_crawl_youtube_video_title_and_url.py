from sources.objects.pk_map_texts import PkTexts


def should_i_crawl_youtube_video_title_and_url():
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    while 1:

        # 테스트용
        keyword = 'blahblah'
        url = f'https://www.youtube.com/results?search_query={keyword}'

        dialog = GuiUtil.CustomQdialog(prompt="해당 페이지의 video title, video url을 크롤링할까요?", btn_list=[YES, NO],
                                       input_box_mode=True, input_box_text_default=url)
        dialog.exec()
        btn_txt_clicked = dialog.btn_txt_clicked

        if btn_txt_clicked == PkTexts.YES:
            crawl_youtube_video_title_and_url(url=dialog.input_box.text())
            break
        else:
            break
