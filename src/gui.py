import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import wfdb
import os
import pandas as pd
from io import BytesIO
from tempfile import NamedTemporaryFile
from filtering import (
    apply_notch_filter, apply_highpass_filter,
    apply_lowpass_filter, apply_wavelet_denoising,
    apply_savgol_filter
)
from preprocessing import (
    add_powerline_noise, add_baseline_wander, add_emg_noise
)
from evaluation import calculate_snr, calculate_mse

# Streamlit Page Configuration
st.set_page_config(page_title="ECG Noise Removal", layout="wide")

st.title("📊 ECG Noise Removal Application")

# 📌 Upload ECG Signal
uploaded_file = st.file_uploader("Upload an ECG signal file (.dat)", type=["dat"])
if uploaded_file is not None:
    # Save .dat file as temporary file
    with NamedTemporaryFile(delete=False, suffix=".dat") as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        temp_path = temp_file.name  # Store file path

    # Generate a temporary header (.hea) file
    temp_hea_path = temp_path.replace(".dat", ".hea")
    record_name = os.path.splitext(os.path.basename(temp_path))[0]

    sampling_frequency = 360  # Assuming MIT-BIH dataset
    num_samples = 650000  # Estimated total samples
    signal_format = 212  # Format used in MIT-BIH ECG recordings

    with open(temp_hea_path, "w") as f:
        f.write(f"{record_name} 1 {sampling_frequency} {num_samples}\n")
        f.write(f"{record_name}.dat {signal_format} 200 11 1024 0 0 0\n")

    # Load ECG Signal
    try:
        ecg_data = wfdb.rdrecord(temp_path.replace(".dat", ""))
    except Exception as e:
        st.error(f"Error reading ECG file: {e}")
        os.remove(temp_path)
        os.remove(temp_hea_path)
        st.stop()

    # Extract ECG Signal
    signal = ecg_data.p_signal[:, 0]
    fs = ecg_data.fs

    # 📉 Display Original ECG Signal
    st.subheader("📉 Original ECG Signal")
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.plot(signal[:fs * 5], color="blue")
    ax.set_title("Original ECG (First 5 seconds)")
    ax.set_xlabel("Time (samples)")
    ax.set_ylabel("Amplitude (mV)")
    st.pyplot(fig)

    # 🔊 Add Noise to ECG Signal
    st.subheader("🔊 Add Noise to ECG")
    noise_type = st.radio("Choose a noise type:", ["None", "Powerline (50Hz)", "Baseline Wander", "EMG Noise"])

    # Apply Noise
    if noise_type == "Powerline (50Hz)":
        noisy_signal = add_powerline_noise(signal, fs)
    elif noise_type == "Baseline Wander":
        noisy_signal = add_baseline_wander(signal, fs)
    elif noise_type == "EMG Noise":
        noisy_signal = add_emg_noise(signal)
    else:
        noisy_signal = signal  # No noise added

    # 📉 Display Noisy ECG Signal
    st.subheader(f"📉 Noisy ECG Signal - {noise_type}")
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.plot(noisy_signal[:fs * 5], color="red")
    ax.set_title(f"ECG with {noise_type} Noise")
    ax.set_xlabel("Time (samples)")
    ax.set_ylabel("Amplitude (mV)")
    st.pyplot(fig)

    # 🛠️ Apply Filtering Method
    st.subheader("🛠️ Apply Noise Removal")
    filter_type = st.selectbox("Choose a filtering method:", [
        "Notch Filter (Powerline Noise)", "High-Pass Filter (Baseline Wander)", 
        "Low-Pass Filter (EMG Noise)", "Wavelet Transform", "Savitzky-Golay Filter"
    ])

    # Apply Filtering
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

    # ✅ Display Filtered ECG Signal
    st.subheader(f"✅ Filtered ECG Signal - {filter_type}")
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.plot(filtered_signal[:fs * 5], color="green")
    ax.set_title(f"ECG After {filter_type}")
    ax.set_xlabel("Time (samples)")
    ax.set_ylabel("Amplitude (mV)")
    st.pyplot(fig)

    # 📊 Compute Performance Metrics
    snr_before = calculate_snr(signal, noisy_signal)
    snr_after = calculate_snr(signal, filtered_signal)
    mse_after = calculate_mse(signal, filtered_signal)

    # 📊 Display Performance Metrics
    st.subheader("📊 Filtering Performance Metrics")
    st.write(f"**SNR Before Filtering:** {snr_before:.2f} dB")
    st.write(f"**SNR After Filtering:** {snr_after:.2f} dB")
    st.write(f"**MSE After Filtering:** {mse_after:.6f}")

    # 📥 Allow Download of Filtered ECG Signal
    buffer = BytesIO()
    pd.DataFrame({"Filtered ECG": filtered_signal}).to_csv(buffer, index=False)
    buffer.seek(0)

    st.download_button(
        label="📥 Download Filtered ECG as CSV",
        data=buffer,
        file_name="filtered_ecg.csv",
        mime="text/csv"
    )

    # Cleanup Temporary Files
    os.remove(temp_path)
    os.remove(temp_hea_path)
