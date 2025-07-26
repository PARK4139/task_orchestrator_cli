def test_example_call_batchfile_as_new_window():
    batch_file_base = D_PROJECT
    batch_filename = rf"pk_push_project_to_github.bat"
    batch_calling_program = 'start "" call'
    batch_file = get_pnx_os_style(rf'{batch_file_base}/{batch_filename}')
    os.chdir(batch_file_base)
    ensure_command_excuted_to_os(cmd=f'{batch_calling_program} "{batch_file}"')


