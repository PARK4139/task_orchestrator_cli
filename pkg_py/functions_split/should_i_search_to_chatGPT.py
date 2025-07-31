

def should_i_search_to_chatGPT():
    # todo : chatGPT 4o with 임시 채팅
    txt_written = should_i_do_cli(
        title=rf"can i search contents dragged to chatGPT?",
        search_keyword_default="",
    )
    txt_written = txt_written.strip()
    if txt_written != "":
        ensure_chat_gpt_responded(txt_written)
