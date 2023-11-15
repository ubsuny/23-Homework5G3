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

# Air samples collected from Ascension Island, United Kingdom (ASC)
url = "https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_asc_surface-flask_1_ccgg_month.txt"
skiprows = 53
delimiter = '\s+'
names = ['site', 'year', 'month', 'value']

# Read the data from the url
df = load_co2_data(url, skiprows, delimiter, names)

# Compute the FFT of the CO2 values
X = fc.fft(df['value'][-512:])

# Plot the FFT spectrum
plot_fft_spectrum(X)

# Print the peak frequency of the signal
print_peak_frequency(X)

# Show the plot
plt.show()
