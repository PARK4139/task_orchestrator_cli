from sources.objects.encodings import Encoding
from sources.objects.pk_map_texts import PkTexts
from PIL import Image


def should_i_crawl_a_tag_href():
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    while 1:

        url = ""

        dialog = GuiUtil.CustomQdialog(prompt="해당 페이지의 href 를 크롤링할까요?", btn_list=[YES, NO], input_box_mode=True, input_box_text_default=url)
        dialog.exec()
        btn_txt_clicked = dialog.btn_txt_clicked

        if btn_txt_clicked == PkTexts.YES:
            crawl_html_href(url=dialog.input_box.text())
            break
        else:
            break
