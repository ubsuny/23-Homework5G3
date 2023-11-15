import unittest
import freq_calc
from unittest.mock import patch
from main import load_co2_data 

class TestLoadCO2Data(unittest.TestCase):

    @patch('your_script.pd.read_csv')
    def test_load_co2_data_normal(self, mock_read_csv):
        url = "https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_asc_surface-flask_1_ccgg_month.txt"
        skiprows = 5
        delimiter = ','
        names = ['Date', 'CO2']
        load_co2_data(url, skiprows, delimiter, names)
        mock_read_csv.assert_called_with(url, skiprows=skiprows, delimiter=delimiter, names=names)

    def test_load_co2_data_invalid_url(self):
        pass

if __name__ == '__main__':
    unittest.main()
