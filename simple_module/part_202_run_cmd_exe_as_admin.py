def run_cmd_exe_as_admin():
    import inspect
    import sys
    import traceback
    func_n = inspect.currentframe().f_code.co_name
    try:
        while 1:
            # run.exe 관리자모드로 exec
            cmd_to_os_like_person_as_admin('PowerShell -cmd "Start-Process cmd -Verb RunAs"')

            # 네 클릭
            # f_png=rf"{PROJECT_D}\pkg_png\run cmd exe.png"
            # click_center_of_img_recognized_by_mouse_left(img_abspath=f_png)

            # 루프 종료
            break
    except:
        traceback.print_exc(file=sys.stdout)
