
cmd_to_os('echo TBD')
def pk_lock_os():
elif is_os_wsl_linux():
else:
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.save_power_as_s3 import save_power_as_s3
if is_os_windows():
save_power_as_s3()
