from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical


def ensure_copied_and_pasted_with_keeping_clipboard(prompt, wsl_mode=False):
    import inspect

    # copy & paste 기능이 끝났을 때 기존의 클립보드를 유지
    func_n = inspect.currentframe().f_code.co_name

    # paste for backup
    txt_bkup = get_str_from_clipboard()
    txt_bkup_list = txt_bkup.split("\n")
    ensure_iterable_printed_as_vertical(item_iterable=txt_bkup_list, item_iterable_n="txt_bkup_list")

    # copy
    ensure_copied(str_working=prompt)
    ensure_printed(str_working=rf'''prompt={prompt}  {'%%%FOO%%%' if LTA else ''}''')

    # paste
    if wsl_mode == True:
        ensure_pressed("ctrl", "c")
        ensure_pressed("ctrl", "shift", "v")
    else:
        ensure_pressed("ctrl", "v")

    # copy for restore
    ensure_copied(str_working=txt_bkup)
