from pkg_py.functions_split.ensure_printed import ensure_printed


def driver_get_url_in_browser_and_wait_loaded(url, driver):
    import json

    driver_get_url_in_browser(url=url, driver=driver)

    # 네트워크 로그 가져오기
    logs = driver.get_log("performance")
    events = [json.loads(entry["message"])["message"] for entry in logs]

    # 가장 늦게 로드된 네트워크 요청 찾기
    latest_time = 0
    latest_url = None

    for event in events:
        if event["method"] == "Network.responseReceived":
            response_time = event["params"]["timestamp"]
            request_url = event["params"]["response"]["url"]

            if response_time > latest_time:
                latest_time = response_time
                latest_url = request_url

    ensure_printed(f"가장 늦게 로드된 요소 URL: {latest_url}")
    ensure_printed(f"로드 완료 시간: {latest_time}")
    return latest_url, latest_time
