



from pkg_py.functions_split.cmd_to_os import cmd_to_os


def compress_pnx_via_bz_exe(pnx, f_zip):
    cmd = f'bz.exe c "{f_zip}" "{pnx}"'
    cmd_to_os(cmd=cmd)
