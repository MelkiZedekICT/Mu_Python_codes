#d.	Generate a 10 Hz sine wave and scale its amplitude by a factor of 3. Plot the original and scaled signals together.
import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 500  # Sampling frequency (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # Time array for 1 second

# Frequency of sine wave
f = 10  # 10 Hz

# Original sine wave
sine_wave = np.sin(2 * np.pi * f * t)

# Scale amplitude by factor of 3
scaled_wave = 3 * sine_wave

# Plot both signals
plt.figure(figsize=(10, 5))
plt.plot(t, sine_wave, label="Original 10 Hz Sine Wave")
plt.plot(t, scaled_wave, label="Scaled (×3 Amplitude)", linestyle="--", color="red")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Original vs Scaled 10 Hz Sine Wave")
plt.legend()
plt.grid(True)
plt.show()
