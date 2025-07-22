

def get_list_sorted(working_list, mode_asc=1):
    if mode_asc == 1:
        return sorted(working_list)  # 오름차순 정렬
    elif mode_asc == 0:
        return sorted(working_list, reverse=True)  # 내림차순 정렬
    else:
        raise ValueError("Invalid order. Use 'asc' or 'desc'.")
