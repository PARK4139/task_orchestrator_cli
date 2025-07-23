from pkg_py.pk_system_object.map_massages import PkMessages2025


def move_pnx_v2(pnx, d_dst, with_overwrite=0, sequential_mode=0, timestamp_mode=0):
    import os
    import shutil
    import traceback
    from datetime import datetime
    from pkg_py.functions_split.get_n import get_n
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_x import get_x
    from pkg_py.functions_split.is_d import is_d
    from pkg_py.functions_split.is_f import is_f
    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.pk_system_object.local_test_activate import LTA

    def generate_sequential_pnx(dst_base_path, base_name, ext):
        for i in range(1, 1000):
            candidate = os.path.join(dst_base_path, f"({i})_{base_name}{ext}")
            if not os.path.exists(candidate):
                return candidate
        raise RuntimeError("Too many duplicates to resolve with sequential mode.")

    def generate_timestamped_pnx(dst_base_path, base_name, ext):
        ts_prefix = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
        candidate = os.path.join(dst_base_path, f"{ts_prefix}_{base_name}{ext}")
        return candidate

    try:
        sequential_mode = int(sequential_mode)
        timestamp_mode = int(timestamp_mode)

        if with_overwrite == 0:
            pnx_p = os.path.dirname(pnx)
            pnx_n = get_n(pnx)
            pnx_x = get_x(pnx)
            dst_base = d_dst

            src_type = 'f' if is_f(pnx) else 'd' if is_d(pnx) else 'unknown'
            dst_pnx = os.path.join(dst_base, get_nx(pnx))

            if os.path.exists(dst_pnx):
                base_name, ext = os.path.splitext(get_nx(pnx))
                if timestamp_mode == 1:
                    dst_pnx = generate_timestamped_pnx(dst_base, base_name, ext)
                elif sequential_mode == 1:
                    dst_pnx = generate_sequential_pnx(dst_base, base_name, ext)
                else:
                    pk_print(f"[{PkMessages2025.ALREADY_EXIST}] '{dst_pnx}'", print_color='red')
                    return

            if not os.path.exists(d_dst):
                os.makedirs(d_dst)

            shutil.move(pnx, dst_pnx)

            if LTA:
                pk_print(f"src_type={src_type} dst_pnx={dst_pnx:<150} dst={d_dst:<50}  {'%%%FOO%%%' if LTA else ''}",
                         print_color='green')
            else:
                pk_print(f"[MOVE] '{pnx}' → '{dst_pnx}'", print_color='green')

        elif with_overwrite == 1:
            if not is_f(pnx):
                pk_print(f"[ERROR] Source file does not exist: {pnx}", print_color='red')
                return

            d_dst = os.path.dirname(d_dst)
            if d_dst and not os.path.exists(d_dst):
                os.makedirs(d_dst)
            try:
                if os.path.exists(d_dst):
                    os.remove(d_dst)
                shutil.move(pnx, d_dst)
                pk_print(f"[OVERWRITE MOVE] '{pnx}' → '{d_dst}'", print_color='green')
            except Exception as e:
                pk_print(f"[ERROR] Failed to move file: {e}", print_color='red')

    except Exception:
        pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
