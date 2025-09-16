#c.	Generate a 5 Hz sine wave signal and shift it in time by 0.1 seconds. Plot the original and shifted signals on the same graph for comparison.
import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 500  # Sampling frequency (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # Time array for 1 second

# Frequency of sine wave
f = 5  # 5 Hz

# Generate original sine wave
sine_wave = np.sin(2 * np.pi * f * t)

# Time shift (in seconds)
shift = 0.1  
# Shifted signal = sin(2πf(t - shift))
shifted_wave = np.sin(2 * np.pi * f * (t - shift))

# Plot both signals
plt.figure(figsize=(10, 5))
plt.plot(t, sine_wave, label="Original 5 Hz Sine Wave")
plt.plot(t, shifted_wave, label="Shifted by 0.1 s", linestyle="--", color="red")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Original vs Time-Shifted 5 Hz Sine Wave")
plt.legend()
plt.grid(True)
plt.show()
