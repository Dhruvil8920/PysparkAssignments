import os
print(os.getcwd())
from ..src.assignment_1.util import *


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
