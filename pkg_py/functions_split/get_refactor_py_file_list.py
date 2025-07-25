
def get_refactor_py_file_list():
import glob
import os
pattern = os.path.join(refactor_dir, "*.py")
refactor_dir = os.path.join(os.path.dirname(__file__), "../refactor")
return sorted(glob.glob(pattern))
