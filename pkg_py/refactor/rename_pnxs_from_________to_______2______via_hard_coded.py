def rename_pnxs_from_________to_______2______via_hard_coded():
    import inspect

    func_n = inspect.currentframe().f_code.co_name

    # pnx=rf"D:\#기타\pkg_dirs"
    # pnx=rf"D:\#기타\pkg_files"
    pnx = rf"D:\#기타"
    pnx = rf"D:\#기타\pkg_files\pkg_mp4"

    txt_to_exclude_list = [
        F_DB_YAML,
        F_SUCCESS_LOG,
        F_LOCAL_PKG_CACHE,
    ]

    # d_list, f_list=get_sub_pnxs_without_walking(pnx=item_pnx, txt_to_exclude_list=txt_to_exclude_list)
    d_list, f_list = get_sub_pnx_list(pnx=pnx, txt_to_exclude_list=txt_to_exclude_list)

    # pnxs=d_list
    pnxs = f_list

    # todo : chore : pattern 변수 그 유사함수에서 참조해서 가져오기
    #
    # # pattern 대체 timestamp 를 붙이기
    # pnxs_and_pnxs_new=[]
    # for item in pnxs:
    #     pattern_new=''
    #     item_without_reg=re.sub(pattern, pattern_new, item[0]) # 날짜/시간 패턴을 모두 remove
    #     item_pn=get_pn(item_without_reg)
    #     item_x=get_x(item_without_reg)
    #     timestamp=get_time_as_("now")
    #     item_new=""
    #     if is_file(item[0]):
    #         item_new=f"{item_pn}_{timestamp}.{item_x}"
    #     else:
    #         item_new=f"{item_pn}_{timestamp}{item_x}"
    #     pnxs_and_pnxs_new.append([item[0], item_new])
    #
    # # 확인
    # print_list_as_vertical(working_list=pnxs_and_pnxs_new, items_name="바꿀 대상")
    # ensure_printed(str_working=rf'''len(pnxs_and_pnxs_new)="{len(pnxs_and_pnxs_new)}"  {'%%%FOO%%%' if LTA else ''}''')
    #
    # # 적용
    # rename_pnxs(pnxs=pnxs_and_pnxs_new)
