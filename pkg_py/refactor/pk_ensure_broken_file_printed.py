from pkg_py.functions_split.pk_ensure_finally_routine_done import pk_ensure_finally_routine_done
from pkg_py.functions_split.pk_ensure_pnx_removed import pk_ensure_pnx_removed
from pkg_py.functions_split.pk_ensure_printed import pk_ensure_printed
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pnxs_from_d_working import get_pnxs_from_d_working
from pkg_py.functions_split.is_f import is_f
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED

if __name__ == "__main__":
    try:
        import traceback

        # from pkg_py.system_object.500_live_logic import copy, LTA, get_pnxs_from_d_working, is_f, get_nx, pk_ensure_pnx_removed
        # , STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
        #

        d_working = fr"C:\Users\WIN10PROPC3\Downloads\working directory for pkg_py pnx restoration via recuva"
        for pnx in get_pnxs_from_d_working(d_working, with_walking=0):
            if is_f(pnx):
                try:
                    with open(pnx, "rb") as f:
                        byte_data = f.read()

                    # 디코딩 시도 + 깨진 바이트 추적
                    decoded = []
                    errors = []
                    i = 0
                    while i < len(byte_data):
                        for j in range(1, 5):
                            try:
                                char = byte_data[i:i + j].decode("utf-8")
                                decoded.append(char)
                                i += j
                                break
                            except UnicodeDecodeError:
                                if j == 4:
                                    errors.append(byte_data[i])
                                    decoded.append(f"[\\x{byte_data[i]:02x}]")
                                    i += 1

                    content = "".join(decoded)

                except Exception as e:
                    print(f"❌ 파일 열기 실패: {e}")
                    exit(1)

                pk_ensure_printed(f'''_________________________________________________ {'%%%FOO%%%' if LTA else ''}''')
                pk_ensure_printed(f'''restored ({get_nx(pnx)}) {'%%%FOO%%%' if LTA else ''}''')
                # print(content)
                # signiture = 'pk_'
                # if signiture in content:
                for line in content.splitlines():
                    # if any(line.strip().startswith(k) for k in ("def ", "class ", "import", "from", "if __name__")):
                    #     print(line.strip())
                    print(line)
                user_input = input("o/x  pass/del : ")
                if user_input == 'o':
                    pass
                if user_input == 'x':
                    pk_ensure_pnx_removed(pnx)

    except:
        traceback_format_exc_list = traceback.format_exc().split("\n")
        pk_ensure_printed(str_working=f'{PK_UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            pk_ensure_printed(str_working=f'{STAMP_UNIT_TEST_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        pk_ensure_printed(str_working=f'{PK_UNDERLINE}', print_color='red')

    finally:
        pk_ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
