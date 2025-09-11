def print_f_list_preview(file_list, num_preview=10):
    """수집될 파일 목록을 미리보기로 출력"""
    print(f"총 {len(file_list)}개 항목 중 앞{num_preview}개:")
    for path in file_list[:num_preview]:
        print(" pk_?? ", path)
    if len(file_list) > num_preview:
        print("...")
