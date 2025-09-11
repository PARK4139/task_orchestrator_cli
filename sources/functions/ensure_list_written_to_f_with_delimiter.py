def ensure_list_written_to_f_with_delimiter(working_list, f, mode, encoding=None):
    from sources.objects.encodings import Encoding
    from pathlib import Path
    from enum import Enum
    encoding: Enum
    encoding = encoding or Encoding.UTF8
    f = Path(f)
    
    # Define the delimiter
    delimiter = "\n%%PK_DELIMITER%%\n"

    with open(file=f, mode=mode, encoding=encoding.value) as f_tmp:
        # Join the list with the delimiter and write once. This is more efficient.
        content_to_write = delimiter.join(map(str, working_list))
        f_tmp.write(content_to_write)

