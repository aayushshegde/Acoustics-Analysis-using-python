import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# --- 1. Define Signal Parameters (Same as before) ---
sampling_rate = 44100
duration = 1.0
frequency = 1000
amplitude = 0.5
noise_amplitude = 0.1

# --- 2. Generate Time and Signals (Same as before) ---
t = np.linspace(0., duration, int(sampling_rate * duration), endpoint=False)
clean_signal = amplitude * np.sin(2 * np.pi * frequency * t)
noise = noise_amplitude * np.random.randn(len(t))
noisy_signal = clean_signal + noise

# --- 3. Design and Apply a Low-Pass Filter (Same as before) ---
cutoff_frequency = 1500.0
filter_order = 4
nyquist = 0.5 * sampling_rate
normal_cutoff = cutoff_frequency / nyquist
b, a = butter(filter_order, normal_cutoff, btype='low', analog=False)
filtered_signal = lfilter(b, a, noisy_signal)

# --- 4. NEW: Perform Frequency Analysis (FFT) ---
N = int(sampling_rate * duration) # Number of sample points

# Calculate FFT for the noisy signal
noisy_fft = np.fft.fft(noisy_signal)
noisy_fft_magnitude = np.abs(noisy_fft)

# Calculate FFT for the filtered signal
filtered_fft = np.fft.fft(filtered_signal)
filtered_fft_magnitude = np.abs(filtered_fft)

# Create the frequency axis for plotting
frequencies = np.fft.fftfreq(N, 1/sampling_rate)

# We only need to plot the positive frequencies
positive_freq_indices = np.where(frequencies >= 0)
frequencies = frequencies[positive_freq_indices]
noisy_fft_magnitude = noisy_fft_magnitude[positive_freq_indices]
filtered_fft_magnitude = filtered_fft_magnitude[positive_freq_indices]


# --- 5. Plot Both the Time and Frequency Domains ---

# First plot: Time Domain Comparison (same as before)
plt.figure(figsize=(12, 10)) # Make the figure taller to fit both plots
plt.subplot(2, 1, 1) # Create a subplot grid of 2 rows, 1 column, and select the 1st plot
plt.plot(t, noisy_signal, 'b-', label='Noisy Signal', alpha=0.5)
plt.plot(t, filtered_signal, 'r-', linewidth=2, label='Filtered Signal')
plt.xlim(0, 0.01)
plt.title("Time Domain: Comparison of Signals")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# Second plot: Frequency Domain Comparison
plt.subplot(2, 1, 2) # Select the 2nd plot in the grid
plt.plot(frequencies, noisy_fft_magnitude, 'b-', label='Noisy Signal Spectrum', alpha=0.5)
plt.plot(frequencies, filtered_fft_magnitude, 'r-', linewidth=2, label='Filtered Signal Spectrum')
plt.xlim(0, 5000) # Zoom in on the 0-5kHz range
plt.title("Frequency Domain: FFT Spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.legend()
plt.grid(True)

plt.tight_layout() # Adjust plots to prevent overlap
plt.show()