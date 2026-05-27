<div align="center">

# 🔮 Customer Churn Prediction

**Predict customer churn before it happens — powered by Machine Learning & Flask**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-RandomForest-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 📌 Overview

**Customer Churn Prediction** is a full-stack machine learning web application that predicts whether a telecom customer is likely to churn — helping businesses take proactive action before losing a customer.

A user enters billing and contract details through a clean web interface, and the app returns an instant churn risk assessment with a probability score, powered by a trained **Random Forest** classifier served via a **Flask** REST API.

---

## ✨ Features

- 🧠 **ML-powered predictions** using Random Forest Classifier (scikit-learn)
- ⚡ **Real-time inference** via a Flask REST API (`/predict` endpoint)
- 🌐 **Responsive web UI** built with HTML, CSS, Bootstrap & JavaScript
- 💱 **INR-aware model** — charges converted from USD to ₹ (₹83 = $1) during training
- 📊 **Probability score** returned alongside binary churn prediction
- 🏗️ **Clean separation** of training pipeline (`train_model.py`) and serving (`app.py`)

---

## 🗂️ Project Structure

```
Customer-Churn-Prediction/
│
├── data/
│   └── Telco-Customer-Churn.csv      # Telco dataset (IBM)
│
├── models/
│   ├── rf_churn_model.pkl            # Trained Random Forest model
│   └── scaler.pkl                    # StandardScaler for numerical features
│
├── static/                           # CSS, JS, frontend assets
├── templates/
│   └── index.html                    # Main web interface
│
├── app.py                            # Flask app — serves UI & prediction API
├── train_model.py                    # Model training & export script
└── requirements.txt
```

---

## 🧠 How It Works

### Training Pipeline (`train_model.py`)

| Step | Description |
|------|-------------|
| **Load** | Read `Telco-Customer-Churn.csv`, clean nulls in `TotalCharges` |
| **Feature Selection** | `tenure`, `MonthlyCharges`, `TotalCharges`, `Contract`, `InternetService`, `PaymentMethod` |
| **Currency Conversion** | Charges multiplied by ₹83 to localize for Indian context |
| **Encoding** | One-hot encoding via `pd.get_dummies()` |
| **Scaling** | `StandardScaler` applied to numerical columns |
| **Train** | `RandomForestClassifier` with `class_weight='balanced'`, `n_estimators=100`, `max_depth=10` |
| **Export** | Model & scaler saved as `.pkl` files via `joblib` |

### Prediction API (`app.py`)

The `/predict` endpoint accepts a JSON payload, auto-calculates `TotalCharges` from `tenure × monthly_charges`, scales the input, and returns:

```json
{
  "churn_risk": 1,
  "probability": 73.45
}
```

> `churn_risk: 1` → Customer is likely to churn  
> `churn_risk: 0` → Customer is likely to stay

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Dhruvbhujbal/Customer-Churn-Prediction-.git
cd Customer-Churn-Prediction-

# Install dependencies
pip install -r requirements.txt
```

### Train the Model

```bash
python train_model.py
```

This will output something like:
```
✅ Success! 'rf_churn_model.pkl' and 'scaler.pkl' are ready for your Flask app.
📊 Model Accuracy on Test Data: XX.XX%
```

### Run the App

```bash
python app.py
```

Then open your browser at **`http://127.0.0.1:5000`**

---

## 🎛️ Input Features

| Feature | Type | Description |
|---------|------|-------------|
| `tenure` | Numeric | Number of months the customer has been with the company |
| `monthly_charges` | Numeric | Monthly billing amount (₹) |
| `contract` | Categorical | `Month-to-month`, `One year`, `Two year` |
| `internet_service` | Categorical | `DSL`, `Fiber optic`, `No` |
| `payment_method` | Categorical | `Electronic check`, `Mailed check`, `Bank transfer`, `Credit card` |

> `TotalCharges` is auto-calculated as `tenure × monthly_charges` — no manual input needed.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **ML Model** | scikit-learn — Random Forest Classifier |
| **Backend** | Flask, joblib, pandas |
| **Frontend** | HTML5, CSS3, Bootstrap, JavaScript (fetch API) |
| **Data** | IBM Telco Customer Churn Dataset |

---

## 📈 Dataset

This project uses the **[IBM Telco Customer Churn dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)**, a popular benchmark dataset with ~7,000 telecom customer records and a binary churn label.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## 👤 Author

**Dhruv Bhujbal**  
M.Sc. Data Science | Savitribai Phule Pune University  
[![GitHub](https://img.shields.io/badge/GitHub-Dhruvbhujbal-181717?style=flat-square&logo=github)](https://github.com/Dhruvbhujbal)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-dhruvbhujbal2601-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/dhruvbhujbal2601)

---

<div align="center">

*If this project helped you, consider leaving a ⭐ on the repo!*

</div>
