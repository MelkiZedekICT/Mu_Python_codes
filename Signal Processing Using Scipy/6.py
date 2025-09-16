#b.	Generate a 5 Hz sine wave and a 10 Hz cosine wave, both sampled at 500 Hz for 2 seconds. Multiply the two signals element-wise and plot the resulting signal.
import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 500  # Sampling frequency (Hz)
t = np.linspace(0, 2, 2 * fs, endpoint=False)  # Time array for 2 seconds

# Frequencies
f1 = 5   # 5 Hz sine
f2 = 10  # 10 Hz cosine

# Generate signals
sine_wave = np.sin(2 * np.pi * f1 * t)
cosine_wave = np.cos(2 * np.pi * f2 * t)

# Element-wise multiplication
product_signal = sine_wave * cosine_wave

# Plot signals
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, sine_wave, label="5 Hz Sine Wave")
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 2)
plt.plot(t, cosine_wave, label="10 Hz Cosine Wave", color="orange")
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 3)
plt.plot(t, product_signal, label="Product Signal (Sine * Cosine)", color="green")
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
