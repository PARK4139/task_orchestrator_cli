


def click_tag_as_with_tag_text(driver, tag_name, tag_text):
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.local_test_activate import LTA
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    try:
        h3_element = driver.find_element(By.XPATH, rf"//{tag_name}[text()='{tag_text}']")
        actions = ActionChains(driver)
        actions.move_to_element(h3_element).click().perform()
    except Exception as e:
        ensure_printed(f'''click {tag_name} tag with text as {tag_text} fail  {'%%%FOO%%%' if LTA else ''}''',
                       print_color='red')
