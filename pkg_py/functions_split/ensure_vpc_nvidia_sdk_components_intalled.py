from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def ensure_vpc_nvidia_sdk_components_intalled(vpc_data):
    if vpc_data.vpc_with_flash_image == 0:
        # jetpack sdk component install 창 자동시현
        if 'no' in vpc_data.vpc_identifier:
            cmd_to_remote_os("sdkmanager --archived-versions")  # wsl 에서 수행
            pass
        elif 'nx' in vpc_data.vpc_identifier:
            pass
        elif 'xc' in vpc_data.vpc_identifier:
            pass
        elif 'evm' in vpc_data.vpc_identifier:
            # sdkmanager
            # show all versions
            # JETPACK 4.6.5
            # Download now. install Later 미체크  #체크 시 플래시imageCREATE 안함 #다음에는 체크해보자 불필요하게 size이 늘거 같은 생각이 든다. 왜냐면 초창기 img  f 은 회사에서는 필요없기 때문
            # APT repository access for Debian package installation(host). 에러발생
            # Skip Check
            # nvidia/nvidia/Flash
            # installation failed
            # retry # reflash
            # #팀Laptop 4.6.5 로 flash 해도 4.6.6 이 INSTALLATION_가 됨.
            pass
        else:
            pk_print(f'''unknown vpc_data.identifier ({vpc_data.vpc_identifier}) {'%%%FOO%%%' if LTA else ''}''',
                     print_color='red')
            raise
    elif vpc_data.vpc_with_flash_image == 1:
        pass
