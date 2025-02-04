import wfdb
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.signal import butter, filtfilt, iirnotch

# Absolute path to the dataset
DATA_PATH = "/home/debjit/Programming/ML/ecg_denoising/data/raw/mitdb/mit-bih-arrhythmia-database-1.0.0/"

def load_ecg(record_name, data_path=DATA_PATH):
    """
    Load an ECG signal from the MIT-BIH Arrhythmia Database.
    """
    record_path = os.path.join(data_path, record_name)
    record = wfdb.rdrecord(record_path)
    signal = record.p_signal[:, 0]  # Extract Lead I ECG Signal
    sampling_rate = record.fs  # Sampling frequency
    return signal, sampling_rate

def add_powerline_noise(signal, fs, freq=50, noise_amplitude=0.2):
    """Add 50Hz or 60Hz powerline interference."""
    t = np.arange(len(signal)) / fs
    noise = noise_amplitude * np.sin(2 * np.pi * freq * t)
    return signal + noise

def add_baseline_wander(signal, fs, freq=0.5, noise_amplitude=0.5):
    """Add low-frequency baseline wander."""
    t = np.arange(len(signal)) / fs
    noise = noise_amplitude * np.sin(2 * np.pi * freq * t)
    return signal + noise

def add_emg_noise(signal, noise_amplitude=0.1):
    """Add high-frequency EMG noise (random white noise)."""
    noise = noise_amplitude * np.random.randn(len(signal))
    return signal + noise

def plot_ecg(signal, sampling_rate, num_seconds=5, title="ECG Signal"):
    """
    Plot ECG Signal.
    """
    num_samples = num_seconds * sampling_rate
    time_axis = np.arange(0, num_samples) / sampling_rate
    
    plt.figure(figsize=(12, 4))
    plt.plot(time_axis, signal[:num_samples], color="blue", linewidth=1)
    plt.title(title)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude (mV)")
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    ecg_signal, fs = load_ecg("100")  # Load record 100

    # Original ECG Plot
    plot_ecg(ecg_signal, fs, title="Original ECG Signal")

    # Add Noise
    ecg_with_powerline = add_powerline_noise(ecg_signal, fs)
    plot_ecg(ecg_with_powerline, fs, title="ECG with Powerline Interference")

    ecg_with_baseline_wander = add_baseline_wander(ecg_signal, fs)
    plot_ecg(ecg_with_baseline_wander, fs, title="ECG with Baseline Wander")

    ecg_with_emg_noise = add_emg_noise(ecg_signal)
    plot_ecg(ecg_with_emg_noise, fs, title="ECG with EMG Noise")
