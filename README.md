# 🛡️ ECGShield - Noise Removal from ECG Signals
> **A powerful tool for removing noise from ECG signals using advanced filtering techniques.**

> Built with **Python, Streamlit, React, and GitHub Pages**, ECGShield helps in **denoising ECG signals** with interactive visualizations and real-time filtering.


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
✅ **Fully interactive UI** using **Streamlit & React**  
✅ **Deployed with GitHub Pages & Streamlit Cloud**

---

## 🚀 Live Demo
🖥️ **Frontend (React):** [ECGShield GitHub Pages](https://mystichronicle.github.io/ECGShield)  
📡 **Backend (Streamlit):** [ECGShield Streamlit Cloud](https://ecg-noise-removal.streamlit.app)

---

## 📌 Installation Guide
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/mystichronicle/ECGShield.git
cd ECGShield
```

### **2️⃣ Install Python Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Backend (Streamlit)**
```bash
streamlit run src/streamlit_app.py
```
The **backend will start at** `http://localhost:8501`.

### **4️⃣ Run the Frontend (React)**
```bash
cd ecg-frontend
npm install
npm start
```
The **frontend will start at** `http://localhost:3000`.

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
│── ecg-frontend/              # React frontend
│   ├── src/                   
│   │   ├── App.js             # React UI
│   │   ├── index.js           # Main React entry
│   │   └── styles.css         # CSS styles
│   ├── public/                # Static assets
│   ├── package.json           # React dependencies
│   ├── .gitignore             
│   ├── README.md              
│   ├── node_modules/          # Installed dependencies
│   └── build/                 # Deployed static files (GitHub Pages)
│
│── src/                       # Python backend (Streamlit)
│   ├── streamlit_app.py       # Main backend script
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
│── requirements.txt            # Python dependencies
│── .gitignore                  # Ignore unnecessary files
│── LICENSE                     # Open-source license
└── deploy.sh                   # Deployment script
```

---

## 📌 Technologies Used
| Component    | Technology |
|-------------|------------|
| **Frontend** | React, GitHub Pages |
| **Backend**  | Streamlit, Python |
| **Signal Processing** | NumPy, SciPy, WFDB, PyWavelets |
| **Deployment** | GitHub Pages, Streamlit Cloud |

---

## 📌 License
📜 **MIT License** - You are free to use, modify, and distribute this project with proper attribution.  

---

## 📌 Acknowledgments
🙏 Special thanks to:
- **MIT-BIH Arrhythmia Database** for ECG datasets
- **Streamlit & React communities** for amazing frameworks
- **OpenAI & SciPy** for signal processing tools

---

### 🚀 Ready to Use?
📥 **Clone Now:**  
```bash
git clone https://github.com/mystichronicle/ECGShield.git
```
🎉 **Enjoy real-time ECG noise removal with `ECGShield`!** 🚀
