
cmd_to_os('powershell.exe Get-Clipboard')
def pk_paste():
else:
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
if is_os_wsl_linux():
import clipboard
return clipboard.paste()
