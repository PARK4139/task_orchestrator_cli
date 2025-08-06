from pkg_py.system_object.color_map import ANSI_COLOR_MAP


def ensure_wifi_pw_printed():
    from pkg_py.functions_split.get_str_from_list import get_str_from_list
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.functions_split import ensure_command_excuted_to_os

    wifi_names = None
    signiture_str = '모든 사용자 프로필 : '
    std_list = ensure_command_excuted_to_os(f'netsh wlan show profile')
    std = get_str_from_list(std_list)
    # ensure_printed(f'''std={std} {'%%%FOO%%%' if LTA else ''}''')
    if signiture_str in std:
        # ensure_printed(str_working=rf'''wifi_names="{wifi_names}" {'%%%FOO%%%' if LTA else ''}''', print_color='green')
        wifi_names = std.split(signiture_str)[1].split(", ")
    wifi_name = wifi_names[0]  # pk_option # TBD 패스워드를 목록들로 나오도록
    ensure_printed(f'''wifi_name={wifi_name} {'%%%FOO%%%' if LTA else ''}''')

    wifi_pw = None
    signiture_str = "키 콘텐츠"
    std_list = ensure_command_excuted_to_os(f'netsh wlan show profile "{wifi_name}" key=clear | find "{signiture_str}"')
    # ensure_printed(f'''std_list={std_list} {'%%%FOO%%%' if LTA else ''}''')
    # ensure_printed(f'''std_list[0]={std_list[0]} {'%%%FOO%%%' if LTA else ''}''')
    # wifi_pw = std_list[0]
    # wifi_pw = std_list[0].split(signiture_str)[1]
    wifi_pw = std_list[0].split(signiture_str)[1].split(":")[1].strip()
    ensure_printed(rf'''{ANSI_COLOR_MAP['YELLOW']}wifi_pw="{wifi_pw}{ANSI_COLOR_MAP['RESET']}" {'%%%FOO%%%' if LTA else ''}''', print_color='green')
