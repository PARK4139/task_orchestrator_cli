from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.directories import D_PKG_TXT
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.encodings import Encoding
from pkg_py.functions_split.ensure_printed import ensure_printed


def save_all_drive_pnxs_to_text_file2():  # 루프 수정필요 # 이 함수는 거의 필요 없을 것 같다. 관심d만 확인하는 것으로 충분해 보인다.
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    f_func_n_txt = rf'{D_PROJECT}\pkg_txt\{func_n}.txt'
    ensure_pnx_made(pnx=f_func_n_txt, mode="item")

    # if not is_window_open(window_title=f_func_n_txt):
    #     open_pnx(f_func_n_txt, debug_mode=True)

    # 1. 특정 경로를 제외할 텍스트 f에서 경로 읽어오기
    def load_pnxs_exclude(file_path):
        import inspect
        func_n = inspect.currentframe().f_code.co_name
        exclude_paths = set()
        try:
            with open(file=file_path, mode='r', encoding=Encoding.UTF8.value) as file:
                for line in file:
                    exclude_paths.add(line.strip())
        except PermissionError as e:
            print(f"PermissionError: {e}. Check if the item is accessible and you have the right permissions.")
        except Exception as e:
            print(f"Error opening item {file_path}: {e}")
        return exclude_paths

    # 2. 모든 드라이브에서 f 목록 가져오기
    def get_drives_connected():
        import inspect
        import os
        import string

        func_n = inspect.currentframe().f_code.co_name
        drives = []
        for letter in string.ascii_uppercase:
            drive = f"{letter}:\\"
            if os.path.exists(drive):
                drives.append(drive)
        ensure_printed(str_working=rf'''drives="{drives}"  {'%%%FOO%%%' if LTA else ''}''')
        return drives

    # 3. 드라이브에서 f 검색하고 처리하기
    def list_files_in_drives(exclude_paths_txt):

        import inspect
        import os

        func_n = inspect.currentframe().f_code.co_name
        exclude_paths = load_pnxs_exclude(exclude_paths_txt)
        drives = get_drives_connected()
        cnt = 0
        pnxs = []
        limit = 10000
        cnt_f_list = limit
        cnt_txt_files = 0
        temp = set()
        # 모든 드라이브에서 f 탐색
        for drive in drives:
            ensure_printed(str_working=rf'''drive="{drive}"  {'%%%FOO%%%' if LTA else ''}''')
            for root, d_nx_list, f_nx_list in os.walk(drive):
                for f_nx in f_nx_list:
                    f = os.path.join(root, f_nx)
                    # ensure_printed(str_working=rf'''f="{f}"  {'%%%FOO%%%' if LTA else ''}''')
                    cnt_f_list = cnt_f_list - 1
                    pnxs.append(f)
                    if cnt_f_list == 0:
                        # ensure_printed(str_working=rf'''f="{f}"  {'%%%FOO%%%' if LTA else ''}''')
                        cnt_f_list = limit
                        cnt_txt_files = cnt_txt_files + 1
                        # ensure_printed(str_working=rf'''cnt_txt_files="{cnt_txt_files}"  {'%%%FOO%%%' if LTA else ''}''')

                        output_pnx_txt_before = rf"{D_PKG_TXT}\{func_n}_{cnt_txt_files - 1}.txt"
                        temp = get_list_from_f(f=output_pnx_txt_before)
                        if None != temp:
                            if 0 == len(temp):
                                cnt_txt_files = cnt_txt_files - 1

                        output_pnx_txt = rf"{D_PKG_TXT}\{func_n}_{cnt_txt_files}.txt"
                        # ensure_printed(str_working=rf'''output_pnx_txt="{output_pnx_txt}"  {'%%%FOO%%%' if LTA else ''}''')
                        # if any(exclude_path in f for exclude_path in exclude_paths):
                        #     continue
                        with open(file=output_pnx_txt, mode='w', encoding=Encoding.UTF8.value) as f:
                            for pnx in pnxs:
                                cnt = cnt + 1
                                # temp.add(rf"{pnx.split("\\")[0]}\{pnx.split("\\")[1]}")
                                # print(temp)
                                for exclude_path in exclude_paths:
                                    if exclude_path in pnx:
                                        break
                                else:
                                    if not pnx.strip() == "":
                                        f.write(f'{pnx}\n')
                                        ensure_printed(
                                            str_working=rf'''cnt="{cnt}" pnxs="{pnx}" output_pnx_txt="{output_pnx_txt}"  {'%%%FOO%%%' if LTA else ''}''')
                                    else:
                                        ensure_printed(f'''없다''')
        ensure_printed(str_working=rf'''temp="{temp}"  {'%%%FOO%%%' if LTA else ''}''')

    # exec
    exclude_paths_txt = rf'{D_PKG_TXT}\{func_n}_exclude_paths.txt'
    ensure_pnx_made(pnx=exclude_paths_txt, mode='item')
    list_files_in_drives(exclude_paths_txt)
