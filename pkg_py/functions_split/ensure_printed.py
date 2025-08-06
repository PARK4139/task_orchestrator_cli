def ensure_printed(str_working, flush=True, print_color='', line_feed_mode=1, STAMP=None, mode_verbose=1, highlight_config_dict=None):
    import traceback
    
    try:
        from pkg_py.system_object.map_massages import PkMessages2025
        from pkg_py.functions_split import get_time_as_
        from pkg_py.functions_split.get_txt_highlighted import get_txt_highlighted
        from pkg_py.functions_split.print_green import print_green
        from pkg_py.functions_split.print_light_black import print_light_black
        from pkg_py.functions_split.print_light_blue import print_light_blue
        from pkg_py.functions_split.print_light_white import print_light_white
        from pkg_py.functions_split.print_magenta import print_magenta
        from pkg_py.functions_split.print_red import print_red
        from pkg_py.functions_split.print_yellow import print_yellow
        
        # Ensure PkMessages2025 is properly initialized
        try:
            # Try to get language and set it if not already set
            from pkg_py.functions_split.get_pk_program_language import get_pk_program_language
            lang = get_pk_program_language()
            PkMessages2025.set_lang(lang)
        except Exception:
            # Fallback to Korean if language detection fails
            PkMessages2025.set_lang("kr")
        
        STAMP_TIME = f"[ {get_time_as_('now')} ]"
        print_color = print_color.strip()
        
        # Safe message getter with fallback
        def get_safe_message(attr_name, fallback=None):
            try:
                value = getattr(PkMessages2025, attr_name, None)
                if value is None:
                    return fallback or f"[{attr_name}]"
                return value
            except Exception:
                return fallback or f"[{attr_name}]"
        
        default_stamp_by_color = {
            'red': rf"[{get_safe_message('ERROR', 'ERROR')}]",
            'yellow': rf"[{get_safe_message('TEST', 'TEST')}]",
            'blue': rf"[{get_safe_message('INFO', 'INFO')}]",
            'green': rf"[{get_safe_message('SUCCEEDED', 'SUCCESS')}]",
            'white': rf"[{get_safe_message('INTERACTIVE', 'INTERACTIVE')}]",
            'grey': rf"[{get_safe_message('WARNING', 'WARNING')}]",
            '': rf"[{get_safe_message('WARNING', 'WARNING')}]",
        }
        stamp_to_use = STAMP if STAMP is not None else default_stamp_by_color.get(print_color, f"[ {get_safe_message('WARNING', 'WARNING')} ]")

        if mode_verbose == 1:
            if print_color == 'white':
                print_light_white(f"{STAMP_TIME} {stamp_to_use} {str_working}", line_feed_mode, flush)
            elif print_color == 'magenta':
                print_magenta(f"{STAMP_TIME} {str_working}", line_feed_mode, flush)
            else:
                config = {
                    'red': {'red': [stamp_to_use, str_working], 'grey': [STAMP_TIME]},
                    'yellow': {'yellow': [stamp_to_use], 'white': [str_working], 'grey': [STAMP_TIME]},
                    'blue': {'blue': [stamp_to_use], 'white': [str_working], 'grey': [STAMP_TIME]},
                    'green': {'green': [stamp_to_use], 'white': [str_working], 'grey': [STAMP_TIME]},
                    'grey': {'grey': [STAMP_TIME, stamp_to_use, str_working]},
                    '': {'grey': [STAMP_TIME, stamp_to_use, str_working]},
                }.get(print_color, {'grey': [STAMP_TIME, stamp_to_use, str_working]})
                print(get_txt_highlighted(f"{STAMP_TIME} {stamp_to_use} {str_working}", config))

        elif mode_verbose == 0:
            {
                'grey': print_light_black,
                'red': print_red,
                'yellow': print_yellow,
                'blue': print_light_blue,
                'green': print_green,
                'white': print_light_white,
                'magenta': print_magenta,
                '': print_light_black,
            }.get(print_color, print_light_black)(str_working, line_feed_mode, flush)

    except Exception as e:
        # Fallback to simple print if ensure_printed fails
        try:
            print(f"[ENSURE_PRINTED_FALLBACK] {str_working}")
        except Exception:
            # Ultimate fallback - just print the string directly
            print(str_working)
