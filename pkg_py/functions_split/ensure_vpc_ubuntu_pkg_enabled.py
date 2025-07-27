

def ensure_vpc_ubuntu_pkg_enabled(vpc_data, config_remote_os):
    # todo 1개씩 나눠서 설치 후 설치여부 재확인    # wsl 환경에 설치
    cmd_to_remote_os(cmd='sudo apt install -y libxml2-utils', **config_remote_os)
    cmd_to_remote_os(cmd='sudo apt install -y simg2img', **config_remote_os)  # 설치 실패
    # Package simg2img is not available, but is referred to by another package.
    # This may mean that the package is missing, has been obsoleted, or
    # is only available from another source
    # However the following packages replace it:
    #   android-sdk-libsparse-utils
    #
    # E: Package 'simg2img' has no installation candidate
    cmd_to_remote_os(cmd='sudo apt install -y abootimg liblz4-tool binutils', **config_remote_os)
    if 'no' in vpc_data.vpc_identifier:
        pass
    if 'nx' in vpc_data.vpc_identifier:
        pass
