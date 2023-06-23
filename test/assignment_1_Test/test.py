import os
import sys

# Get the absolute path of the current script
script_path = os.path.abspath(__file__)

# Get the directory containing the script
script_directory = os.path.dirname(script_path)

# Get the absolute path of the 'src' directory
src_directory = os.path.join(script_directory, '..', 'src')

# Add the 'src' directory to the Python import path
sys.path.insert(0, src_directory)

import assignment_1.util


