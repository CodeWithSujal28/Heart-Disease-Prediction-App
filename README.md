# ❤️ Heart Disease Prediction Web App

This is a **machine learning–based web application** that predicts whether a person is likely to have heart disease based on medical input data.
The project uses a **K-Nearest Neighbors (KNN)** model and is deployed using **Flask** with a clean, user-friendly medical UI.

---

## 🚀 Features

* Machine Learning model using **KNN**
* **StandardScaler** used for consistent feature scaling
* Clean and modern **medical-style UI**
* Dropdowns and sliders for easy, error-free input
* Real-time prediction
* Refresh button for new prediction
* User-friendly labels with explanations

---

## 🛠 Tech Stack

* **Python**
* **Flask**
* **Scikit-learn**
* **NumPy**
* **HTML & CSS**

---

## 📂 Project Structure

```
Heart-Disease-Prediction-App/
│
├── app.py
├── KNN_Heart.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Flask app

```bash
python app.py
```

### 3️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 📊 Model Information

* **Algorithm:** K-Nearest Neighbors (KNN)
* **Preprocessing:** StandardScaler
* **Dataset:** UCI Heart Disease Dataset
* **Target:** Presence or absence of heart disease

---

## ✅ Model Testing & Validation

* Evaluated using accuracy, confusion matrix, and classification report
* Predictions verified by comparing notebook outputs with deployed app outputs
* Manual test cases and edge cases tested
* Correct feature ordering ensured using saved column list

---

## 🎯 Use Case

This application can be used as:

* An academic machine learning project
* A portfolio project for placements
* A demonstration of ML model deployment using Flask

> ⚠️ This project is for educational purposes only and should not be used as a medical diagnosis tool.

---

## 👤 Author

**Sujal Mondal**

---
