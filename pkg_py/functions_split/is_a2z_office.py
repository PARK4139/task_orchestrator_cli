def is_a2z_office():
    from pkg_py.system_object.directories_reuseable import D_HOME

    if "user" in D_HOME:
        return True
    else:
        return False
