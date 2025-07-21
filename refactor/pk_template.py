# _________________________________________________________________________________________________________ python file meta info
#!/usr/bin/env python   # shebang
# -*- coding: utf-8 -*- # encoding declaration
# _________________________________________________________________________________________________________ author info
#🚀 __author__ = 'pk == junghoon.park'
# _________________________________________________________________________________________________________ dictionary structure
# TODO : work to do
# TBD : to be determined
# d : directory
# f : file
# n : name
# p : path
# x : extension
# pnx : path name extension
# nx  : name extension
# pn : path name
# mkr.. : marker to do
# mkr** : marker important
# pk_ : customized
# pk_option : optional literal or value
# _________________________________________________________________________________________________________ user input ( question ))
# decision = get_value_completed(key_hint=rf"{PkMessages2025.PREVIEW_MODE}=", values=[PkMessages2025.YES, PkMessages2025.NO])
# if decision == PkMessages2025.YES:
# _________________________________________________________________________________________________________ user input ( variable= )
# decision = get_value_completed(key_hint=rf"{PkMessages2025.PREVIEW_MODE}=", values=[PkMessages2025.PREVIEW, rf"{PkMessages2025.PREVIEW} X"])
# if decision == PkMessages2025.PREVIEW_MODE:
#     preview = False
# else:
#     preview = True
# _________________________________________________________________________________________________________  history option
# *based on history database
# key_name = "pk_program_language"
# pk_program_language = get_values_from_historical_database_routine(db_id = db.get_id(key_name,func_n), key_hint=f'{key_name}=', values_default=["kr", "en"])

# *based on database
# key_name = "is_initial_launch"
# is_initial_launch = db.get_values(db_id = db.get_id(key_name,func_n)) or True
# is_initial_launch = db.get_values(db_id = db.get_id(key_name,func_n)) or []
# is_initial_launch = db.get_values(db_id = db.get_id(key_name,func_n)) or 11

# based on history file
# key_name = "d_working"
# d_working = get_values_from_historical_file_routine(file_id=get_file_id(key_name,func_n), key_hint=f'{key_name}=', values_default=['pk_working'], editable=True)

# *based on file
# TBD

# _________________________________________________________________________________________________________  os
# ensure_os_shutdown(seconds=10)
# _________________________________________________________________________________________________________  info
# print(f"LOCAL LEPO : {GREEN}{os.getcwd()}{RESET}")
# _________________________________________________________________________________________________________  python program structure
# if __name__ == "__main__":
#     try:
#         pk_initialize_and_customize_logging_config()
#         pass
#     except Exception as exception:
#         ensure_do_exception_routine(traceback=traceback, exception=exception)
#     finally:
#         ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
# _________________________________________________________________________________________________________  log structure  (awesome)   : measure time/ performance
# pk_initialize_and_customize_logging_config(__file__)
# start_time = ensure_start_time_logged()
# end_time = ensure_end_time_logged()
# elapsed_time = ensure_elapsed_time_logged(start_time)
# logging.info("______")
# _________________________________________________________________________________________________________  stop debugger
# ensure_pk_system_exit_silent()  # pk_option
# _________________________________________________________________________________________________________  loop debugger
# miliseconds = [1000, 500, 250, 100, 50]
# pk_ensure_loop_delayed_at_loop_foot(loop_cnt, mode_level=2, miliseconds_limit=50)
# loop_cnt += 1
# _________________________________________________________________________________________________________
# f_working = get_pnx_from_fzf(pnx=d_working)
# _________________________________________________________________________________________________________
# f_working = get_value_completed(key_hint=rf"f_working=", values=get_pnxs_from_d_working(d_working=d_working))
