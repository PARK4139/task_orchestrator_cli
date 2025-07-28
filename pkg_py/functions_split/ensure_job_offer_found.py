def ensure_job_offer_found():
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.system_object.urls import URL_NAVER_MAIL, URL_GOOGLE_MAIL
    from pkg_py.system_object.urls import URL_ALBAMON, URL_JOBKOREA, URL_SARAMIN
    ensure_command_excuted_to_os(cmd=fr"explorer.exe {URL_SARAMIN}")
    ensure_command_excuted_to_os(cmd=fr"explorer.exe {URL_JOBKOREA}")
    ensure_command_excuted_to_os(cmd=fr"explorer.exe {URL_ALBAMON}")
    ensure_command_excuted_to_os(cmd=fr"explorer.exe {URL_NAVER_MAIL}")
    ensure_command_excuted_to_os(cmd=fr"explorer.exe {URL_GOOGLE_MAIL}")
