



from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os


def compress_pnx_via_bz_exe(pnx, f_zip):
    cmd = f'bz.exe c "{f_zip}" "{pnx}"'
    ensure_command_excuted_to_os(cmd=cmd)
