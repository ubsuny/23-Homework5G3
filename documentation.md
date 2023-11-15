#  Fast Fourier Transform

A fast Fourier transform (FFT) is an algorithm that computes the discrete Fourier transform (DFT) of a sequence, or its inverse (IDFT). Fourier analysis converts a signal from its original domain (often time or space) to a representation in the frequency domain and vice versa. [1]

## Station Chosen 
We choose Ascension Island, United Kingdom (ASC) [3]

https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_asc_surface-flask_1_ccgg_month.txt

## Library
we use `NumPy` `pandas`

## Calculates the actual frequency

```python
import freq_calc as fc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_co2_data(url, skiprows, delimiter, names):
    """
    Load CO2 concentration data from a given URL.

    Parameters:
    - url (str): The URL pointing to the CO2 concentration data file.
    - skiprows (int): The number of rows to skip from the beginning of the file.
    - delimiter (str): The delimiter used in the data file.
    - names (list): A list of column names for the DataFrame.

    Returns:
    - pd.DataFrame: A DataFrame containing the loaded data.
    """
    df = pd.read_csv(url, skiprows=skiprows, delimiter=delimiter, names=names)
    df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1)).dt.to_period('M')
    df = df.set_index('date')
    df['months'] = [x.n for x in (df.index - df.index[0])]
    return df

def plot_fft_spectrum(X):
    """
    Plot the FFT spectrum of the given data.

    Parameters:
    - X (array-like): The input data for FFT.

    Returns:
    - None
    """
    plt.plot(np.abs(X[:int(len(X) / 2)])**2 / int(len(X) / 2))
    plt.yscale("log")
    plt.xlim(0, 100)

def print_peak_frequency(X):
    """
    Print the peak frequency of the FFT signal.

    Parameters:
    - X (array-like): The input data for FFT.

    Returns:
    - None
    """
    peak_frequency = fc.find_peak_frequency(X)
    print('The peak frequency is', peak_frequency, 'per year')

```
<img alt="image" src="https://raw.githubusercontent.com/LinxuanHu/23-Homework5G3/main/fft_output.png">


## Clean up low frequency noise

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import butter, filtfilt

def butter_lowpass_filter(data, cutoff, sample_rate, order=4):
    """
    Apply a low-pass Butterworth filter to the input data.

    Parameters:
    - data (array-like): The input data to be filtered.
    - cutoff (float): The cutoff frequency of the filter.
    - sample_rate (float): The sample rate of the input data.
    - order (int, optional): The order of the filter. Defaults to 4.

    Returns:
    - array-like: The filtered data.
    """
    nyquist = 0.5 * sample_rate
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

```


## Fast Fourier Transform

<img alt="image" src="https://github.com/ubsuny/23-Homework5G3/blob/main/co2_concentration.png?raw=true">

## Linting

`main.py`

<img alt="image" src="https://raw.githubusercontent.com/LinxuanHu/23-Homework5G3/main/main_lint.png">

`low_freq_clean_up.py`

<img alt="image" src="https://raw.githubusercontent.com/LinxuanHu/23-Homework5G3/main/low_freq_clean_lint.png">

## Unit test



## References

[1] Wikipedia
https://en.wikipedia.org/wiki/Fast_Fourier_transform

[2] ChatGPT

[3] Global Monitoring Laboratory
Earth System Research Laboratories


