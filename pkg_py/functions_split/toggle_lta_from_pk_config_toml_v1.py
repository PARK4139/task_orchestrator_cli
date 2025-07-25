
break
config_file = F_PK_CONFIG_TOML
current_value = int(line.split('=')[1].strip())
def pk_toggle_lta_from_pk_config_toml_v1():
except Exception as e:
file.writelines(lines)
for i, line in enumerate(lines):
found = False
found = True
from passlib.context import CryptContext
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.system_object.directories import D_PKG_PY
if line.startswith("LOCAL_TEST_ACTIVATE"):
if not found:
import keyboard
lines = file.readlines()
lines[i] = f"LOCAL_TEST_ACTIVATE = {new_value}\n"
new_value = 0 if current_value == 1 else 1
print("Error: 'LOCAL_TEST_ACTIVATE' not found in config file.")
print(f"Error: {e}")
print(f"LOCAL_TEST_ACTIVATE is now set to {new_value}.")
print(f"LTA value successfully toggled and saved to {config_file}.")
return
try:
with open(config_file, 'r', encoding='utf-8') as file:
with open(config_file, 'w', encoding='utf-8') as file:
