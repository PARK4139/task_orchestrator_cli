"""
Common imports for frequently used functions across the pk_system.
This module provides centralized imports to reduce import statements in individual files.
"""

# Import modules directly to avoid name duplication
import pkg_py.functions_split.ensure_console_cleared
import pkg_py.functions_split.ensure_memo_contents_found
import pkg_py.functions_split.ensure_pk_system_exit_silent
import pkg_py.functions_split.ensure_seconds_measured
import pkg_py.functions_split.get_keyword_colors

# Create convenient aliases with clear naming
ensure_console_cleared = pkg_py.functions_split.ensure_console_cleared
ensure_memo_contents_found = pkg_py.functions_split.ensure_memo_contents_found.ensure_memo_contents_found
ensure_pk_system_exit_silent = pkg_py.functions_split.ensure_pk_system_exit_silent
ensure_printed = pkg_py.functions_split.ensure_printed
ensure_spoken = pkg_py.functions_split.ensure_spoken
ensure_spoken_hybrid = pkg_py.functions_split.ensure_spoken_hybrid
does_pnx_exist = pkg_py.functions_split.does_pnx_exist
get_pnx_os_style = pkg_py.functions_split.get_pnx_os_style
get_value_completed = pkg_py.functions_split.get_value_completed
get_time_as_ = pkg_py.functions_split.get_time_as_
ensure_seconds_measured = pkg_py.functions_split.ensure_seconds_measured
ensure_slept = pkg_py.functions_split.ensure_slept
ensure_pnx_made = pkg_py.functions_split.ensure_pnx_made
ensure_command_excuted_to_os = pkg_py.functions_split.ensure_command_excuted_to_os
get_os_n = pkg_py.functions_split.get_os_n
chcp_65001 = pkg_py.functions_split.chcp_65001
get_fzf_command = pkg_py.functions_split.get_fzf_command
highlight_multiple_keywords_fast = pkg_py.functions_split.get_keyword_colors.highlight_multiple_keywords_fast

# Export all functions for easy access
__all__ = [
    'ensure_console_cleared',
    'ensure_memo_contents_found',
    'ensure_pk_system_exit_silent',
    'ensure_printed',
    'ensure_spoken',
    'ensure_spoken_hybrid',
    'does_pnx_exist',
    'get_pnx_os_style',
    'get_value_completed',
    'get_time_as_',
    'ensure_seconds_measured',
    'ensure_slept',
    'ensure_pnx_made',
    'ensure_command_excuted_to_os',
    'get_os_n',
    'chcp_65001',
    'get_fzf_command',
    'highlight_multiple_keywords_fast'
]
