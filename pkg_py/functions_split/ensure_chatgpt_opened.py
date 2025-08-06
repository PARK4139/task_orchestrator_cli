from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_chatgpt_opened():
    from pkg_py.system_object.urls import URL_CHATGPT_PK_WORKING
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    ensure_command_excuted_to_os(cmd=fr"explorer.exe {URL_CHATGPT_PK_WORKING}")
