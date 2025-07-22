

from pkg_py.functions_split.pk_measure_seconds import pk_measure_seconds


@pk_measure_seconds
def guide_to_use_pk_system_process(pk_system_process_pnx_list, nx_by_user_input):
    from pkg_py.pk_system_object.Local_test_activate import LTA
    from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.pk_print import pk_print
    if LTA:
        pk_print(f'''{'%%%FOO%%%' if LTA else ''}''')
    for idx, pnx_working in enumerate(pk_system_process_pnx_list):

        if nx_by_user_input in pnx_working:
            if LTA:
                pk_print(f'''pnx_working={pnx_working} {'%%%FOO%%%' if LTA else ''}''')
            if nx_by_user_input in get_nx(pnx_working):

                if nx_by_user_input != get_nx(pnx_working):
                    print(rf'''{STAMP_TRY_GUIDE} pk {idx} ({get_nx(pnx_working)}) {'%%%FOO%%%' if LTA else ''}''')
            else:
                if LTA:
                    pk_print(f'''{'%%%FOO%%%' if LTA else ''}''')
                break
