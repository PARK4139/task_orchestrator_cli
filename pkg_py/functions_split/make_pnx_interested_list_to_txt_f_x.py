

from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.system_object.directories import D_PKG_TXT
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical


def make_pnx_interested_list_to_txt_f_x(pnx_interested_list=None, string_exclude=None):
    import inspect

    # todo f 내용 초기화 되어야 한다.
    func_n = inspect.currentframe().f_code.co_name

    # pnx_interested_list = []
    if pnx_interested_list is None:
        pnx_interested_list = [
            rf'{D_DOWNLOADS}',
            rf'{D_HOME}\AppData\Roaming\bittorrent',

            rf'D:\\',
            rf'E:\\',
            rf'F:\\',
        ]
    if string_exclude is None:
        string_exclude = [
            rf'{D_DOWNLOADS}\[]\docker_image_maker\venv',
            rf'{D_DOWNLOADS}\[]\test_flutter(모바일 프론트 엔드 용도)\ios',
            rf'{D_DOWNLOADS}\[]\test_flutter(모바일 프론트 엔드 용도)\macos',
            rf'{D_DOWNLOADS}\[]\test_flutter(모바일 프론트 엔드 용도)\windows',
            rf'{D_DOWNLOADS}\[]\test_flutter(모바일 프론트 엔드 용도)\web',
            rf'{D_DOWNLOADS}\[]\test_flutter(모바일 프론트 엔드 용도)\linux',
            rf'{D_DOWNLOADS}\[]\test_flutter(모바일 프론트 엔드 용도)\lib',
            rf'{D_DOWNLOADS}\[]\test_flutter(모바일 프론트 엔드 용도)\build',
            rf'{D_DOWNLOADS}\[]\test_flutter(모바일 프론트 엔드 용도)\asset',
            rf'{D_DOWNLOADS}\[]\test_flutter(모바일 프론트 엔드 용도)\android',

            rf'D:\$RECYCLE.BIN',
            rf'D:\System Volume Information',

            rf'E:\$RECYCLE.BIN',
            rf'E:\System Volume Information',

            rf'F:\$RECYCLE.BIN',
            rf'F:\System Volume Information',

            rf'deprecated',
            rf'[ARCHIVED]',
            rf'.git',
            rf'.idea',
            rf'venv',
            rf'node_modules',
            rf'test_flutter',
            rf'pkg_font',
            rf'telegram memo export by static web',
            rf'docker_image_maker',
            rf'e-magazine',
            rf'netlify-web',
        ]
    pnx_processed_list = []
    file_cnt = 0
    write_cnt = 0
    write_cnt_limit = 1000000
    for pnx_interested in pnx_interested_list:
        pnxs_with_walking = get_pnxs(d_working=pnx_interested, filter_option="f", with_walking=1)

        # 'pnxs_exclude'를 set으로 변경하여 'in' 연산을 최적화
        func_n_file_cnt_txt = None
        for pnx_with_walking in pnxs_with_walking:
            # 빠른 'in' 연산을 위해 set으로 변환된 pnxs_exclude 활용
            if any(pnx_exclude in pnx_with_walking for pnx_exclude in string_exclude):
                continue  # 'pnx_exclude'에 포함되면 건너뛰기
            # 'exclude' 목록에 포함되지 않으면 'pnx_processed_list'에 추가
            pnx_processed_list.append(pnx_with_walking)
            # ensure_printed(str_working=rf'''len(pnx_processed_list)="{len(pnx_processed_list)}"  {'%%%FOO%%%' if LTA else ''}''')
            if write_cnt == write_cnt_limit % 2 == 0:
                file_cnt = file_cnt + 1
                ensure_iterable_printed_as_vertical(item_iterable=pnx_processed_list, item_iterable_n="pnx_processed_list")
                # func_n_file_cnt_txt = rf"{D_PKG_TXT}\{func_n}_{file_cnt}.txt"
                # ensure_list_written_to_file(texts=pnx_processed_list, pnx=func_n_file_cnt_txt, mode="w")
            func_n_file_cnt_txt = rf"{D_PKG_TXT}\{func_n}_{file_cnt}.txt"
            # ensure_printed(str_working=rf'''write_cnt="{write_cnt}"  {'%%%FOO%%%' if LTA else ''}''')
            ensure_str_writen_to_f(msg=f"{pnx_with_walking}\n", f=func_n_file_cnt_txt, mode="a")
            write_cnt = write_cnt + 1
            if write_cnt == write_cnt_limit % 2 == 0:
                window_title = rf"{func_n}_{file_cnt}"
                # if not is_window_open(window_title_seg=window_title):
                #     open_pnx(pnx=func_n_file_cnt_txt)
