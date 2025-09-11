def test_example_call_batchfile_as_new_window():
    batch_file_base = D_TASK_ORCHESTRATOR_CLI
    batch_filename = rf"pk_push_project_to_github.bat"
    batch_calling_program = 'start "" call'
    batch_file = Path(rf'{batch_file_base}/{batch_filename}')
    os.chdir(batch_file_base)
    ensure_command_executed(cmd=f'{batch_calling_program} "{batch_file}"')


