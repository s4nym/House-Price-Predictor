# 🏠 House Price Predictor (India)

A Streamlit web app that predicts house prices in India using machine learning. Built with **XGBoost**, it uses real estate features to estimate the expected price of a house. Perfect for portfolio showcase, data science demos, or learning ML deployment.

---

## 🔹 Features

- Predict house prices using **20+ features**, including:
  - Number of bedrooms & bathrooms
  - Living area & lot area
  - House grade, condition, floors
  - Built year & renovation year
  - Location info (latitude, longitude, postal code)
  - Nearby schools, distance from airport, waterfront, etc.
- Log-transformed target to handle price skew
- Real-time predictions in a **user-friendly Streamlit interface**
- Feature importance plots (optional) to understand which attributes drive prices

---

## 📊 Dataset

- Source: [House Price India CSV](https://raw.githubusercontent.com/s4nym/House-Price-Predictor/main/House%20Price%20India.csv)
- 14,619 rows, 23 columns
- Target: `Price` (INR)
- Features include numeric, categorical indicators for house attributes and location

**Price statistics:**

| Metric | Value |
|--------|-------|
| Count  | 14,619 |
| Mean   | 5,38,806 ₹ |
| Min    | 78,000 ₹ |
| Max    | 7,700,000 ₹ |
| Median | 4,50,000 ₹ |

---

## 🛠 Technology Stack

- Python 3.10+
- Libraries:
  - `pandas`, `numpy` — data handling
  - `scikit-learn` — preprocessing & evaluation
  - `xgboost` — regression model
  - `joblib` — model serialization
  - `streamlit` — interactive web app
  - `matplotlib`, `seaborn` — feature importance visualization

---

## 🚀 How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/s4nym/House-Price-Predictor.git
cd House-Price-Predictor
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. The app will open in your browser at `http://localhost:8501`

---

## 📈 Model

- **Trained models compared:**
  - Linear Regression — RMSE: 0.251, R²: 0.78
  - Random Forest — RMSE: 0.174, R²: 0.89
  - XGBoost — RMSE: 0.161, R²: 0.91 ✅ (Best model)
- The app uses **XGBoost** for real-time predictions.
- Log-transform applied on `Price` for better model performance.

---

## 🔹 Usage

1. Enter property details in the app (defaults provided).
2. Click **Predict Price**.
3. Get the estimated price in INR instantly.

**Default input example:**
- 3 Bedrooms, 2 Bathrooms  
- 1000 sq.ft living area, 5000 sq.ft lot  
- Grade 7, Built 2000, Renovated 2000  
- Distance from airport 20 km, 5 nearby schools  

Predicted price with defaults: ~₹2,57,592 (reasonable for a small-to-medium house).

---

## 📂 Files in Repository

- `app.py` — Streamlit app  
- `house_price_xgb.pkl` — saved XGBoost model  
- `House Price India.csv` — dataset  
- `requirements.txt` — Python dependencies  

---

## 👨‍💻 Author

**Sanyam Sood**  

---

## ⚡ Future Improvements

- Add **interactive feature importance charts** in the app  
- Integrate **map visualization** for location-based pricing  
- Enable **batch predictions** for multiple properties  
- Explore **other ML models** for better accuracy