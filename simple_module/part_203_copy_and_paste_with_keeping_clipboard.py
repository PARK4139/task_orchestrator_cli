from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical


def copy_and_paste_with_keeping_clipboard(prompt, wsl_mode=False):
    import inspect

    # copy & paste 기능이 끝났을 때 기존의 클립보드를 유지
    func_n = inspect.currentframe().f_code.co_name

    # paste for backup
    txt_bkup = get_str_from_clipboard()
    txt_bkup_list = txt_bkup.split("\n")
    print_iterable_as_vertical(item_iterable=txt_bkup_list, item_iterable_n="txt_bkup_list")

    # copy
    pk_copy(working_str=prompt)
    pk_print(working_str=rf'''prompt={prompt}  {'%%%FOO%%%' if LTA else ''}''')

    # paste
    if wsl_mode == True:
        pk_press("ctrl", "c")
        pk_press("ctrl", "shift", "v")
    else:
        pk_press("ctrl", "v")

    # copy for restore
    pk_copy(working_str=txt_bkup)
