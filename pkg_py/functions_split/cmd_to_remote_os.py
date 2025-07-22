

# import win32gui
# from project_database.test_project_database import MySqlUtil


def cmd_to_remote_os(cmd, **config_remote_os):
    return cmd_to_remote_os_with_pubkey(cmd=cmd, **config_remote_os)
