

from pkg_py.system_object.directories import D_DOWNLOADS
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style

from pkg_py.functions_split.ensure_printed import ensure_printed


def parse_addup_from_issues_list_csv():  # todo

    issues_list_csv = rf"{D_DOWNLOADS}/Issues_list.csv"
    f_csv = issues_list_csv
    f_csv = get_pnx_unix_style(f_csv)

    ensure_pnx_opened_by_ext(f_csv)

    ensure_printed(str_working='line_order=', print_color='blue')
    line_order = input(":")
    issue_log_index_data = get_issue_log_index_data_from_f_csv(line_order=line_order, issues_list_csv=issues_list_csv)

    import ipdb
    ipdb.set_trace()

    # 노션 이슈발생 템플릿
    print_template_for_notion_issue_reporting(line_order=line_order, issues_list_csv=issues_list_csv)
