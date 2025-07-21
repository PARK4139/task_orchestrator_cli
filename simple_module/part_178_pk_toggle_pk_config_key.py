from pkg_py.simple_module.part_014_pk_print import pk_print


def pk_toggle_pk_config_key(key):
    # pk_config의 value가 bool인 경우만 사용가능

    def get_pk_config_for_toggling(key) -> int:

        import tomllib
        try:
            with open(F_PK_CONFIG_TOML, 'rb') as f:
                config = tomllib.load(f)
            return int(config.get(key, 0))
        except Exception as e:
            pk_print(f"{key} {e}", print_color='red')
            return -1

    def set_pk_config_for_toggling(key, new_value: int):
        import toml  # toml:    쓰기 기능 추천
        import tomllib  # tomllib: 파싱/읽기 전용, binary 모드로 읽어야 하는 이유?
        try:
            assert new_value in (0, 1), "value must be 0 or 1"
            back_up_f_without_duplication_at_f_location(F_PK_CONFIG_TOML)
            with open(F_PK_CONFIG_TOML, 'rb') as f_obj:
                config = tomllib.load(f_obj)

            config[key] = new_value
            with open(F_PK_CONFIG_TOML, 'w', encoding='utf-8') as f_obj:
                toml.dump(config, f_obj)

            print(f"set {key} = {new_value}")
        except Exception as e:
            print(f"set {key} = {new_value} {e}")

    try:
        current = get_pk_config_for_toggling(key)
        if current == -1:
            return
        new_value = 0 if current == 1 else 1
        set_pk_config_for_toggling(key, new_value)

    except Exception as e:
        print(f"[ERROR][toggle] {e}")
