# _____________________________________________________________________ python file meta info
# !/usr/bin/env python   # shebang
# -*- coding: utf-8 -*- # encoding declaration
# _____________________________________________________________________ decision
# decision = get_value_completed(key_hint=rf"{PkMessages2025.PREVIEW_MODE}=", values=[PkMessages2025.YES, PkMessages2025.NO])
# if decision == PkMessages2025.YES:
#
# else:
#     preview = True
# _____________________________________________________________________ decision
# decision = get_value_completed(key_hint=rf"{PkMessages2025.PREVIEW_MODE}=", values=[PkMessages2025.PREVIEW, rf"{PkMessages2025.PREVIEW} X"])
# if decision == PkMessages2025.PREVIEW_MODE:
#     preview = False
# else:
#     preview = True
# _____________________________________________________________________ fzf
# key_name = 'file_to_hot_reload'
# values = get_pnxs(d_working=D_PKG_PY, with_walking=0, filter_option="f")
# file_to_hot_reload = get_value_from_fzf(key_name=key_name, values=values)
# file_to_hot_reload = get_pnx_os_style(file_to_hot_reload)
# ensure_printed(f'''file_to_hot_reload={file_to_hot_reload} {'%%%FOO%%%' if LTA else ''}''')
# _____________________________________________________________________  history file (new)
# key_name = 'f_working'
# func_n = inspect.currentframe().f_code.co_name
# file_id = get_file_id(key_name, func_n)
# editable = False
# # editable = True
# init_options = [
#     get_pnx_os_style(file)
#     for file in get_pnxs_from_d_working(D_PKG_PY, with_walking=True, only_files=True)
#     if ".venv" in file
#     if "__pycache__" in file
#     if file.endswith(".py")
# ]
# value = get_value_via_fzf_or_history_routine(key_name=key_name, file_id=file_id, init_options=init_options, editable=editable)
# f_working = value
# save_file = ensure_modules_saved_from_file(f_working=f_working,func_n=f_working)
# ensure_pnx_opened_by_ext(save_file)
# _____________________________________________________________________  history sqlite
# key_name = "pk_program_language"
# pk_program_language = get_values_from_historical_database_routine(db_id = db.get_id(key_name,func_n), key_hint=f'{key_name}=', options_default=["kr", "en"])
# _____________________________________________________________________  history sqlite
# key_name = "is_initial_launch"
# is_initial_launch = db.get_values(db_id = db.get_id(key_name,func_n)) or True
# is_initial_launch = db.get_values(db_id = db.get_id(key_name,func_n)) or []
# is_initial_launch = db.get_values(db_id = db.get_id(key_name,func_n)) or 11
# is_initial_launch = db.get_values(db_id = db.get_id(key_name,func_n)) or ""
# _____________________________________________________________________  history file
# key_name = "d_working"
# d_working = get_values_from_historical_file_routine(file_id=get_file_id(key_name,func_n), key_hint=f'{key_name}=', options_default=['pk_working'], editable=True)
# _____________________________________________________________________ options
# options = []
# d_working = get_value_completed(key_hint='d_working=', values=options)
# _____________________________________________________________________  os
# ensure_os_shutdown(seconds=10)
# _____________________________________________________________________  info
# print(f"LOCAL LEPO : {GREEN}{os.getcwd()}{RESET}")
# _____________________________________________________________________  log structure  (awesome)   : measure time/ performance
# initialize_and_customize_logging_config(__file__)

# start_time = ensure_start_time_logged()
# elapsed_time = ensure_elapsed_time_logged(start_time)
# logging.info(f'''[{PkMessages2025.DATA}] elapsed_time={elapsed_time} {'%%%FOO%%%' if LTA else ''}''')


# start_time = ensure_start_time_logged()
# end_time = ensure_end_time_logged()
# ipdb.set_trace()
# _____________________________________________________________________  loop debugger
# miliseconds = [1000, 500, 250, 100, 50]
# ensure_loop_delayed_at_loop_foot(loop_cnt, mode_level=2, miliseconds_limit=50)
# loop_cnt += 1
# _____________________________________________________________________
# f_working = get_pnx_from_fzf(pnx=d_working)
# _____________________________________________________________________
# f_working = get_value_completed(key_hint=rf"f_working=", values=get_pnxs_from_d_working(d_working=d_working))
# _____________________________________________________________________  debugger
# ipdb.set_trace()


