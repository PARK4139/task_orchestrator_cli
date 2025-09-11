

def encode_via_task_orchestrator_cli(text_plain):
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    text_plain = text_plain.replace("8", "2")
    text_plain = text_plain.replace("7", "3")
    text_plain = text_plain.replace("6", "4")
    text_plain = text_plain.replace("4", "6")
    text_plain = text_plain.replace("3", "7")
    text_plain = text_plain.replace("2", "8")
    return text_plain
