def get_list_differenced(list_a, list_b):
    set_b = set(list_b)
    return [item for item in list_a if item not in set_b]
