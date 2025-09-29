# 🏭 Supplier Evaluation Dashboard

An AI-powered **Supplier Evaluation Dashboard** built with **Streamlit** that allows businesses to analyze, rank, and evaluate suppliers based on procurement KPIs.

🔗 **Live Demo**: [Supplier Evaluation Dashboard](https://supplier-evaluations.streamlit.app/)

---

## 🚀 Features

* 📊 Interactive **Streamlit dashboard** for supplier evaluation
* 🤖 **Machine Learning model** to score and rank suppliers
* 📈 Custom supplier ranking based on uploaded data
* ⚙️ Trained pipeline with **Scaler + Model (`.pkl` files)**
* 🧾 Training workflow in **Jupyter Notebook** (`supplier_training.ipynb`)

---

## 📂 Project Structure

```
.
├── app.py                   # Streamlit app (main dashboard)
├── supplier_training.ipynb  # Training notebook
├── supplier_model.pkl       # Trained ML model
├── scaler.pkl               # Data scaler
├── supplier_ranking.csv     # Sample supplier ranking results
├── requirements.txt         # Python dependencies
├── Procurement KPI Analysis Dataset 1.xlsx  # Sample dataset
└── README.md
```

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/u-faizan/Supplier-Evaluation-Dashboard.git
cd Supplier-Evaluation-Dashboard
```

### 2️⃣ Create Virtual Environment (Optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Streamlit App

```bash
streamlit run app.py
```

The app will be available at:
👉 `http://localhost:8501/`

---

## 📊 Training the Model

If you want to retrain the model:

* Open `supplier_training.ipynb`
* Run all cells to preprocess data, train model, and save `.pkl` files

---

## 🛠️ Tech Stack

* **Python** (Pandas, Scikit-learn, NumPy)
* **Streamlit** (interactive dashboard)
* **Jupyter Notebook** (model training & experimentation)

---

## 📌 Future Improvements

* ✅ Add authentication for multiple company logins
* ✅ Integrate live supplier performance APIs
* ✅ Deploy with CI/CD pipeline for auto-updates

---

## 👨‍💻 Author

**Umar Faizan**

* 💼 [LinkedIn](https://www.linkedin.com/in/umar-faizan)
* 🐙 [GitHub](https://github.com/u-faizan)

---

⭐ If you find this project useful, consider giving it a **star** on GitHub!
