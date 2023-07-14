from PysparkAssignments.src.assignment_1.util import *
import unittest

path = "c"
class TestMyFunc(unittest.TestCase):

    if readCSV_to_DF(path) is None:
        print("hello")
        pass
    else:
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

    if trial(var)==0:
        pass

    else:
        def test_2(self):
            try:
                var_trial = trial(var)

            except AssertionError:
                print("test_1 fails")
                raise



if __name__ == '__main__':
    unittest.main()
