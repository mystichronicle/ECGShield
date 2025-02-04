import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, iirnotch
import pywt
from scipy.signal import savgol_filter


def apply_savgol_filter(signal, window_size=151, poly_order=7):
    return signal - savgol_filter(signal, window_size, poly_order)


def apply_notch_filter(signal, fs, notch_freq=50, quality_factor=30):
    """Apply a notch filter to remove powerline interference at 50 Hz."""
    b, a = iirnotch(notch_freq, quality_factor, fs)
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal


def apply_highpass_filter(signal, fs, cutoff=0.5, order=4):
    """Apply a high-pass Butterworth filter to remove baseline wander."""
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal


def apply_lowpass_filter(signal, fs, cutoff=50, order=4):
    """Apply a low-pass Butterworth filter to remove EMG noise."""
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal


def apply_wavelet_denoising(signal, wavelet='db6', level=5):
    """Apply Wavelet Transform-based denoising."""
    coeffs = pywt.wavedec(signal, wavelet, level=level)
    threshold = np.std(coeffs[-level])  # Thresholding based on noise level
    coeffs[1:] = [pywt.threshold(c, threshold, mode='soft')
                  for c in coeffs[1:]]
    denoised_signal = pywt.waverec(coeffs, wavelet)
    return denoised_signal[:len(signal)]  # Match original length


def apply_highpass_filter(signal, fs, cutoff=0.3, order=4):
    """Apply a high-pass Butterworth filter to remove baseline wander."""
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal


def plot_ecg(signal, sampling_rate, num_seconds=5, title="Filtered ECG Signal"):
    """Plot ECG Signal."""
    num_samples = num_seconds * sampling_rate
    time_axis = np.arange(0, num_samples) / sampling_rate

    plt.figure(figsize=(12, 4))
    plt.plot(time_axis, signal[:num_samples], color="green", linewidth=1)
    plt.title(title)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude (mV)")
    plt.grid(True)
    plt.show()
