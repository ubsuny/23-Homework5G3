"""
This file uses the find_peaks_by_decade function to analyze the carbon dioxide data from the NOAA GML Carbon Cycle Cooperative Global Air Sampling Network[^2^][2].

The file imports the find_peaks_by_decade function from another file, and passes the url of the data file, the number of rows to skip, the delimiter, and the names of the columns as arguments. The function returns a Series containing the number of peaks in each decade. The file then prints the number of peaks in each decade.

Functions:
find_peaks_by_decade (url, skiprows, delimiter, names): Find the number of peaks in the carbon dioxide data by decade.

Variables:
output = (Series): The output of the find_peaks_by_decade function.
"""
import freq_generator as fg

# Air samples collected from Ascension Island, United Kingdom (ASC)
url = "https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_asc_surface-flask_1_ccgg_month.txt" 
skiprows = 53
delimiter = '\s+'
names = ['site',	'year',	'month', 'value']

# Calling freq_generator function
ouput = fg.find_peaks_by_decade(url, skiprows, delimiter, names)

# Print the number of peaks in each decade
for decade, peaks in ouput.items():
    print(f"There are {(len(peaks))//2} peaks in {int(decade)}s.")
