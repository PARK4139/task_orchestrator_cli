from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def ensure_location_about_system_img_and_system_img_raw(config_remote_os):
    # ~/Downloads/flash/xc_flash/Linux_for_Tegra/bootloader/ 안에 system.img* 이 있으면 정상.
    dst = '~/Downloads/flash/xc_flash/Linux_for_Tegra/bootloader/'
    cmd = rf'sudo find {dst} -type f -name "system.img*"'
    std_out, std_err = cmd_to_remote_os(cmd=cmd, **config_remote_os)
    std_list = std_out.split('\n')
    if not check_signiture_in_loop(time_limit=10, working_list=std_list, signiture="/bootloader/system.img",
                                   signiture_found_ment=rf'system.img found in {dst}'):
        pk_print(working_str=rf'''system.img* not found in the expected path ({dst}).  {'%%%FOO%%%' if LTA else ''}''',
                 print_color='red')
        raise  # todo raise 보다는 ipdb 로 대체하여 에러가 난 위치에서 수동으로 재시도 해볼 수 있도록 하는게 나을것 같다. ipdb 가 함수 호출부에서 이루어져도록 수정필요할 수도 있다.
