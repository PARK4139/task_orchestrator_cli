if __name__ == '__main__':
    from pkg_py.functions_split.pk_ensure_functions_splited import pk_ensure_functions_splited
    from pkg_py.functions_split.pk_initialize_and_customize_logging_config import pk_initialize_and_customize_logging_config

    pk_initialize_and_customize_logging_config(__file__)
    pk_ensure_functions_splited()
