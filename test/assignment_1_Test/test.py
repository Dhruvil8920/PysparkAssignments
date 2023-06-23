import os
import sys

# Get the absolute path of the current script
script_path = os.path.abspath(__file__)

# Get the directory of the script
script_directory = os.path.dirname(script_path)

# Set the current working directory to the script's directory
os.chdir(script_directory)

# Add the current directory to the Python import path
sys.path.append(script_directory)

# Add the 'src' directory to the Python import path
sys.path.append(os.path.join(script_directory, 'src'))

# Now you can import modules or perform operations in the new working directory
from assignment_1.util import *
import unittest



data1 = [("1",), ("2",), ("3",)]
schema1 = ["no"]
expdf1 = spark.createDataFrame(data1, schema1)
var = ""
class TestMyFunc(unittest.TestCase):

    def test_1(self):
        try:
            result_df = createDF(data1, schema1)
            result_str = result_df.show(truncate=False)
            expected_str = expdf1.show(truncate=False)
            self.assertEqual(result_str, expected_str)
            print("test_1 passes")

        except AssertionError:
            print("test_1 fails")
            raise

    def test_2(self):
        try:
            var_trial = trial(var)
            pass

        except AssertionError:
            print("test_1 fails")
            raise

if __name__ == '__main__':
    unittest.main()
