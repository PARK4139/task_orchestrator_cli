if __name__ == "__main__":
    from pk_system_sources.pk_system_functions.ensure_test_scenarios_executed import ensure_test_scenarios_executed
    import traceback
    from pk_system_sources.pk_system_functions.ensure_exception_routine_done import ensure_exception_routine_done
    from pk_system_sources.pk_system_functions.ensure_finally_routine_done import ensure_finally_routine_done

    from pk_system_sources.pk_system_objects.pk_system_directories import D_PK_SYSTEM
    from pk_system_sources.pk_system_functions.ensure_pk_system_starting_routine_done import ensure_pk_system_starting_routine_done

    ensure_pk_system_starting_routine_done(__file__=__file__, traceback=traceback)
    try:
        ensure_test_scenarios_executed()
    except Exception as exception:
        ensure_exception_routine_done(__file__=__file__, traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(__file__=__file__, D_PK_SYSTEM=D_PK_SYSTEM)
