import numpy as np
import scipy.signal as signal
import pandas as pd

def fft(x):
"""
Parameters
----------
x : array_like
    A complex data vector of length N

Returns
-------
array_like
    A complex vector of the same length as x containing the FFT coefficients

Notes
-----
This function implements the Cooley-Tukey algorithm, which is a divide-and-conquer method that recursively splits the data vector into even and odd parts and combines them using the twiddle factor. The algorithm requires that the length of the data vector is a power of two. If the length is odd, the function falls back to the discrete transform function.
"""
    N = len(x)
    if N <= 1: return x
    elif N % 2 == 1:         # N is odd, lemma does not apply
        print ('N is ' + str(N) + ', fall back to discrete transform')
        return discrete_transform(x)
    even = fft(x[0::2])
    odd =  fft(x[1::2])
    return np.array( [even[k] + np.exp(-2j*np.pi*k/N)*odd[k] for k in range(N//2)] + \
                     [even[k] - np.exp(-2j*np.pi*k/N)*odd[k] for k in range(N//2)] )

def discrete_transform(data):
"""
Parameters
----------
x : array_like
    A complex data vector of length N

Returns
-------
array_like
    A complex vector of the same length as x containing the FFT coefficients

Notes
-----
This function implements the Cooley-Tukey algorithm, which is a divide-and-conquer method that recursively splits the data vector into even and odd parts and combines them using the twiddle factor. The algorithm requires that the length of the data vector is a power of two. If the length is odd, the function falls back to the discrete transform function.
"""
    N = len(data)
    transform = np.zeros(N)
    for k in range(N):
        for j in range(N):
            angle = 2 * np.pi * k * j / N
            transform[k] += data[j] * np.exp(1j * angle)
    return transform

def find_peak_frequency(X):
"""
Parameters
----------
X : array_like
    A real or complex data vector representing a signal

Returns
-------
int
    The number of peaks in the frequency spectrum of the signal

Notes
-----
This function first computes the FFT of the signal using the fft function, then takes the absolute value of the first half of the FFT coefficients, which correspond to the positive frequencies. Then, it uses the scipy.signal.argrelextrema function to find the indices of the local maxima of the absolute FFT coefficients, which indicate the peaks in the frequency spectrum. The number of peaks is the length of the array of indices returned by the argrelextrema function.
"""
    Y = fft(X)
    # Get the length of the signal
    N = len(Y)
    # Divide by two to get the positive half of the FFT
    half = N // 2
    # Get the absolute value of the FFT
    abs_Y = np.abs(Y[:half])
    # Find the indices of the local maxima of the FFT
    peak_indices = signal.argrelextrema(abs_Y, np.greater)[0]
    # Count the number of peaks
    number_of_peaks = len(peak_indices)
    return number_of_peaks
