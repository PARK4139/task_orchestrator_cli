def get_text_coordinates_via_easy_ocr(string):  # 한글인식 잘 안되는 듯하다
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    # 화면 캡처
    screenshot = get_screenshot()

    # EsayOCR을 통해 모든텍스트 바운딩박스좌표 추출
    # coordinates_bounding_box=get_all_text_with_coordinates_via_easy_ocr(screenshot)
    # print_list_as_vertical(working_list=coordinates_bounding_box, items_name="coordinates_bounding_box")

    # EsayOCR을 통해 특정텍스트 바운딩박스좌표 추출
    coordinates_bounding_box = get_coordinates_bounding_box(image=screenshot, str_working=string)
    # print_list_as_vertical(working_list=coordinates_bounding_box, items_name="coordinates_bounding_box")

    # 중심 좌표 구하기
    if get_center_of_bounding_box(coordinates_bounding_box) is not None:
        center_x, center_y = get_center_of_bounding_box(coordinates_bounding_box)
        # pk_print(str_working=rf'''center_x="{center_x}"  {'%%%FOO%%%' if LTA else ''}''')
        # pk_print(str_working=rf'''center_y="{center_y}"  {'%%%FOO%%%' if LTA else ''}''')
        pk_print(f'''"text_coordinates=({center_x}, {center_y})"''')
        return center_x, center_y
    return None
