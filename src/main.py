from preprocessing import load_ecg, add_powerline_noise, add_baseline_wander, add_emg_noise
from filtering import apply_notch_filter, apply_highpass_filter, apply_lowpass_filter, apply_wavelet_denoising, plot_ecg, apply_savgol_filter, apply_highpass_filter
from evaluation import evaluate_filtering, plot_evaluation_results

ecg_signal, fs = load_ecg("100")

ecg_powerline = add_powerline_noise(ecg_signal, fs)
ecg_baseline_wander = add_baseline_wander(ecg_signal, fs)
ecg_emg = add_emg_noise(ecg_signal)

filtered_powerline = apply_notch_filter(ecg_powerline, fs)
filtered_baseline = apply_highpass_filter(ecg_baseline_wander, fs)
filtered_emg = apply_lowpass_filter(ecg_emg, fs)
wavelet_denoised = apply_wavelet_denoising(ecg_signal)

evaluate_filtering(ecg_signal, ecg_powerline, filtered_powerline,
                   "Notch Filter (Powerline Noise Removal)")
evaluate_filtering(ecg_signal, ecg_baseline_wander, filtered_baseline,
                   "High-Pass Filter (Baseline Wander Removal)")
evaluate_filtering(ecg_signal, ecg_emg, filtered_emg,
                   "Low-Pass Filter (EMG Noise Removal)")
evaluate_filtering(ecg_signal, ecg_emg, wavelet_denoised,
                   "Wavelet Transform Denoising")

results = {}

results["Notch Filter"] = evaluate_filtering(
    ecg_signal, ecg_powerline, filtered_powerline, "Notch Filter (Powerline Noise Removal)")
results["High-Pass Filter"] = evaluate_filtering(
    ecg_signal, ecg_baseline_wander, filtered_baseline, "High-Pass Filter (Baseline Wander Removal)")
results["Low-Pass Filter"] = evaluate_filtering(
    ecg_signal, ecg_emg, filtered_emg, "Low-Pass Filter (EMG Noise Removal)")
results["Wavelet Transform"] = evaluate_filtering(
    ecg_signal, ecg_emg, wavelet_denoised, "Wavelet Transform Denoising")

plot_evaluation_results(results)

filtered_baseline_savgol = apply_savgol_filter(ecg_baseline_wander)
evaluate_filtering(ecg_signal, ecg_baseline_wander,
                   filtered_baseline_savgol, "Savitzky-Golay Filter (Baseline Removal)")
plot_ecg(filtered_baseline_savgol, fs, title="ECG After Savitzky-Golay Filter")
