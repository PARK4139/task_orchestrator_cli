
def ensure_potplayer_killed():
	import time
	from pkg_py.functions_split.ensure_process_killed_by_window_title import ensure_process_killed_by_window_title
	from pkg_py.functions_split.get_window_titles import get_window_titles
	for window_title in get_window_titles():
		if " - 팟플레이어" in window_title:
			ensure_process_killed_by_window_title(window_title)
			break

