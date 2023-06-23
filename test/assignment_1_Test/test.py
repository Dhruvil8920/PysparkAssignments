import os
import sys

# Get the absolute path of the current script
script_path = os.path.abspath(__file__)

# Get the directory of the script
script_directory = os.path.dirname(script_path)

# Get the absolute path of the parent directory (containing both 'test' and 'src' directories)
parent_directory = os.path.dirname(script_directory)

# Add the parent directory to the Python import path
sys.path.insert(0, parent_directory)

from src.assignment_1.util import *


