import win32con
import pyglet
import json
import functools
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from bs4 import ResultSet
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style


def ensure_vpc_aifw_running(vpc_data, config_remote_os):
    remove_vpc_aifw(vpc_data, config_remote_os)
    # 노션/AI_Framework 2 도커 환경 셋업  # apply target :NX , NO
    # run_container 레포 같은데
    download_vpc_aifw_docker_image(vpc_data, config_remote_os)
    ensure_vpc_config_right(vpc_data, config_remote_os)
    run_vpc_aifw_docker_container(vpc_data, config_remote_os)
    download_aifw(vpc_data, config_remote_os)
    build_aifw(vpc_data, config_remote_os)
    # exit_docker_container() ?
    ensure_aifw_running(vpc_data, config_remote_os)  # ?
