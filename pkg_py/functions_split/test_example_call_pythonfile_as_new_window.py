
# not recommanded way
cmd_to_os(cmd=f'{python_calling_program} "{python_file}"')
def test_example_call_pythonfile_as_new_window():
os.chdir(python_file_base)
python_calling_program = 'start "" python'
python_file = get_pnx_os_style(rf'{python_file_base}/{python_filename}')
python_file_base = D_PROJECT
python_filename = rf"pk_push_project_to_github.py"
