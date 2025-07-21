

from pkg_py.pk_system_layer_directories import D_DOWNLOADS
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style

from pkg_py.simple_module.part_014_pk_print import pk_print


def parse_addup_from_issues_list_csv():  # todo

    issues_list_csv = rf"{D_DOWNLOADS}/Issues_list.csv"
    f_csv = issues_list_csv
    f_csv = get_pnx_unix_style(f_csv)

    open_pnx_by_ext(f_csv)

    pk_print(working_str='line_order=', print_color='blue')
    line_order = input(":")
    issue_log_index_data = get_issue_log_index_data_from_f_csv(line_order=line_order, issues_list_csv=issues_list_csv)

    import ipdb
    ipdb.set_trace()

    # 노션 이슈발생 템플릿
    print_template_for_notion_issue_reporting(line_order=line_order, issues_list_csv=issues_list_csv)
