

def should_i_search_to_chatGPT():
    from pkg_py.functions_split.ensure_chat_gpt_responded import ensure_chat_gpt_responded
    from pkg_py.functions_split.should_i_do_cli import should_i_do_cli

    is_user_want_to_exit =  False
    while is_user_want_to_exit:
        # todo : chatGPT 4o with 임시 채팅
        txt_written = should_i_do_cli(
            title=rf"can i search contents dragged to chatGPT?",
            search_keyword_default="",
        )
        txt_written = txt_written.strip()
        if txt_written != "":
            ensure_chat_gpt_responded(txt_written)
