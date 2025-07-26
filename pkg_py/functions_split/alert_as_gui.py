
import pickle
import cv2
import colorama
import chardet
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from datetime import datetime

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_d_working import get_d_working


def alert_as_gui(title_: str, ment: str, auto_click_positive_btn_after_seconds: int, input_text_default: str = "",
                 btn_list: any = None):
    if not btn_list:
        btn_list: [str] = ["확인"]
    import inspect
    import platform

    from PySide6.QtWidgets import QApplication
    func_n = inspect.currentframe().f_code.co_name
    # should_i_do 가 앱 안과 밖에서도 잘 된다면 deprecated 하자
    if platform.system() == 'Windows':
        func_n = inspect.currentframe().f_code.co_name
        ensure_printed(f"{func_n}()")

        # QApplication 인스턴스 확인
        app_foo = None
        app = QApplication.instance()
        if app is None:
            app_foo = QApplication()
        if input_text_default == "":
            is_input_text_box = False
        else:
            is_input_text_box = True

        dialog = GuiUtil.CustomQdialog(
            title=title_,
            btn_list=btn_list,
            input_box_mode=is_input_text_box,
            input_box_text_default=input_text_default,
            auto_click_positive_btn_after_seconds=auto_click_positive_btn_after_seconds,
        )
        dialog.exec()
        btn_txt_clicked = dialog.btn_txt_clicked

        if btn_txt_clicked == "":
            ensure_printed(f'버튼  입니다 {btn_txt_clicked}')
        if app == True:  # .....app 은 bool 이 아닌데. 동작 되고있는데..
            ensure_printed("여기는 좀 확인을 해야하는데. 호출 안되면 좋겠는데1")
            if isinstance(app_foo, QApplication):
                ensure_printed("여기는 좀 확인을 해야하는데. 호출 안되면 좋겠는데2")
                app_foo.exec()
        if app == True:
            # app_foo.quit()# QApplication 인스턴스 remove시도 : fail
            # app_foo.deleteLater()# QApplication 인스턴스 파괴시도 : fail
            # del app_foo # QApplication 인스턴스 파괴시도 : fail
            # app_foo=None # QApplication 인스턴스 파괴시도 : fail
            ensure_printed("여기는 좀 확인을 해야하는데. 호출 안되면 좋겠는데3")
            app_foo.shutdown()  # QApplication 인스턴스 파괴시도 : success  # 성공요인은 app.shutdown()이 호출이 되면서 메모리를 해제까지 수행해주기 때문
            # raise
    else:
        ensure_printed(f"{ment}")
