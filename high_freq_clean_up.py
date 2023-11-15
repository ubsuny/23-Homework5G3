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

# Load CO2 data using pandas
url = "https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_mlo_surface-flask_1_ccgg_month.txt"
df = pd.read_csv(url, delimiter="\s+", skiprows=54, names=['site', 'year', 'month', 'value'])

# Extract relevant columns
time = pd.to_datetime(df[['year', 'month']].assign(day=1))
co2_concentration = df['value']

# Define the cutoff frequency and order for the low-pass filter
cutoff_frequency = 0.065  # Adjust based on your data characteristics
order = 4  # Adjust based on the desired sharpness of the cutoff

# Apply the low-pass filter
filtered_data = butter_lowpass_filter(co2_concentration, cutoff_frequency, sample_rate=1, order=order)

# Plot both raw and filtered data as scatter plots
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.scatter(time, co2_concentration, label="Raw Data", s=5, color='blue')  # Change the line color to blue
plt.title("Raw CO2 Concentration (PPM) vs. Frequency (6 months)")
plt.xlabel("Frequency (6 months)")
plt.ylabel("CO2 Concentration (PPM)")
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.scatter(time, filtered_data, label="Filtered Data", s=5, color='red')  # Change the line color to red
plt.title("Filtered CO2 Concentration (PPM) vs. Frequency (6 months)")
plt.xlabel("Frequency (6 months)")
plt.ylabel("CO2 Concentration (PPM)")
plt.grid(True)
plt.legend()

plt.tight_layout()

# Save the plot as a PNG image named `co2_concentration.png`
plt.savefig('co2_concentration.png')
