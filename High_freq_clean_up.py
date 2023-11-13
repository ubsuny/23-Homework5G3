import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Define the butter_lowpass_filter function
def butter_lowpass_filter(data, cutoff_frequency, sample_rate, order=4):
  """Applies a low-pass filter to the given data using the scipy.signal.butter() and scipy.signal.filtfilt() functions.

  Args:
    data: A NumPy array containing the data to be filtered.
    cutoff_frequency: The cutoff frequency of the filter in Hz.
    sample_rate: The sample rate of the data in Hz.
    order: The order of the filter.

  Returns:
    A NumPy array containing the filtered data.
  """

  return filtfilt(*butter(order, cutoff_frequency / (sample_rate / 2), btype='low'), data)

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
plt.scatter(time, co2_concentration, label="Raw Data", s=5)  # 's' adjusts the size of the points
plt.title("Raw CO2 Concentration(PPM) vs. Frequency/6months")
plt.xlabel("Frequency/6 month")
plt.ylabel("CO2 Concentration(PPM)")
plt.legend()

plt.subplot(2, 1, 2)

plt.scatter(time, filtered_data, label="Filtered Data", s=5, color='red')  # 's' adjusts the size of the points
plt.title("Filtered CO2 Concentration(PPM) vs. Frequenccy/6months")
plt.xlabel("Frequency/6 month")
plt.ylabel("CO2 Concentration(PPM)")
plt.legend()

plt.tight_layout()
plt.show()
