

def get_wsl_pw(wsl_distro_n):
    # return get_token_from_f_txt(f_token=rf'{D_PKG_TXT}\token_pw_wsl.txt', initial_str="")
    wsl_distro_number = wsl_distro_n.split('-')[1].split('.')[0]
    return get_pk_token(f_token=rf'{D_PKG_TOML}/pk_token_pw_wsl_{wsl_distro_number}.toml', initial_str="")
