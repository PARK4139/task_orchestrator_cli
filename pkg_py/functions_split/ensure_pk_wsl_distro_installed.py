from pkg_py.pk_system_object.print_red import print_red
from pkg_py.pk_system_object.directories import D_DOWNLOADS

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.pk_system_object.print_red import print_red

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.pk_system_object.directories import D_DOWNLOADS
from pkg_py.functions_split.pk_print import pk_print


def ensure_pk_wsl_distro_installed():
    """
    1. PK_WSL_DISTRO_N이 이미 설치되어 있으면 건너뜀
    2. DEFAULT_DISTRO가 설치 안 됐으면 install
    3. DEFAULT_DISTRO export -> unregister -> import as PK_WSL_DISTRO_N
    4. 성공 시 tar 파일 삭제
    """
    from pathlib import Path

    # 설정 기본값
    DEFAULT_DISTRO = "Ubuntu-24.04"
    # DEFAULT_DISTRO = "Ubuntu-18.04"
    pk_print(f"PK_WSL_DISTRO_N={PK_WSL_DISTRO_N}{' %%%FOO%%%' if LTA else ''}")
    pk_print(f"DEFAULT_DISTRO={DEFAULT_DISTRO}{' %%%FOO%%%' if LTA else ''}")

    wsl_distro_name_installed = get_wsl_distro_name(cmd="wsl -l -v")
    pk_print(f'''wsl_distro_name_installed={wsl_distro_name_installed} {'%%%FOO%%%' if LTA else ''}''')
    # # 1) 이미 PK_WSL_DISTRO_N 확인
    if PK_WSL_DISTRO_N or rf'* {PK_WSL_DISTRO_N}' == wsl_distro_name_installed:
        pk_print(f"'{PK_WSL_DISTRO_N}' 배포판이 이미 설치되어 있습니다. 설치를 건너뜁니다.")
        return True

    # 2) DEFAULT_DISTRO 설치 여부
    if DEFAULT_DISTRO not in wsl_distro_name_installed:
        wsl_distro_name_installable_from_online = get_wsl_distro_name(cmd="wsl --list --online")
        pk_print(
            f'''wsl_distro_name_installable_from_online={wsl_distro_name_installable_from_online} {'%%%FOO%%%' if LTA else ''}''')
        if DEFAULT_DISTRO not in wsl_distro_name_installable_from_online:
            print_red(f"'{DEFAULT_DISTRO}' 배포판을 online 목록에서 찾을 수 없습니다.")
            return False
        else:
            pk_print(f"'{DEFAULT_DISTRO}' 배포판을 online 목록에서 찾았습니다.")
        pk_print(f"'{DEFAULT_DISTRO}' 배포판을 설치합니다...")
        try:
            cmd_to_os_with_splited_arg(["wsl", "--install", "-d", DEFAULT_DISTRO])
        except Exception as e:
            print_red(f"설치 명령 실패: {e}")
            return False
    else:
        pk_print(f"'{DEFAULT_DISTRO}' 배포판이 이미 설치되어 있습니다.")

    # 3) export, unregister, import

    tar_path = Path.cwd() / f"{DEFAULT_DISTRO}.tar"  # 임시 export 파일 경로
    install_path = Path(D_DOWNLOADS) / PK_WSL_DISTRO_N  # import 설치 디렉토리
    try:
        pk_print(f"'{DEFAULT_DISTRO}' 배포판을 '{tar_path}'로 export합니다.")
        cmd_to_os_with_splited_arg(["wsl", "--export", DEFAULT_DISTRO, str(tar_path)])

        pk_print(f"'{DEFAULT_DISTRO}' 배포판을 unregister 합니다.")
        cmd_to_os_with_splited_arg(["wsl", "--unregister", DEFAULT_DISTRO])

        pk_print(f"'{tar_path}'를 '{install_path}'에 import하여 '{PK_WSL_DISTRO_N}'으로 등록합니다.")
        install_path.mkdir(parents=True, exist_ok=True)
        cmd_to_os_with_splited_arg(["wsl", "--import", PK_WSL_DISTRO_N, str(install_path), str(tar_path)])
    except Exception as e:
        print_red(f"export/import 중 오류: {e}")
        return False

    # 4) 등록 확인 및 tar 파일 삭제
    wsl_distro_name_installed_after = get_wsl_distro_name(cmd="wsl -l -v")
    pk_print(f'''wsl_distro_name_installed_after={wsl_distro_name_installed_after} {'%%%FOO%%%' if LTA else ''}''')
    if PK_WSL_DISTRO_N or rf'* {PK_WSL_DISTRO_N}' in wsl_distro_name_installed_after:
        pk_print(f"'{PK_WSL_DISTRO_N}' 배포판이 정상적으로 import되었습니다.")
        if tar_path.exists():
            pk_print(f"'{tar_path}' 파일을 삭제합니다.")
            tar_path.unlink()
        return True
    else:
        print_red("import 후에도 배포판을 확인할 수 없습니다.")
        return False
