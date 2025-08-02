def get_window_titles_matches(window_title: str):
    import win32gui

    from pkg_py.functions_split.ensure_process_killed_by_window_title import calculate_similarity

    matches = []

    def enum_handler(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title:
                similarity = calculate_similarity(window_title, title)
                if similarity >= 1.0:  # 유사도 임계값을 완전히 동일하게 설정 (0.9 → 1.0)
                    matches.append((hwnd, title, similarity))

    win32gui.EnumWindows(enum_handler, None)
    matches.sort(key=lambda x: x[2], reverse=True)
    return matches
