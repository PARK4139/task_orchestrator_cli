from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def print_txt_dragged_changed():
    # todo : chore : detect is changed dragged txt
    # previous_question = None
    # while 1:
    #     question = get_txt_dragged()
    #     question = question.strip()
    #     if question != previous_question:
    #         previous_question = question
    #         question_list = question.split("\n")
    #         question_list = get_list_striped_element(working_list=question_list, mode='rstrip')
    #         for question in question_list:
    #             pk_print(f'''[question_layer] {question}  {'%%%FOO%%%' if LTA else ''}''', print_color="blue")
    #     print()
    #     print()
    #     print()
    #     print()
    #     sleep(seconds=3)
    from pynput import mouse
    class DragTracker:
        def __init__(self):
            self.drag_ing_state = False
            self.is_dragging = False
            self.start_listener()
            pk_print(working_str="track drag state.")

        def start_listener(self):
            with mouse.Listener(
                    on_click=self.on_click,
                    on_move=self.on_move,
            ) as listener:
                listener.join()

        def on_click(self, x, y, button, pressed):
            if button == mouse.Button.left:
                if pressed:
                    self.is_dragging = True
                    # print(f"드래그 시작: ({x}, {y})")
                else:
                    if self.is_dragging:
                        if self.drag_ing_state == True:
                            # print(f"드래그 종료: ({x}, {y})")
                            question = get_txt_dragged()
                            previous_question = question
                            question_list = question.split("\n")
                            question_list = get_list_striped_element(working_list=question_list, mode='rstrip')
                            for question in question_list:
                                pk_print(f'''[dragged_text_layer] {question}  {'%%%FOO%%%' if LTA else ''}''',
                                         print_color="blue")
                            print()
                            print()
                            print()
                            print()
                            pass
                            self.drag_ing_state = False
                    self.is_dragging = False

        def on_move(self, x, y):
            if self.is_dragging:
                self.drag_ing_state = True
                pass

    DragTracker()
