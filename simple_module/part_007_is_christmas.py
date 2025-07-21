

# import win32process
# import win32gui
# import pywin32
# import pywin32
# from project_database.test_project_database import MySqlUtil


def is_christmas():
    yyyy = get_time_as_('%Y')
    if is_month(mm=12) and is_day(dd=25):
        return 1
    else:
        return 0
