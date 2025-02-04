import streamlit as st
import numpy as np
import wfdb
import os
import pandas as pd
from io import BytesIO
from filtering import (
    apply_notch_filter, apply_highpass_filter,
    apply_lowpass_filter, apply_wavelet_denoising,
    apply_savgol_filter
)
from preprocessing import (
    add_powerline_noise, add_baseline_wander, add_emg_noise
)
from evaluation import calculate_snr, calculate_mse

st.set_page_config(page_title="ECG Noise Removal", layout="wide")

st.title("📊 ECG Noise Removal - Streamlit Backend")

uploaded_file = st.file_uploader("Upload an ECG signal file (.dat)", type=["dat"])

if uploaded_file is not None:
    with NamedTemporaryFile(delete=False, suffix=".dat") as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        temp_path = temp_file.name

    temp_hea_path = temp_path.replace(".dat", ".hea")
    record_name = os.path.splitext(os.path.basename(temp_path))[0]

    with open(temp_hea_path, "w") as f:
        f.write(f"{record_name} 1 360 650000\n")
        f.write(f"{record_name}.dat 212 200 11 1024 0 0 0\n")

    ecg_data = wfdb.rdrecord(temp_path.replace(".dat", ""))
    signal = ecg_data.p_signal[:, 0]
    fs = ecg_data.fs

    st.subheader("📉 Original ECG Signal")
    st.line_chart(signal[:fs * 5])

    noise_type = st.radio("Choose a noise to add:", ["None", "Powerline (50Hz)", "Baseline Wander", "EMG Noise"])
    if noise_type == "Powerline (50Hz)":
        noisy_signal = add_powerline_noise(signal, fs)
    elif noise_type == "Baseline Wander":
        noisy_signal = add_baseline_wander(signal, fs)
    elif noise_type == "EMG Noise":
        noisy_signal = add_emg_noise(signal)
    else:
        noisy_signal = signal

    st.subheader("🔊 Noisy ECG Signal")
    st.line_chart(noisy_signal[:fs * 5])

    filter_type = st.selectbox("Choose a filtering method:", [
        "Notch Filter (Powerline Noise)", "High-Pass Filter (Baseline Wander)",
        "Low-Pass Filter (EMG Noise)", "Wavelet Transform", "Savitzky-Golay Filter"
    ])

    if filter_type == "Notch Filter (Powerline Noise)":
        filtered_signal = apply_notch_filter(noisy_signal, fs)
    elif filter_type == "High-Pass Filter (Baseline Wander)":
        filtered_signal = apply_highpass_filter(noisy_signal, fs)
    elif filter_type == "Low-Pass Filter (EMG Noise)":
        filtered_signal = apply_lowpass_filter(noisy_signal, fs)
    elif filter_type == "Wavelet Transform":
        filtered_signal = apply_wavelet_denoising(noisy_signal)
    elif filter_type == "Savitzky-Golay Filter":
        filtered_signal = apply_savgol_filter(noisy_signal)

    st.subheader("✅ Filtered ECG Signal")
    st.line_chart(filtered_signal[:fs * 5])

    snr_before = calculate_snr(signal, noisy_signal)
    snr_after = calculate_snr(signal, filtered_signal)
    mse_after = calculate_mse(signal, filtered_signal)

    st.write(f"**SNR Before Filtering:** {snr_before:.2f} dB")
    st.write(f"**SNR After Filtering:** {snr_after:.2f} dB")
    st.write(f"**MSE After Filtering:** {mse_after:.6f}")

    buffer = BytesIO()
    pd.DataFrame({"Filtered ECG": filtered_signal}).to_csv(buffer, index=False)
    buffer.seek(0)
    st.download_button(
        label="📥 Download Filtered ECG as CSV",
        data=buffer,
        file_name="filtered_ecg.csv",
        mime="text/csv"
    )
