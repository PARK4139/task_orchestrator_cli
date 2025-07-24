


def is_os_wsl_linux():
    from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
    # todo : detect wsl.exe

    if does_pnx_exist(pnx='/mnt/c/Users'):
        # if LTA:
        #     pk_print(f'''wsl os is detected {'%%%FOO%%%' if LTA else ''}''')
        return 1
    else:
        return 0
