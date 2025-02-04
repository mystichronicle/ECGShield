import numpy as np
import matplotlib.pyplot as plt


def plot_evaluation_results(results):
    """
    Plot SNR Before, SNR After, and MSE for all filters.

    :param results: Dictionary with filtering method names as keys and (SNR Before, SNR After, MSE) as values.
    """
    methods = list(results.keys())
    snr_before = [results[m][0] for m in methods]
    snr_after = [results[m][1] for m in methods]
    mse_values = [results[m][2] for m in methods]

    plt.figure(figsize=(10, 5))

    # Plot SNR Improvement
    plt.subplot(1, 2, 1)
    plt.bar(methods, snr_before, label="SNR Before", alpha=0.6)
    plt.bar(methods, snr_after, label="SNR After", alpha=0.8)
    plt.title("SNR Comparison")
    plt.ylabel("SNR (dB)")
    plt.xticks(rotation=20)
    plt.legend()

    # Plot MSE
    plt.subplot(1, 2, 2)
    plt.bar(methods, mse_values, color="red")
    plt.title("Mean Squared Error (MSE)")
    plt.ylabel("MSE")
    plt.xticks(rotation=20)

    plt.tight_layout()
    plt.show()


def calculate_snr(original_signal, noisy_signal):
    """
    Compute the Signal-to-Noise Ratio (SNR).
    SNR = 10 * log10(P_signal / P_noise)
    """
    signal_power = np.mean(original_signal ** 2)
    noise_power = np.mean((original_signal - noisy_signal) ** 2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr


def calculate_mse(original_signal, filtered_signal):
    """
    Compute the Mean Squared Error (MSE).
    MSE = (1/N) * Σ (original - filtered)^2
    """
    mse = np.mean((original_signal - filtered_signal) ** 2)
    return mse


def evaluate_filtering(original_signal, noisy_signal, filtered_signal, method_name):
    """
    Print performance metrics for a given filtering method.
    """
    snr_before = calculate_snr(original_signal, noisy_signal)
    snr_after = calculate_snr(original_signal, filtered_signal)
    mse = calculate_mse(original_signal, filtered_signal)

    print(f"\nPerformance of {method_name}:")
    print(f"SNR Before Filtering: {snr_before:.2f} dB")
    print(f"SNR After Filtering: {snr_after:.2f} dB")
    print(f"MSE After Filtering: {mse:.6f}")

    return snr_before, snr_after, mse
