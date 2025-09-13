import logging

import pyautogui
import pygetwindow
import time
import sys

def ensure_applications_killed_like_person():
    """
    Closes all visible windows by simulating human-like key presses (Alt+F4, Left, Enter).
    Includes a 5-second countdown as a safety measure before starting.
    """
    import pyautogui
    import pygetwindow
    import time
    import sys


    logging.debug("WARNING: This script will attempt to close ALL open windows.")
    logging.debug("You have 5 seconds to cancel by pressing Ctrl+C.")
    
    try:
        for i in range(5, 0, -1):
            sys.stdout.write(f"Closing in {i} seconds... \r")
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        logging.debug("\nOperation cancelled by user.")
        return

    logging.debug("\nStarting to close all windows...")
    
    all_windows = pygetwindow.getAllWindows()
    
    for window in all_windows:
        try:
            if not window.title:
                continue
                
            if window.isMinimized:
                window.restore()
            
            window.activate()
            time.sleep(0.2)

            active_window = pygetwindow.getActiveWindow()
            if active_window and active_window._hWnd == window._hWnd:
                logging.debug(f"Attempting to close: {window.title}")
                pyautogui.hotkey('alt', 'f4')
                time.sleep(0.3)
                pyautogui.press('left')
                time.sleep(0.1)
                pyautogui.press('enter')
                time.sleep(0.5)
            else:
                logging.debug(f"Could not activate window: {window.title}. Skipping.")

        except pygetwindow.PyGetWindowException as e:
            logging.debug(f"Could not process window '{window.title}': {e}. It might have been closed already.")
        except Exception as e:
            logging.debug(f"An unexpected error occurred while processing window '{window.title}': {e}")

    logging.debug("All applications have been processed.")
