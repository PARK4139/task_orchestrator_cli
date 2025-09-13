import logging
from pathlib import Path

from functions import ensure_slept
from functions.get_list_from_f import get_list_from_f
from functions.get_list_from_set import get_list_from_set
from functions.get_list_interested_from_list import get_list_interested_from_list
from functions.get_list_replaced_element_from_str_to_str import get_list_replaced_element_from_str_to_str
from functions.get_pnx_excluded_list import get_pnx_excluded_list
from functions.get_set_from_list import get_set_from_list
from functions.is_internet_connected import is_internet_connected
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.get_nx import get_nx
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_windows import is_os_windows
from sources.objects.pk_local_test_activate import LTA
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_HOME


def load_magnet_set_to_bittorrent():
    import webbrowser

    if not is_internet_connected():
        raise

    # pk_magnets.txt explorer
    f = rf'{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}/pk_magnets.txt'
    if is_os_windows():
        ensure_command_executed(cmd=rf'explorer "{get_pnx_windows_style(f)}"', mode="a")
        if not ensure_window_to_front(get_nx(f)):
            ensure_window_to_front(get_nx(f))
    # else:
    #     f = get_pnx_unix_style(f)
    # ensure_command_executed(cmd=rf'sudo nano "{f}"', debug_mode=True, mode="a")

    answer = ensure_value_completed(key_hint='answer(o/x)', options=['o', 'x'])
    if answer != 'o':
        return
    magnet_list = get_list_from_f(f=Path(f))

    # f.torrent 이 있는 경우, # magnets_set 에서  magnet remove
    d_bittorrent = [
        rf'{D_HOME}\AppData\Roaming\bittorrent',
    ]
    exclusion_list = [
        rf'.dat', rf'.dll', rf'.exe', rf'.dmp', rf'.lng', rf'.zip',
        rf'D:\$RECYCLE.BIN',
        rf'D:\System Volume Information',

        rf'E:\$RECYCLE.BIN',
        rf'E:\System Volume Information',

        rf'F:\$RECYCLE.BIN',
        rf'F:\System Volume Information',

        rf'deprecated',
        rf'archived',
        rf'.git',
        rf'.idea',
        rf'venv',
        rf'node_modules',
        rf'test_flutter',
        rf'task_orchestrator_cli_sensitive_public',
        rf'telegram memo export by static web',
        rf'docker_image_maker',
        rf'e-magazine',
        rf'netlify-web',
    ]
    logging.debug(f'''d_bittorrent={d_bittorrent}  {'%%%FOO%%%' if LTA else ''}''')
    logging.debug(f'''exclusion_list={exclusion_list}  {'%%%FOO%%%' if LTA else ''}''')
    f_torrent_from_d_bittorrent_list = get_pnx_excluded_list(d_working_list=d_bittorrent, exclusion_list=exclusion_list)
    logging.debug(f'''f_torrent_from_d_bittorrent_list={f_torrent_from_d_bittorrent_list}  {'%%%FOO%%%' if LTA else ''}''')
    f_torrent_from_d_bittorrent_list = get_list_interested_from_list(working_list=f_torrent_from_d_bittorrent_list,
                                                                     ext_list_include=[".torrent"])
    logging.debug(f'''f_torrent_from_d_bittorrent_list={f_torrent_from_d_bittorrent_list}  {'%%%FOO%%%' if LTA else ''}''')
    f_torrent_from_d_bittorrent_list = get_list_replaced_element_from_str_to_str(
        working_list=f_torrent_from_d_bittorrent_list,
        from_str=f'C:\\Users\\WIN10PROPC3\\AppData\\Roaming\\bittorrent\\', to_str='')
    logging.debug(f'''f_torrent_from_d_bittorrent_list={f_torrent_from_d_bittorrent_list}  {'%%%FOO%%%' if LTA else ''}''')
    f_torrent_from_d_bittorrent_list = get_list_replaced_element_from_str_to_str(
        working_list=f_torrent_from_d_bittorrent_list, from_str=rf'.torrent', to_str='')
    logging.debug(f'''f_torrent_from_d_bittorrent_list={f_torrent_from_d_bittorrent_list}  {'%%%FOO%%%' if LTA else ''}''')
    f_torrent_set = get_set_from_list(working_list=f_torrent_from_d_bittorrent_list)
    logging.debug(f'''f_torrent_set={f_torrent_set}  {'%%%FOO%%%' if LTA else ''}''')
    magnet_required_set = {magnet for magnet in magnet_list if not any(torrent in magnet for torrent in f_torrent_set)}
    magnet_set = magnet_required_set
    magnet_list = get_list_from_set(magnet_set)
    magnet_list = [magnet for magnet in
                   sorted(magnet_list, key=lambda magnet: magnet.split("&dn=")[1] if "&dn=" in magnet else "")]
    logging.debug(f'''{len(magnet_list)} magnets are loading...  {'%%%FOO%%%' if LTA else ''}''')
    for magnet in magnet_list:
        if magnet.strip() == "":
            continue
        logging.debug(f'''magnet={magnet}  {'%%%FOO%%%' if LTA else ''}''')
        interval_seconds = int(ensure_value_completed(key_hint='interval_seconds', options=['1000', '5000', '10000']))
        if "&mgt_url=" in magnet:
            magnet = magnet.split("&mgt_url=")[1].strip()
            webbrowser.open(magnet)
        else:
            webbrowser.open(magnet)
        ensure_slept(milliseconds=interval_seconds)
        ensure_pressed("alt", "n")
