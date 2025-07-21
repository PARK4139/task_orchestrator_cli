from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def exec_vpc_doctor(vpc_issue_code):
    # todo 3 번 재시도 후, loop out,   pk_print(f'''solution_code를 3번 해결하려고 했으나  issue_code를 해결할 수 없었습니다. {'%%%FOO%%%' if LTA else ''}''')
    solution_code = None
    while 1:
        report_vpc_issue_discovered()
        if vpc_issue_code:
            solution_code = get_solution_code_from_map_issue_and_solution_code()
            if solution_code:
                solve_issue(solution_code)
                vpc_issue_code = get_vpc_issue_code(vpc_issue_code)
                if not vpc_issue_code:
                    pk_print(f'''issue_code is solved {'%%%FOO%%%' if LTA else ''}''', print_color='green')
                    remove_issue_code()
                    break
            elif not solution_code:
                pk_print(f'''solution_code is not found {'%%%FOO%%%' if LTA else ''}''', print_color='red')
            continue
    report_vpc_test_report(vpc_issue_code, solution_code)
