import glob
import os


def get_refactor_py_file_list():
    refactor_dir = os.path.join(os.path.dirname(__file__), "../refactor")
    pattern = os.path.join(refactor_dir, "*.py")
    return sorted(glob.glob(pattern))
