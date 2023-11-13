import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Define the butter_lowpass_filter function as provided earlier

# Load CO2 data using pandas
url = "https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_mlo_surface-flask_1_ccgg_month.txt"
df = pd.read_csv(url, delimiter="\s+", skiprows=54, names=['site', 'year', 'month', 'value'])

# Extract relevant columns
time = pd.to_datetime(df[['year', 'month']].assign(day=1))
co2_concentration = df['value']

# Define the cutoff frequency and order for the low-pass filter
cutoff_frequency = 0.07  # Adjust based on your data characteristics
order = 4  # Adjust based on the desired sharpness of the cutoff

# Apply the low-pass filter
filtered_data = butter_lowpass_filter(co2_concentration, cutoff_frequency, sample_rate=1, order=order)

# Plot both raw and filtered data as scatter plots
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.scatter(time, co2_concentration, label="Raw Data", s=5)  # 's' adjusts the size of the points
plt.title("Raw CO2 Concentration vs. Time")
plt.xlabel("Time")
plt.ylabel("CO2 Concentration")
plt.legend()

plt.subplot(2, 1, 2)
plt.scatter(time, filtered_data, label="Filtered Data", s=5)  # 's' adjusts the size of the points
plt.title("Filtered CO2 Concentration vs. Time")
plt.xlabel("Time")
plt.ylabel("CO2 Concentration")
plt.legend()

plt.tight_layout()
plt.show()
