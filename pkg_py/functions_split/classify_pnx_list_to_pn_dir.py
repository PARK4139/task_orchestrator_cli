import urllib
import tomllib
import mutagen
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.system_object.files import F_FFMPEG_EXE
from dataclasses import dataclass
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.functions_split.pk_print import pk_print


def classify_pnx_list_to_pn_dir(d_working):
    import os

    for pnx_nx in os.listdir(d_working):
        pnx_item = os.path.join(d_working, pnx_nx)
        if is_f(pnx_item):
            pk_print(f'''pnx_item={pnx_item}''')
            f_n_d = os.path.join(d_working, pnx_nx)
            f_n_d_pn = get_pn(f_n_d)

            if not os.path.exists(f_n_d_pn):
                os.makedirs(f_n_d_pn)

            # shutil.move(pnx_item, f_n_d_pn) # 중복있으면 에러로 처리됨
            move_pnx(pnx=pnx_item, d_dst=f_n_d_pn)  # 중복있으면 timestamp를 붙여 이동됨
