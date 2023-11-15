# task 1

import unittest
from freq_calc import fft  # Replace with your actual function

class TestFreqCalc(unittest.TestCase):

    def test_your_function_normal_case(self):
        # Test for normal input
        self.assertEqual(fft(), expected_output)

    def test_your_function_edge_case(self):
        # Test for edge cases
        pass

    def test_your_function_error_handling(self):
        # Test error handling
        self.assertRaises(ExpectedException, your_function, error_input)

if __name__ == '__main__':
    unittest.main()


# task 2