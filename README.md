# 🏠 House Price Predictor

A simple Machine Learning project that predicts house prices based on real housing data.  
Built with **Python, scikit-learn, and Streamlit**, this app lets you adjust features like income, house age, rooms, and location — then instantly see a predicted price.

---

## 🚀 Live Demo
👉 [Try it here on Streamlit](https://your-app-link.streamlit.app)  
*(link will work after deployment)*

---

## 📂 Project Structure

house-price-predictor/ ├── app.py               # Streamlit app ├── house_price_model.pkl # Trained ML model ├── notebook.ipynb       # Model training notebook ├── requirements.txt     # Dependencies └── README.md            # Project description

---

## ⚙️ How It Works
1. **Dataset** → California Housing dataset (features like median income, house age, population, latitude/longitude).  
2. **Model** → Linear Regression trained to predict median house value.  
3. **Streamlit App** → Interactive sliders let you input values → model predicts price in USD.  

---

## 📊 Example Prediction
If you set:
- Median Income: 5 (=$50k)  
- House Age: 20 years  
- Average Rooms: 6  
- Population: 1000  
- Latitude: 35, Longitude: -120  

👉 Predicted price ≈ **$200,000 – $250,000**

---

## 🛠 Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Streamlit  
- Joblib  

---

## 🔮 Future Improvements
- Try advanced models (Random Forest, XGBoost).  
- Add better visualization for results.  
- Deploy with custom dataset options.  

---

## 👤 Author
**Sanyam Sood**  
 📂 [GitHub](https://github.com/s4nym)