import os
import sys

# Get the absolute path of the current script
script_path = os.path.abspath(__file__)

# Get the directory of the script
script_directory = os.path.dirname(script_path)

# Get the absolute path of the 'util' module
util_module_path = os.path.join(script_directory, '..', 'src', 'assignment_1', 'util.py')

# Add the directory containing the 'util' module to the Python import path
util_module_directory = os.path.dirname(util_module_path)
sys.path.append(util_module_directory)

# Now you can import the 'util' module
from util import *

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
