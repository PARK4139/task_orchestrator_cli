# _____________________________________________________________________ python file meta info
# !/usr/bin/env python   # shebang
# -*- coding: utf-8 -*- # encoding declaration
# _____________________________________________________________________ decision
# question = "휴지통을 비울까요?"
# ensure_spoken(question)
# decision = ensure_value_completed(key_hint=rf"{question}=", values=[PkTexts.YES, PkTexts.NO])
# if decision == PkTexts.YES:
#     logging.info("[INFO] 휴지통 비우기 실행")
#     ensure_trash_bin_emptied()
# else:
#     logging.info("[INFO] 휴지통 비우기 취소")
# _____________________________________________________________________ decision
# decision = ensure_value_completed(key_hint=rf"{PkTexts.PREVIEW_MODE}=", values=[PkTexts.PREVIEW, rf"{PkTexts.PREVIEW} X"])
# if decision == PkTexts.PREVIEW_MODE:
#     preview = False
# else:
#     preview = True
# _____________________________________________________________________ fzf
# key_name = 'file_to_hot_reload'
# values = get_pnxs(d_working=D_TASK_ORCHESTRATOR_CLI_RESOURCES, with_walking=0, filter_option="f")
# file_to_hot_reload = get_value_from_fzf(key_name=key_name, values=values)
# file_to_hot_reload = Path(file_to_hot_reload)
# logging.debug(f'''file_to_hot_reload={file_to_hot_reload} {'%%%FOO%%%' if LTA else ''}''')
# _____________________________________________________________________  history file (new)
# key_name = 'f_working'
# func_n = get_caller_n()
# file_id = get_file_id(key_name, func_n)
# editable = False
# # editable = True
# init_options = [
#     Path(file)
#     for file in get_pnxs_from_d_working(D_TASK_ORCHESTRATOR_CLI_RESOURCES, with_walking=True, only_files=True)
#     if ".venv" in file
#     if "__pycache__" in file
#     if file.endswith(".py")
# ]
# value = get_value_advanced_return_via_fzf_routine(key_name=key_name, file_id=file_id, init_options=init_options, editable=editable)
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
# d_working = ensure_value_completed(key_hint='d_working=', values=options)
# _____________________________________________________________________  os
# ensure_os_shutdown(seconds=10)
# _____________________________________________________________________  info
# print(f"LOCAL LEPO : {GREEN}{os.getcwd()}{RESET}")
# _____________________________________________________________________  log structure  (awesome)   : measure time/ performance
# ensure_task_orchestrator_cli_log_initialized(__file__)

# start_time = ensure_start_time_logged()
# elapsed_time = ensure_elapsed_time_logged(start_time)
# logging.info(f'''elapsed_time={elapsed_time} {'%%%FOO%%%' if LTA else ''}''')


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
# f_working = ensure_value_completed(key_hint=rf"f_working=", values=get_pnxs_from_d_working(d_working=d_working))
# _____________________________________________________________________  debugger
# ipdb.set_trace()
# _____________________________________________________________________ pk process
# ensure_py_system_processes_restarted([rf"{D_TASK_ORCHESTRATOR_CLI_RESOURCES}/pk_ensure_os_locked.py"])
# _____________________________________________________________________ pk processes