import wfdb
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.signal import butter, filtfilt, iirnotch

DATA_PATH = "/home/debjit/Programming/ML/ecg_denoising/data/raw/mitdb/mit-bih-arrhythmia-database-1.0.0/"


def load_ecg(record_name, data_path=DATA_PATH):
    record_path = os.path.join(data_path, record_name)
    record = wfdb.rdrecord(record_path)
    signal = record.p_signal[:, 0]
    sampling_rate = record.fs
    return signal, sampling_rate


def add_powerline_noise(signal, fs, freq=50, noise_amplitude=0.2):
    t = np.arange(len(signal)) / fs
    noise = noise_amplitude * np.sin(2 * np.pi * freq * t)
    return signal + noise


def add_baseline_wander(signal, fs, freq=0.5, noise_amplitude=0.5):
    t = np.arange(len(signal)) / fs
    noise = noise_amplitude * np.sin(2 * np.pi * freq * t)
    return signal + noise


def add_emg_noise(signal, noise_amplitude=0.1):
    noise = noise_amplitude * np.random.randn(len(signal))
    return signal + noise


def plot_ecg(signal, sampling_rate, num_seconds=5, title="ECG Signal"):
    num_samples = num_seconds * sampling_rate
    time_axis = np.arange(0, num_samples) / sampling_rate

    plt.figure(figsize=(12, 4))
    plt.plot(time_axis, signal[:num_samples], color="blue", linewidth=1)
    plt.title(title)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude (mV)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    ecg_signal, fs = load_ecg("100")

    plot_ecg(ecg_signal, fs, title="Original ECG Signal")

    ecg_with_powerline = add_powerline_noise(ecg_signal, fs)
    plot_ecg(ecg_with_powerline, fs, title="ECG with Powerline Interference")

    ecg_with_baseline_wander = add_baseline_wander(ecg_signal, fs)
    plot_ecg(ecg_with_baseline_wander, fs, title="ECG with Baseline Wander")

    ecg_with_emg_noise = add_emg_noise(ecg_signal)
    plot_ecg(ecg_with_emg_noise, fs, title="ECG with EMG Noise")
