from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.system_object.urls import URL_NAVER_MAIL, URL_GOOGLE_MAIL


def ensure_mail_found():
    ensure_command_excuted_to_os(cmd=fr"explorer.exe {URL_NAVER_MAIL}")
    ensure_command_excuted_to_os(cmd=fr"explorer.exe {URL_GOOGLE_MAIL}")
