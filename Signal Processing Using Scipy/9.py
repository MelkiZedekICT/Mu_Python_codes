#e.	Generate a 5 Hz sine wave and reverse it in time. Plot the original and reversed signals on the same graph. 
import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 500  # Sampling frequency (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # Time array for 1 second

# Frequency
f = 5  # 5 Hz

# Generate original sine wave
sine_wave = np.sin(2 * np.pi * f * t)

# Reverse in time (flip the signal)
reversed_wave = sine_wave[::-1]  

# Plot both signals
plt.figure(figsize=(10, 5))
plt.plot(t, sine_wave, label="Original 5 Hz Sine Wave")
plt.plot(t, reversed_wave, label="Time-Reversed Sine Wave", linestyle="--", color="red")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Original vs Time-Reversed 5 Hz Sine Wave")
plt.legend()
plt.grid(True)
plt.show()
