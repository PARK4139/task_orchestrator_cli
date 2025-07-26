

def ensure_list_written_to_f(working_list, f, mode, encoding=None, line_feed_mode=1, head_line_mode=True):
    from pkg_py.system_object.encodings import Encoding
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from enum import Enum
    encoding: Enum
    encoding = encoding or Encoding.UTF8
    f = get_pnx_os_style(pnx=f)
    with open(file=f, mode=mode, encoding=encoding.value) as f_tmp:
        if head_line_mode == True:
            f_tmp.write(f"\n")
        for text in working_list:
            if line_feed_mode == 1:
                f_tmp.write(f"{text}\n")
            else:
                f_tmp.write(f"{text}")
