def is_office_pc_v2():
    from pkg_py.system_object.directories_reuseable import D_HOME

    if "user" in D_HOME:
        return True
    else:
        return False
