

from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def guide_to_use_pk_system_process(pk_system_process_pnx_list, nx_by_user_input):
    from pkg_py.system_object.local_test_activate import LTA
    # pk_#
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.ensure_printed import ensure_printed
    if LTA:
        ensure_printed(f'''{'%%%FOO%%%' if LTA else ''}''')
    for idx, pnx_working in enumerate(pk_system_process_pnx_list):

        if nx_by_user_input in pnx_working:
            if LTA:
                ensure_printed(f'''pnx_working={pnx_working} {'%%%FOO%%%' if LTA else ''}''')
            if nx_by_user_input in get_nx(pnx_working):

                if nx_by_user_input != get_nx(pnx_working):
                    print(rf'''{'[ TRY GUIDE ]'} pk {idx} ({get_nx(pnx_working)}) {'%%%FOO%%%' if LTA else ''}''')
            else:
                if LTA:
                    ensure_printed(f'''{'%%%FOO%%%' if LTA else ''}''')
                break
