def ensure_guided_not_prepared_yet():
	from pkg_py.functions_split.is_internet_connected import is_internet_connected
	from pkg_py.functions_split import ensure_printed, ensure_spoken
	from pkg_py.system_object.local_test_activate import LTA
	from pkg_py.system_object.map_massages import PkMessages2025
	ensure_printed(f'''{PkMessages2025.NOT_PREPARED_YET}{'%%%FOO%%%' if LTA else ''}''', print_color='magenta', mode_verbose=0)
	if is_internet_connected():
		ensure_spoken(f'''{PkMessages2025.NOT_PREPARED_YET}{'%%%FOO%%%' if LTA else ''}''')