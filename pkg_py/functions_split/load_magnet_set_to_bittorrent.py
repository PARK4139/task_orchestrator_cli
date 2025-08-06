# from pkg_py.system_object.is_os_windows import is_os_windows

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.directories import D_PKG_CACHE_PRIVATE
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os

from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front


def load_magnet_set_to_bittorrent():
    import webbrowser

    if not is_internet_connected():
        raise

    # pk_magnets.txt explorer
    f = rf'{D_PKG_CACHE_PRIVATE}/pk_magnets.txt'
    if is_os_windows():
        ensure_command_excuted_to_os(cmd=rf'explorer "{get_pnx_windows_style(f)}"', mode="a")
        if not is_front_window_title(window_title_seg=get_nx(f)):
            ensure_window_to_front(window_title_seg=get_nx(f))
    # else:
    #     f = get_pnx_unix_style(f)
    # ensure_command_excuted_to_os(cmd=rf'sudo nano "{f}"', debug_mode=True, mode="a")

    answer = get_value_completed(key_hint='answer(o/x)=', values=['o', 'x'])
    if answer != 'o':
        return
    magnet_list = get_list_from_f(f=get_pnx_os_style(f))

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
        rf'pkg_cache_private_public',
        rf'telegram memo export by static web',
        rf'docker_image_maker',
        rf'e-magazine',
        rf'netlify-web',
    ]
    ensure_printed(f'''d_bittorrent={d_bittorrent}  {'%%%FOO%%%' if LTA else ''}''')
    ensure_printed(f'''exclusion_list={exclusion_list}  {'%%%FOO%%%' if LTA else ''}''')
    f_torrent_from_d_bittorrent_list = get_pnx_excluded_list(d_working_list=d_bittorrent, exclusion_list=exclusion_list)
    ensure_printed(f'''f_torrent_from_d_bittorrent_list={f_torrent_from_d_bittorrent_list}  {'%%%FOO%%%' if LTA else ''}''')
    f_torrent_from_d_bittorrent_list = get_list_interested_from_list(working_list=f_torrent_from_d_bittorrent_list,
                                                                     ext_list_include=[".torrent"])
    ensure_printed(f'''f_torrent_from_d_bittorrent_list={f_torrent_from_d_bittorrent_list}  {'%%%FOO%%%' if LTA else ''}''')
    f_torrent_from_d_bittorrent_list = get_list_replaced_element_from_str_to_str(
        working_list=f_torrent_from_d_bittorrent_list,
        from_str=f'C:\\Users\\WIN10PROPC3\\AppData\\Roaming\\bittorrent\\', to_str='')
    ensure_printed(f'''f_torrent_from_d_bittorrent_list={f_torrent_from_d_bittorrent_list}  {'%%%FOO%%%' if LTA else ''}''')
    f_torrent_from_d_bittorrent_list = get_list_replaced_element_from_str_to_str(
        working_list=f_torrent_from_d_bittorrent_list, from_str=rf'.torrent', to_str='')
    ensure_printed(f'''f_torrent_from_d_bittorrent_list={f_torrent_from_d_bittorrent_list}  {'%%%FOO%%%' if LTA else ''}''')
    f_torrent_set = get_set_from_list(working_list=f_torrent_from_d_bittorrent_list)
    ensure_printed(f'''f_torrent_set={f_torrent_set}  {'%%%FOO%%%' if LTA else ''}''')
    magnet_required_set = {magnet for magnet in magnet_list if not any(torrent in magnet for torrent in f_torrent_set)}
    magnet_set = magnet_required_set
    magnet_list = get_list_from_set(magnet_set)
    magnet_list = [magnet for magnet in
                   sorted(magnet_list, key=lambda magnet: magnet.split("&dn=")[1] if "&dn=" in magnet else "")]
    ensure_printed(f'''{len(magnet_list)} magnets are loading...  {'%%%FOO%%%' if LTA else ''}''')
    for magnet in magnet_list:
        if magnet.strip() == "":
            continue
        ensure_printed(f'''magnet={magnet}  {'%%%FOO%%%' if LTA else ''}''')
        interval_seconds = int(get_value_completed(key_hint='interval_seconds=', values=['1000', '5000', '10000']))
        if "&mgt_url=" in magnet:
            magnet = magnet.split("&mgt_url=")[1].strip()
            webbrowser.open(magnet)
        else:
            webbrowser.open(magnet)
        ensure_slept(milliseconds=interval_seconds)
        ensure_pressed("alt", "n")
