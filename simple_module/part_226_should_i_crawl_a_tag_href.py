from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from PIL import Image


def should_i_crawl_a_tag_href():
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    while 1:

        url = ""

        dialog = GuiUtil.CustomQdialog(prompt="해당 페이지의 href 를 크롤링할까요?", btn_list=[YES, NO], input_box_mode=True, input_box_text_default=url)
        dialog.exec()
        btn_txt_clicked = dialog.btn_txt_clicked

        if btn_txt_clicked == PkMessages2025.YES:
            crawl_html_href(url=dialog.input_box.text())
            break
        else:
            break
