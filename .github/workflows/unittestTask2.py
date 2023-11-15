import unittest
import numpy as np
import low_freq_clean_up
from low_freq_clean_up import butter_lowpass_filter

class TestButterLowpassFilter(unittest.TestCase):

    def test_filter_with_valid_data(self):
        data = np.array([0, 1, 2, 3, 4, 5])
        cutoff = 2.0
        sample_rate = 10
        order = 4
        filtered_data = butter_lowpass_filter(data, cutoff, sample_rate, order)

    def test_filter_with_empty_data(self):
        data = np.array([])
        cutoff = 2.0
        sample_rate = 10
        order = 4
        with self.assertRaises(ValueError):
            butter_lowpass_filter(data, cutoff, sample_rate, order)

if __name__ == '__main__':
    unittest.main()
