


from pkg_py.system_object.directories import D_DOWNLOADS
from pkg_py.system_object.directories import D_PKG_TXT

from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def assist_to_analize_addup_issue():  # todo

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    import inspect
    func_n = inspect.currentframe().f_code.co_name

    # 애드업 웹 로그인 및 검색
    # login_and_filter_and_export_addup(filter_vehicle_id_mode=True)

    # 파싱
    # parse_addup_from_issues_list_csv()

    def move_to_url(driver, url):
        expected_url = url
        while 1:
            current_url = driver.current_url
            pk_sleep(seconds=1)
            if current_url != expected_url:
                driver.get(url)
                print(f"URL 이동 성공 {url}")
            else:
                # 페이지 로딩 상태 확인
                try:
                    timeout = 10
                    WebDriverWait(driver, timeout).until(
                        lambda d: d.execute_script("return document.readyState;") == "complete")
                    return
                except:
                    import inspect
                    import traceback
                    func_n = inspect.currentframe().f_code.co_name
                    stamp_func_n = rf'''[{func_n}()]'''
                    pk_print(f'''{stamp_func_n} {traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''',
                             print_color='red')
                    pk_print(str_working="페이지 로딩에 실패", print_color='red')
                    return

    def write_user_input_by_tag_id(driver, tag_id, user_input):
        # dom 에서 확인
        wait = WebDriverWait(driver, 30)
        input_field = wait.until(
            EC.presence_of_element_located((By.ID, tag_id))  # 필드가 DOM에 존재하는지 확인
        )
        # 클릭 가능상태 확인
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, tag_id))  # 클릭 가능 상태인지 확인
        )
        input_field.send_keys(user_input)

    def click_btn_by_btn_tag_text(driver, btn_text):
        # dom 에서 확인
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, f"//button[text()='{btn_text}']")))
        button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[text()='{btn_text}']")))
        button.click()

    def click_btn_by_tag_id(driver, tag_id):
        # dom 에서 확인
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, tag_id)))
        # 클릭 가능상태 확인
        dropdown_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, tag_id)))
        # dropdown_button = wait.until(EC.presence_of_element_located((By.ID, "targetModules")))
        # dropdown_button = driver.find_element(By.XPATH, "//div[@id='targetModules']")
        dropdown_button.click()

    # 애드업 웹 로그인 및 이슈검색 및 issue ? .csv 다운로드
    token_ip_addup_web = get_token_from_f_token(f_token=rf'{D_PKG_TXT}\token_ip_addup_web.txt', initial_str="")
    token_id_addup_web = get_token_from_f_token(f_token=rf'{D_PKG_TXT}\token_id_addup_web.txt', initial_str="")
    token_pw_addup_web = get_token_from_f_token(f_token=rf'{D_PKG_TXT}\token_pw_addup_web.txt', initial_str="")
    browser_debug_mode = True
    driver = get_driver_selenium(browser_debug_mode=browser_debug_mode)
    issues_list_csv = rf"{D_DOWNLOADS}/Issues_list.csv"

    # move to addup 웹 로그인
    move_to_url(driver, url=rf"http://{token_ip_addup_web}/login")
    write_user_input_by_tag_id(driver=driver, tag_id="userId", user_input=token_id_addup_web)
    write_user_input_by_tag_id(driver=driver, tag_id="password", user_input=token_pw_addup_web)
    click_btn_by_btn_tag_text(driver=driver, btn_text='LOGIN NOW')

    # Google 비밀번호저장 창 닫기 : fail
    # sleep(seconds=5)
    # window_title_seg = "ADDup - Chrome"
    # while 1:
    #     if not is_front_window_title(window_title_seg=window_title_seg):
    #         move_window_to_front(window_title_seg=window_title_seg)
    #     if is_front_window_title(window_title_seg=window_title_seg):
    #         break
    # press("shift", "tab")
    # press("shift", "tab")
    # press("enter", debug_mode=False)

    # Google 비밀번호저장 창 닫기 : fail
    # alert = driver.switch_to.alert
    # alert.dismiss()  # "취소" 버튼 클릭

    # Google 비밀번호저장 창 닫기 : fail
    # cancel_button = driver.find_element(By.XPATH, "//button[contains(text(), '취소')]")
    # cancel_button.click()

    # Google 비밀번호저장 창 닫기 : fail : selenium은 네이티브 팝업 제어 미지원, GPT 4.o
    # chrome_options.add_experimental_option("prefs", {
    #     "credentials_enable_service": False,  # 비밀번호 저장 서비스 비활성화
    #     "profile.password_manager_enabled": False  # 비밀번호 저장 팝업 비활성화
    # })

    # download Issues_list.csv
    move_to_url(driver, url=rf"http://{token_ip_addup_web}/issue")
    click_btn_by_btn_tag_text(driver=driver, btn_text='Show Filter')  # click Show Filter
    click_btn_by_tag_id(driver=driver, tag_id="targetModules")  # click 문제 모듈
    click_tag_by_tag_xpath(driver=driver, tag_name='li', tag_property='text', tag_property_value='영상')  # click 영상
    remove_block_hidden(driver)
    click_btn_by_tag_id(driver=driver, tag_id="resolutionStatuses")  # click 해결 여부
    click_tag_by_tag_xpath(driver=driver, tag_name='li', tag_property='text', tag_property_value='미해결')  # click 미해결
    remove_block_hidden(driver)
    click_tag_by_tag_xpath(driver=driver, tag_name='button', tag_property='text',
                           tag_property_value='Search')  # click Search
    src_f = f'{D_DOWNLOADS}/Issues_list.csv'
    src_f = get_pnx_unix_style(src_f)
    if does_pnx_exist(pnx=src_f):
        # remove Issues_list.csv
        while 1:
            move_pnx_to_pk_recycle_bin(pnx=src_f)
            if not does_pnx_exist(pnx=src_f):
                break
    if not does_pnx_exist(pnx=src_f):
        while 1:
            # click Export
            if not does_pnx_exist(pnx=src_f):
                click_tag_by_tag_xpath(driver=driver, tag_name='button', tag_property='text',
                                       tag_property_value='Export')
            pk_sleep(milliseconds=500)
            if does_pnx_exist(pnx=src_f):
                break
    # todo : option : 필요 시 주석처리
    # driver.quit()

    ensure_pnx_opened_by_ext(issues_list_csv)

    pk_print(str_working='line_order=', print_color='blue')
    line_order = input(":")
    issue_log_index_data = get_issue_log_index_data_from_f_csv(line_order=line_order, issues_list_csv=issues_list_csv)

    # 노션 이슈발생 템플릿
    print_template_for_notion_issue_reporting(line_order=line_order, issues_list_csv=issues_list_csv)

    # download the issue log
    pk_print(str_working=rf'''Could I proceed to download the issue log?  {'%%%FOO%%%' if LTA else ''}''',
             print_color='blue')
    input(f"{pk_get_colorful_str_working_with_stamp_enviromnet(func_n=func_n)} >")

    if isinstance(issue_log_index_data["_f_ 위치"], float):
        issue_log_index_data["_f_ 위치"] = ""
        # print_and_open_original_log_position(vehicle_id='58_SEJONG_APOLLO_900_2', area_id='09_Sejong', course_id='05_BRT_Osong')
        steering_date = input("주행일자를 yymmdd 형태로 입력하세요:")
        steering_date = steering_date.strip()
        print_and_open_original_log_position(vehicle_id=issue_log_index_data["차량"], area_id=issue_log_index_data["지역"],
                                             course_id=issue_log_index_data["코스"], steering_date=steering_date)
        download_issue_log_f(issue_log_index_data=issue_log_index_data, original_log=True)
    else:
        download_issue_log_f(issue_log_index_data=issue_log_index_data)

    # download issue log
    try:
        quit_autoa2z_drive()
    except:
        import ipdb
        ipdb.set_trace()

    # run
    try:
        run_and_login_acu_update_v3_exe_and_run_autoa2zdrive_release_exe(issue_log_index_data=issue_log_index_data)
    except:
        import ipdb
        ipdb.set_trace()

    run_autoa2z_drive()
