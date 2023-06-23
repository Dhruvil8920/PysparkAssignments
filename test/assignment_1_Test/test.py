import os
import sys

# Get the absolute path of the current script
script_path = os.path.abspath(__file__)

# Get the directory containing the script
script_directory = os.path.dirname(script_path)

# Get the absolute path of the 'src' directory
src_directory = os.path.join(script_directory, '..', 'src')

# Check if the 'src' directory exists
if os.path.isdir(src_directory):
    # Add the 'src' directory to the Python import path
    sys.path.append(src_directory)
else:
    print("Error: 'src' directory not found.")


from assignment_1.util import *


