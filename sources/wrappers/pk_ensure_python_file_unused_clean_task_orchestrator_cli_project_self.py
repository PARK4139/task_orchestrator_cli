if __name__ == "__main__":
    import traceback

    from sources.functions.ensure_exception_routine_done import ensure_exception_routine_done
    from sources.functions.ensure_finally_routine_done import ensure_finally_routine_done
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI
    from sources.functions.ensure_task_orchestrator_cli_starting_routine_done import ensure_task_orchestrator_cli_starting_routine_done

    ensure_task_orchestrator_cli_starting_routine_done(__file__=__file__, traceback=traceback)
    try:

        import logging
        import traceback

        from functions.ensure_spoken import ensure_spoken, ensure_value_completed
        from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose
        from functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
        from functions.ensure_python_file_unused_clean import ensure_python_file_unused_clean
        from functions.get_easy_speakable_text import get_easy_speakable_text
        from objects.pk_map_texts import PkTexts
        from objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_WRAPPERS, D_TASK_ORCHESTRATOR_CLI
        from sources.functions.ensure_seconds_measured import ensure_seconds_measured


        @ensure_seconds_measured
        def _ensure_python_file_unused_clean_task_orchestrator_cli_project_self():
            # TODO  entrypoints 사용자 입력처리 필요.
            try:

                question = f'사용하지 않는 프로젝트 내의 파이썬 파일을 dry run 으로 출력할까요?'
                ensure_spoken(get_easy_speakable_text(question))
                ok = ensure_value_completed(key_hint=rf"{question}=", values=[PkTexts.YES, PkTexts.NO])
                if ok != PkTexts.YES:
                    ensure_task_orchestrator_cli_wrapper_suicided(__file__)

                ok = ensure_python_file_unused_clean(
                    project_root=D_TASK_ORCHESTRATOR_CLI,
                    entrypoints=[
                        D_TASK_ORCHESTRATOR_CLI_WRAPPERS / "pk_ensure_task_orchestrator_cli_enabled.py",
                        D_TASK_ORCHESTRATOR_CLI_WRAPPERS / "hello_world.py",
                    ],
                    execute=False,  # DRY-RUN
                    trash=True,  # if execute=True, try moving to trash
                    prune_empty_dirs_flag=True,  # remove empty dirs afterward
                    safe_filter=True,  # keep skipping venv/.git/tests/etc.
                    extra_keep=[  # whitelist
                        "scripts/*.py"
                        "*pyproject.py"
                    ],
                )
                logging.debug(rf"ok={ok}")

                question = f'정말로, 사용하지 않는 프로젝트 내의 파이썬 파일을 지울까요'
                ensure_spoken(get_easy_speakable_text(question))
                ok = ensure_value_completed(key_hint=rf"{question}=", values=[PkTexts.YES, PkTexts.NO])
                if ok != PkTexts.YES:
                    ensure_task_orchestrator_cli_wrapper_suicided(__file__)

                ok = ensure_python_file_unused_clean(
                    project_root=D_TASK_ORCHESTRATOR_CLI,
                    entrypoints=[
                        D_TASK_ORCHESTRATOR_CLI_WRAPPERS / "pk_ensure_task_orchestrator_cli_enabled.py",
                        D_TASK_ORCHESTRATOR_CLI_WRAPPERS / "hello_world.py",
                    ],
                    execute=False,
                    # execute=True,
                    trash=True,
                    prune_empty_dirs_flag=True,
                    safe_filter=True,
                    extra_keep=[
                        "scripts/*.py"
                        "*pyproject.py"
                    ],
                )
                logging.debug(rf"ok={ok}")

                return True
            except:
                ensure_debug_loged_verbose(traceback)
            finally:
                pass

        _ensure_python_file_unused_clean_task_orchestrator_cli_project_self()

    except Exception as exception:
        ensure_exception_routine_done(__file__=__file__,traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done( __file__=__file__,D_TASK_ORCHESTRATOR_CLI=D_TASK_ORCHESTRATOR_CLI)
