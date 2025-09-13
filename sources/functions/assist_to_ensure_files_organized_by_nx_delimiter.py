from sources.functions.get_list_sorted import get_list_sorted
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI
from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.ensure_value_completed import ensure_value_completed


def assist_to_ensure_files_organized_by_nx_delimiter():
    from colorama import init as pk_colorama_init

    ensure_task_orchestrator_cli_colorama_initialized_once()

    option_values = [D_PK_WORKING, D_TASK_ORCHESTRATOR_CLI, D_DOWNLOADS]
    while 1:
        d_working = ensure_value_completed(key_hint='d_working', options=option_values)
        option_values.append(d_working)
        option_values = get_list_deduplicated(working_list=option_values)
        word_set = get_word_set_from_f_list(d_working=d_working)
        word_list = get_list_from_set(working_set=word_set)
        word_list = get_list_unioned(list_a=word_list, list_b=['seg', 'SEG'])
        word_list = get_list_sorted(working_list=word_list)
        nx_delimiter = ensure_value_completed(key_hint='nx_delimiter', options=word_list)
        # for nx_delimiter in range(2000,2024):
        #     organize_f_list_by_nx_delimiter(nx_delimiter=str(nx_delimiter), d_working=d_working)
        pk_organize_f_list_by_nx_delimiter(nx_delimiter=nx_delimiter, d_working=d_working)
