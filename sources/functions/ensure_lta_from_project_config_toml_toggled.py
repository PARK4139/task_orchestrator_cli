


def ensure_lta_from_project_config_toml_toggled():
    from sources.objects.pk_local_test_activate import F_TASK_ORCHESTRATOR_CLI_CONFIG_TOML
    try:
        config_file = F_TASK_ORCHESTRATOR_CLI_CONFIG_TOML

        with open(config_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        found = False
        for i, line in enumerate(lines):
            if line.startswith("LOCAL_TEST_ACTIVATE"):
                found = True
                current_value = int(line.split('=')[1].strip())
                new_value = 0 if current_value == 1 else 1
                lines[i] = f"LOCAL_TEST_ACTIVATE = {new_value}\n"
                print(f"LOCAL_TEST_ACTIVATE is now set to {new_value}.")
                break

        if not found:
            print("Error: 'LOCAL_TEST_ACTIVATE' not found in config file.")
            return

        with open(config_file, 'w', encoding='utf-8') as file:
            file.writelines(lines)

        print(f"LTA value successfully toggled and saved to {config_file}.")

    except Exception as e:
        print(f"Error: {e}")
