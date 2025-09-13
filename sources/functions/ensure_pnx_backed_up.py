def ensure_pnx_backed_up(pnx_working, d_dst, with_timestamp: bool = True, blacklist=None):
    import logging
    from functions import ensure_pnx_made
    import tempfile
    import shutil
    import traceback
    from pathlib import Path

    from functions.ensure_tree_copied_except_blacklist_and_including_whitelist import ensure_tree_copied_except_blacklist_and_including_whitelist
    from sources.functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose

    from sources.functions.ensure_spoken import ensure_spoken
    from sources.functions.ensure_value_completed import ensure_value_completed
    from sources.functions.ensure_disk_capacity_safe import ensure_disk_capacity_safe
    from sources.functions.ensure_trash_bin_emptied import ensure_trash_bin_emptied
    from sources.objects.pk_map_texts import PkTexts

    from sources.objects.pk_local_test_activate import LTA

    try:
        pnx_working = Path(pnx_working)
        d_dst = Path(d_dst)
        logging.debug(f"pnx_working: {pnx_working}, exists: {pnx_working.exists()}")
        logging.debug(f"Before is_dir/is_file check: pnx_working={pnx_working}, is_dir={pnx_working.is_dir()}, is_file={pnx_working.is_file()}")
        if not pnx_working.exists():
            question = f"백업 대상이 존재하지 않습니다"
            logging.warning(question)
            ensure_spoken(question)
            return None

        ensure_pnx_made(d_dst, mode='d')

        logging.debug(f"LTA is: {LTA}")
        if not LTA:
            ok, msg, stats = ensure_disk_capacity_safe(target_path=".", danger_used_percent=95.0)
            logging.debug(f"Disk capacity check result: ok={ok}, msg={msg}, stats={stats}")
            if not ok:
                question = "디스크 용량이 부족합니다. 휴지통을 비울까요?"
                ensure_spoken(question)
                ok = ensure_value_completed(key_hint=question, options=[PkTexts.YES, PkTexts.NO])
                logging.debug(f"User choice for trash bin: {ok}")
                if ok == PkTexts.YES:
                    logging.debug("휴지통 비우기 실행")
                    ensure_trash_bin_emptied()
                else:
                    logging.debug("휴지통 비우기 취소. 백업을 중단합니다.")
                    return None

        rar_result = None
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            thing_to_compress = None

            if pnx_working.is_dir():
                logging.debug(f"pnx_working is a directory. Copying to temp dir: {temp_path}")
                # The contents of pnx_working will be copied into this new directory
                target_copy_dir = temp_path / pnx_working.name
                target_copy_dir.mkdir()
                d_copied_tree = ensure_tree_copied_except_blacklist_and_including_whitelist(
                    d_working=pnx_working,
                    dst_dir=target_copy_dir,
                    blacklist=blacklist,
                    whitelist=[]
                )
                thing_to_compress = d_copied_tree
                logging.debug(f"After directory copy: d_copied_tree={d_copied_tree}")

            elif pnx_working.is_file():
                logging.debug(f"pnx_working is a file. Copying to temp dir: {temp_path}")
                # Create a directory inside temp to hold the file, preserving a parent folder structure
                target_copy_dir = temp_path / pnx_working.stem
                target_copy_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(pnx_working, target_copy_dir / pnx_working.name)
                thing_to_compress = target_copy_dir
                logging.debug(f"After file copy: target_copy_dir={target_copy_dir}")
            else:
                logging.debug(f"pnx_working is neither a file nor a directory: {pnx_working}")
                return None

            if thing_to_compress is None:
                logging.warning(f"thing_to_compress is None. Skipping further processing for {pnx_working}.")
                return None

            logging.debug(f"thing_to_compress: {thing_to_compress}, exists: {thing_to_compress.exists()}")

            import os
            is_thing_to_compress_empty = not (thing_to_compress.exists() and any(os.listdir(thing_to_compress)))
            logging.debug(f"is_thing_to_compress_empty: {is_thing_to_compress_empty}")

            if not is_thing_to_compress_empty:
                import datetime
                import tarfile

                base_name = pnx_working.name
                if with_timestamp:
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    archive_name_base = f"{base_name}_{timestamp}"
                else:
                    archive_name_base = base_name

                archive_filename = f"{archive_name_base}.tar.gz"
                archive_path = d_dst / archive_filename

                with tarfile.open(archive_path, "w:gz") as tar:
                    tar.add(str(thing_to_compress), arcname='.')

                rar_result = str(archive_path)
            else:
                message = f"백업할 내용이 없습니다. 소스 폴더가 비어있어 압축을 건너뜁니다."
                logging.warning(message)
                ensure_spoken(message)
                rar_result = None

        # The TemporaryDirectory context manager handles all cleanup of temp_dir
        logging.debug(f"Final rar_result: {rar_result}")
        return rar_result

    except:
        ensure_debug_loged_verbose(traceback)
    finally:
        ensure_spoken(wait=True)
