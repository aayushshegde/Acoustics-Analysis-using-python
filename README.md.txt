# Acoustic Signal Processing and Analysis in Python

## Project Objective

This project demonstrates the fundamentals of digital signal processing (DSP) to analyze and filter a simulated acoustic signal. It showcases a complete workflow: generating a noisy signal, applying a digital filter to remove the noise, and using a Fast Fourier Transform (FFT) to verify the result in the frequency domain.

This was built as a practical exercise to target the skills required for an Acoustic Instrument Systems Design Engineer role.

---

## How It Works

The Python script (`generate_signal.py`) performs the following steps:

1.  **Signal Generation:** Creates a clean 1kHz sine wave and adds random Gaussian noise to simulate a real-world sensor reading.
2.  **Filtering:** Designs and applies a digital low-pass Butterworth filter to remove the high-frequency noise from the signal.
3.  **Analysis & Visualization:** Generates two plots for comparison:
    * **Time Domain Plot:** Shows the noisy signal vs. the clean, filtered signal over time.
    * **Frequency Domain Plot:** Shows the FFT spectrum of both signals, proving that the filter successfully removed noise while preserving the desired 1kHz tone.

---

## Key Skills Demonstrated

* **Programming:** Python
* **Libraries:** NumPy (for numerical operations), Matplotlib (for plotting), SciPy (for filter design and signal processing).
* **Core Concepts:**
    * Digital Signal Processing (DSP)
    * Digital Filter Design (Low-pass Butterworth)
    * Fast Fourier Transform (FFT) for frequency analysis.
    * Data Visualization

---

## How to Run

1.  **Ensure you have Python and the required libraries installed:**
    ```bash
    pip install numpy matplotlib scipy
    ```
2.  **Run the script from your terminal:**
    ```bash
    python generate_signal.py
    ```