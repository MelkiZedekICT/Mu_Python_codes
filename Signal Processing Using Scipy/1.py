#Generates a sine wave and a square wave with a frequency of 5 Hz and a sampling frequency of 500 Hz.

#Step-1---importing necessary libs
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


#Step-2---setting Parameters for the signal
fs = 500  # Sampling frequency
f = 5  # Frequency of the signal
t = np.linspace(0, 1, fs, endpoint=False)  # Time array


#Step-3---Create a sine wave signal
sine_wave = np.sin(2 * np.pi * f * t)


#Step-4---Create a square wave signal using scipy
square_wave = signal.square(2 * np.pi * f * t)


#Step-5---Plot the signals
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(t, sine_wave)
plt.title('Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.subplot(2, 1, 2)
plt.plot(t, square_wave)
plt.title('Square Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()
