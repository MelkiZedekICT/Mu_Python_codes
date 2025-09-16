#a.	Generate two sine wave signals with frequencies of 5 Hz and 10 Hz, both sampled at 1000 Hz for 1 second. Add the two signals together and plot the result.
import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 1000  # Sampling frequency (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # Time array for 1 second

# Frequencies of sine waves
f1 = 5   # 5 Hz
f2 = 10  # 10 Hz

# Generate sine waves
sine1 = np.sin(2 * np.pi * f1 * t)
sine2 = np.sin(2 * np.pi * f2 * t)

# Add the signals
combined_signal = sine1 + sine2

# Plot signals
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, sine1, label="5 Hz Sine Wave")
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 2)
plt.plot(t, sine2, label="10 Hz Sine Wave", color="orange")
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 3)
plt.plot(t, combined_signal, label="Combined (5 Hz + 10 Hz)", color="green")
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
