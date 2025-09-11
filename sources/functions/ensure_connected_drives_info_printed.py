from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_connected_drives_info_printed():
    # 
    from sources.objects.pk_map_texts import PkTexts
    try:
        # optional lazy logging initializer (one-time)
        from resources.logging.ensure_task_orchestrator_cli_log_initialized import ensure_task_orchestrator_cli_log_initialized
    except Exception:
        ensure_task_orchestrator_cli_log_initialized = None

    import os
    import psutil
    import logging
    import logging

    # Initialize logging once if no handlers exist
    if ensure_task_orchestrator_cli_log_initialized and not logging.getLogger().handlers:
        try:
            ensure_task_orchestrator_cli_log_initialized(__file__)
        except Exception:
            pass

    # Precompute tags
    TAG_STARTED = PkTexts.get_value_via_attr("STARTED")
    TAG_INFO = PkTexts.get_value_via_attr("INFO")
    TAG_FINISHED = PkTexts.get_value_via_attr("FINISHED")
    TAG_WARN = PkTexts.get_value_via_attr("WARNING")

    # Helpers
    def to_mib(n_bytes: int) -> float:
        return n_bytes / (1024 ** 2)

    header = (
        f"{'Drive':<8}"
        f"{'Type':<12}"
        f"{'File Count':<12}"
        f"{'Capacity (MiB)':<18}"
        f"{'Used (MiB)':<18}"
        f"{'Free (MiB)':<18}"
    )
    separator = "-" * len(header)

    logging.debug(f"{TAG_STARTED} Drive scan (excluding C:)")

    logging.debug(f"{header}")
    logging.debug(f"{separator}")

    partitions = psutil.disk_partitions(all=False)

    # Totals
    total_file_count = 0
    total_capacity_bytes = 0
    total_used_bytes = 0
    total_free_bytes = 0

    for part in partitions:
        drive_letter = part.device.rstrip("\\")  # e.g., 'D:'

        # Skip C:
        if drive_letter.upper().startswith("C:"):
            continue

        # Skip inaccessible or transient mountpoints
        try:
            usage = psutil.disk_usage(part.mountpoint)
        except PermissionError:
            logging.warning(f"{TAG_WARN} Permission denied: {part.mountpoint}")
            continue
        except FileNotFoundError:
            logging.warning(f"{TAG_WARN} Mountpoint not found: {part.mountpoint}")
            continue
        except OSError as e:
            logging.warning(f"{TAG_WARN} OS error on {part.mountpoint}: {e}")
            continue

        # Count files (can be slow on huge volumes)
        file_count = 0
        for root, dirs, files in os.walk(part.mountpoint):
            file_count += len(files)

        # Derive drive type
        if "removable" in part.opts:
            drive_type = "Removable"
        elif "cdrom" in part.opts:
            drive_type = "CD-ROM"
        elif "network" in part.opts or "nfs" in part.fstype.lower():
            drive_type = "Network"
        else:
            drive_type = "Fixed"

        # Use consistent byte-based math
        capacity_b = int(usage.total)
        free_b = int(usage.free)
        used_b = capacity_b - free_b  # avoid rounding inconsistencies

        logging.debug(f"{TAG_INFO} "
            f"{drive_letter:<8}{drive_type:<12}{file_count:<12}"
            f"{to_mib(capacity_b):<18.2f}"
            f"{to_mib(used_b):<18.2f}"
            f"{to_mib(free_b):<18.2f}"
        )

        # Accumulate totals
        total_file_count += file_count
        total_capacity_bytes += capacity_b
        total_used_bytes += used_b
        total_free_bytes += free_b

    logging.debug(f"{separator}")
    logging.debug(
        f"{TAG_INFO} "
        f"{'TOTAL':<8}{'—':<12}{total_file_count:<12}"
        f"{to_mib(total_capacity_bytes):<18.2f}"
        f"{to_mib(total_used_bytes):<18.2f}"
        f"{to_mib(total_free_bytes):<18.2f}"
    )
    logging.debug(f"{TAG_FINISHED} Drive scan completed")
