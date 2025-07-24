

# import win32process
# import win32gui

from pkg_py.system_object.local_test_activate import LTA


def is_same_time(time1, time2):
    time2.strftime(rf'%Y-%m-%d %H:%M:%S')
    if LTA:
        print(rf'time1 : {time1} , time2 : {time2}')
    if time1 == time2:
        return 1
    else:
        return 0
