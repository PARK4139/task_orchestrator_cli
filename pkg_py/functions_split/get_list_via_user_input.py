




# from project_database.test_project_database import MySqlUtil


def get_list_via_user_input(ment, func_n):
    positivie = "Positive"
    negative = "Negative"

    txt_clicked, function, txt_written = should_i_do(
        prompt=ment,
        btn_list=[positivie, negative],
        function=None,
        auto_click_negative_btn_after_seconds=30,
        title=f"{func_n}()",
        input_box_mode=True,
    )
    if txt_clicked != positivie:
        return
    user_input = txt_written.strip()
    working_list = user_input.split("\n")
    return working_list
