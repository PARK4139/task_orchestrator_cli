def test_api():
    from objects.pk_local_test_activate import F_TASK_ORCHESTRATOR_CLI_CONFIG_TOML
    
    from sources.functions.ensure_command_executed import ensure_command_executed

    # def save_data_via_api_server():
    import requests
    import json

    import toml

    # SWAGGER ACCESS # FASTAPI # INCLUDE ROUTING TEST
    config = toml.load(F_TASK_ORCHESTRATOR_CLI_CONFIG_TOML)
    pk_protocol_type = config["pk_uvicorn"]["protocol_type"]
    pk_host = config["pk_uvicorn"]["host"]
    pk_port = config["pk_uvicorn"]["port"]
    ensure_command_executed(cmd=fr"explorer.exe {pk_protocol_type}://{pk_host}:{pk_port}/docs")
    ensure_command_executed(cmd=fr"explorer.exe {pk_protocol_type}://{pk_host}:{pk_port}/redoc")
    ensure_command_executed(cmd=fr"explorer.exe {pk_protocol_type}://{pk_host}:{pk_port}")

    # TODO : ROUTING TEST

    # POST REQUEST TEST
    url = "https://task_orchestrator_cli.store/api/db-maria/items"
    data = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "pw": "pw",
    }
    json_data = json.dumps(data)
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json_data)
    if response.status_code == 201:
        print("데이터가 성공적으로 저장되었습니다.")
    else:
        print("데이터 저장에 실패했습니다.")
