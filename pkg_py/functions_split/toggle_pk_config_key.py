
# pk_config의 value가 bool인 경우만 사용가능
assert new_value in (0, 1), "value must be 0 or 1"
back_up_f_without_duplication_at_f_location(F_PK_CONFIG_TOML)
config = tomllib.load(f)
config = tomllib.load(f_obj)
config[key] = new_value
current = get_pk_config_for_toggling(key)
def get_pk_config_for_toggling(key) -> int:
def pk_toggle_pk_config_key(key):
def set_pk_config_for_toggling(key, new_value: int):
except Exception as e:
from pkg_py.functions_split.print import pk_print
if current == -1:
import toml  # toml:    쓰기 기능 추천
import tomllib
import tomllib  # tomllib: 파싱/읽기 전용, binary 모드로 읽어야 하는 이유?
new_value = 0 if current == 1 else 1
pk_print(f"{key} {e}", print_color='red')
print(f"[ERROR][toggle] {e}")
print(f"set {key} = {new_value} {e}")
print(f"set {key} = {new_value}")
return
return -1
return int(config.get(key, 0))
set_pk_config_for_toggling(key, new_value)
toml.dump(config, f_obj)
try:
with open(F_PK_CONFIG_TOML, 'rb') as f:
with open(F_PK_CONFIG_TOML, 'rb') as f_obj:
with open(F_PK_CONFIG_TOML, 'w', encoding='utf-8') as f_obj:
