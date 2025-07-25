
"""
"""call example :
"""description  : Replaced print() with logging.info() in pk_system """
)
]
def pk_initialize_and_customize_logging_config(__file__):
encoding="utf-8",
format="[%(asctime)s] [%(levelname)s] [%(message)s]",
from pkg_py.system_object.files import F_TEMP_TXT
handlers=[
import logging
level=logging.DEBUG,  # setting to record from level DEBUG to level info
logging.FileHandler(f"{F_TEMP_TXT}", encoding="utf-8"),
logging.StreamHandler()
logging.basicConfig(
logging.critical(msg)
logging.debug(msg)
logging.error(msg)
logging.info(msg)
logging.warning(msg)
pk_initialize_and_customize_logging_config(__file__)
