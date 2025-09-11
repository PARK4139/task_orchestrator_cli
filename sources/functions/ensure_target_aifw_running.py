import win32con
import pyglet
import json
import functools
from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.get_list_sorted import get_list_sorted
from bs4 import ResultSet
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style


def ensure_target_aifw_running (target_device_data, remote_device_target_config):
    remove_target_aifw (target_device_data, remote_device_target_config)
    # 노션/AI_Framework 2 도커 환경 셋업  # apply target :NX , NO
    # run_container 레포 같은데
    download_target_aifw_docker_image (target_device_data, remote_device_target_config)
    ensure_target_config_right (target_device_data, remote_device_target_config)
    run_target_aifw_docker_container (target_device_data, remote_device_target_config)
    download_aifw (target_device_data, remote_device_target_config)
    build_aifw (target_device_data, remote_device_target_config)
    # exit_docker_container() ?
    ensure_aifw_running (target_device_data, remote_device_target_config)  # ?
