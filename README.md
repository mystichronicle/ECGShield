# 🛡️ ECGShield - Noise Removal from ECG Signals
> **A powerful tool for removing noise from ECG signals using advanced filtering techniques.**

> Built with **Python and Streamlit**, ECGShield helps in **denoising ECG signals** with interactive visualizations and real-time filtering.


---

## 📌 Features
✅ **Upload ECG `.dat` files** from the **MIT-BIH Arrhythmia Database**  
✅ **Visualize the raw ECG signal** for analysis  
✅ **Add artificial noise** to simulate real-world ECG disturbances  
✅ **Apply various filtering techniques**:
   - **Notch Filter** *(removes powerline interference)*
   - **High-Pass Filter** *(removes baseline wander)*
   - **Low-Pass Filter** *(removes EMG noise)*
   - **Wavelet Transform Denoising** *(removes multi-frequency noise)*
   - **Savitzky-Golay Filter** *(smoothens signal without distorting peaks)*  
✅ **Analyze Performance Metrics**:
   - **Signal-to-Noise Ratio (SNR)**
   - **Mean Squared Error (MSE)**
✅ **Download the cleaned ECG signal** for further research  
✅ **Fully interactive UI** using **Streamlit**  
✅ **Runs locally without requiring cloud deployment**

---

## 📌 Installation Guide
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/mystichronicle/ECGShield.git
cd ECGShield
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Streamlit App Locally**
```bash
streamlit run src/gui.py
```
- This will open the **ECG Noise Removal App** in the browser.
- The **local server** will run at:  
  ```
  http://localhost:8501
  ```

---

## 📌 Usage Guide
### **Step 1: Upload an ECG File**
- Upload a `.dat` file from the **MIT-BIH Arrhythmia Database**.

### **Step 2: Visualize the Raw ECG Signal**
- The original ECG signal will be plotted.

### **Step 3: Add Noise**
- Choose from **Powerline Noise, Baseline Wander, or EMG Noise**.

### **Step 4: Apply Filtering**
- Select a **filtering method** to remove the noise.

### **Step 5: View Performance Metrics**
- Check the **SNR and MSE values** before & after filtering.

### **Step 6: Download the Processed ECG**
- Save the cleaned ECG signal as a `.csv` file.

---

## 📌 Project Structure
```
ECGShield/
│── src/                       # Python backend (Streamlit)
│   ├── gui.py                 # Main Streamlit GUI script
│   ├── filtering.py           # Signal filtering functions
│   ├── preprocessing.py       # Noise addition functions
│   ├── evaluation.py          # SNR & MSE calculations
│   └── utils.py               # Utility functions
│
│── data/                      # ECG Data (ignored in .gitignore)
│   ├── raw/                   # Original ECG signals
│   ├── processed/             # Filtered signals
│
│── README.md                  # Project Documentation
│── requirements.txt           # Python dependencies
│── .gitignore                 # Ignore unnecessary files
└── LICENSE                    # Open-source license
```

---

## 📌 Technologies Used
| Component    | Technology |
|-------------|------------|
| **Backend**  | Streamlit, Python |
| **Signal Processing** | NumPy, SciPy, WFDB, PyWavelets |


---

## 📌 License
📜 **MIT License** - You are free to use, modify, and distribute this project with proper attribution.  

---

## 📌 Acknowledgments
🙏 Special thanks to:
- **MIT-BIH Arrhythmia Database** for ECG datasets
- **Streamlit & Python communities** for amazing frameworks
- **OpenAI & SciPy** for signal processing tools

---

### 🚀 Ready to Use?
📥 **Clone Now:**  
```bash
git clone https://github.com/mystichronicle/ECGShield.git
```
🎉 **Enjoy real-time ECG noise removal with `ECGShield`!** 🚀
