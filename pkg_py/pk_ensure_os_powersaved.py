# from pkg_py.system_object.500_live_logic import save_power_as_s4, ensure_spoken, save_screen

save_screen()

ensure_spoken('최대 절전 모드 진입', after_delay=0.55)
save_power_as_s4()
# make_os_power_saving_mode_as_s3()
