from tkinter import UNDERLINE

from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.simple_module.part_014_pk_print import pk_print


def save_all_drive_pnxs_to_txt_f():  # 이 함수는 Everything.exe 를 대체할 f탐색기 용도로 만들었으나 거의 필요 없을 것 같다. 관심d만 확인하는 것으로 충분해 보인다.
    """모든 f d에 대한 정보를 텍스트 f로 저장하는 함수"""
    import os

    # 윈도우냐 아니야에 따라
    # os.system('chcp 65001 >nul')
    # os.system('export LANG=en_US.UTF-8 >nul')

    opening_d = os.getcwd()
    proper_tree_txt = rf"{D_PROJECT}\pkg_all_tree\proper_tree.txt"
    all_tree_txt = rf"{D_PROJECT}\pkg_all_tree\all_tree.txt"
    if not os.path.exists(os.path.dirname(all_tree_txt)):
        os.makedirs(os.path.dirname(all_tree_txt))
        # os.system(f'echo. >> "{all_tree_txt}"')
        os.system(f'echo. >> "{all_tree_txt}" >nul')
        os.system(f'echo. >> "{proper_tree_txt}" >nul')
    with open(file=all_tree_txt, mode='w', encoding=Encoding.UTF8.value) as f:
        f.write(" ")
    with open(file=proper_tree_txt, mode='w', encoding=Encoding.UTF8.value) as f:
        f.write(" ")

    drives = "foo"

    f_cnt = 0
    f = open(D_PROJECT + '\\all_list.txt', 'a', encoding=Encoding.UTF8.value)  # >>  a    > w   각각 대응됨.
    for drive in drives:
        pk_chdir(drive)
        for root, d_nx_list, f_nx_list in os.walk(os.getcwd()):  # 여기 또 os.getcwd() 있는 부분 수정하자..
            for f_nx in f_nx_list:
                f_cnt = f_cnt + 1
                f.write(str(f_cnt) + " " + os.path.join(root, f_nx) + "\n")
    f.close()  # close() 를 사용하지 않으려면 with 문을 사용하는 방법도 있다.
    pk_print(f"{UNDERLINE}{UNDERLINE}all_list.txt writing e", print_color='blue')
    pk_print(f"{UNDERLINE}{UNDERLINE}all_list_proper.txt rewriting s", print_color='blue')
    texts_black = [
        rf"C:\$WinREAgent",
        rf"C:\mingw64",
        rf"C:\PerfLogs",
        rf"C:\Program Files (x86)",
        rf"C:\Program Files",
        rf"C:\ProgramData",
        rf"C:\Temp",
        rf"C:\Users\All Users",
        rf"C:\Windows\servicing",
        rf"C:\Windows\SystemResources",
        rf"C:\Windows\WinSxS",
        rf"C:\Users\Default",
        rf"C:\Users\Public",
        rf"C:\Windows.old",
        rf"C:\Windows",
        rf"C:\$Recycle.Bin",
        rf"D:\$RECYCLE.BIN",
        rf"E:\$RECYCLE.BIN",
        rf"E:\$Recycle.Bin",
        rf"F:\$RECYCLE.BIN",
        rf"{D_HOME}\AppData",
    ]
    texts_white = [
        ".mkv",
    ]
    f = open(rf'{D_PROJECT}\all_list.txt', 'r+', encoding=Encoding.UTF8.value)
    f2 = open(rf'{D_PROJECT}\all_list_proper.txt', 'a', encoding=Encoding.UTF8.value)
    lines_cnt = 0
    while 1:
        line = f.readline()
        if not line:
            break
        lines_cnt = lines_cnt + 1
        if any(text_black not in line for text_black in texts_black):
            # pk_print(line)
            if any(text_white in line for text_white in texts_white):
                # pk_print(line.split("\n")[0] + " o")
                f2.write(line.split("\n")[0] + " o " + "\n")
                # pk_print('o')
                pass
            else:
                # pk_print(line.split("\n")[0] + " x")
                # f2.write(line.split("\n")[0] + " x "+"\n")
                # pk_print('x')
                pass
    f.close()
    f2.close()
    pk_print(f"{UNDERLINE}{UNDERLINE}all_list_proper.txt rewriting e", print_color='blue')

    pk_print(f"{UNDERLINE}{UNDERLINE}files opening s", print_color='blue')
    pk_chdir(os.getcwd())

    # 윈도우냐 아니냐
    os.system("chcp 65001 >nul")
    os.system('export LANG=en_US.UTF-8 >nul')

    # os.system("type all_list.txt")
    # os.system("explorer all_list.txt")
    os.system("explorer all_list_proper.txt")
    pk_print(f"{UNDERLINE}{UNDERLINE}files opening e", print_color='blue')

    # os.system('del "'+os.getcwd()+'\\all_list.txt"')
    # mk("all_list.txt")
    pk_print(f"{UNDERLINE}{UNDERLINE}e", print_color='blue')
