

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.press import press


def get_text_dragged():
    import inspect
    import clipboard
    func_n = inspect.currentframe().f_code.co_name

    # 클립보드 백업
    clipboard_current_contents = pk_paste()

    # 드래그된것 클립보드에 저장
    pk_press("ctrl", "c")

    # 클립보드에서 변수에 저장
    text_dragged = pk_paste()

    ensure_printed(str_working=rf'''text_dragged="{text_dragged}"  {'%%%FOO%%%' if LTA else ''}''')

    # 클립보드 복원
    clipboard.copy(clipboard_current_contents)

    return text_dragged
