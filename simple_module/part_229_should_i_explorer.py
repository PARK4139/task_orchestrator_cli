from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025

from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os


def should_i_explorer():
    while 1:
        dialog = GuiUtil.CustomQdialog(prompt="해당위치의 타겟을 exec 할까요?", btn_list=[YES, NO], input_box_mode=True,
                                       input_box_text_default=pk_paste())
        dialog.exec()
        btn_txt_clicked = dialog.btn_txt_clicked
        input_box_text = dialog.input_box.text()
        if btn_txt_clicked == PkMessages2025.YES:
            pnx = input_box_text
            cmd = rf"explorer {pnx}"
            cmd_to_os(cmd=cmd, mode="a")
            break
        else:
            break
