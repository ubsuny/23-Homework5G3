import freq_calc as fc
import pandas as pd
import numpy as np

# Air samples collected from Ascension Island, United Kingdom (ASC)
url = "https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_asc_surface-flask_1_ccgg_month.txt"
skiprows = 53
delimiter = '\s+'
names = ['site',	'year',	'month', 'value']

# Read the data from the url
df = pd.read_csv(url, skiprows=skiprows, delimiter=delimiter, names=names)
df['date'] = pd.to_datetime(df[['year','month']].assign(day=1)).dt.to_period('M')
df = df.set_index('date')
df['months'] = [x.n for x in (df.index-df.index[0])]


# Compute the FFT of the CO2 values
X = fc.fft(df['value'][-512:])

plt.plot(np.abs(X[:int(len(X)/2)])**2/int(len(X)/2))
plt.yscale("log")
plt.xlim(0,100)
# Find the peak frequency of the signal
peak_frequency = fc.find_peak_frequency(X)
# Print the peak frequency of the signal
print('The peak frequency is', peak_frequency, 'per year')
