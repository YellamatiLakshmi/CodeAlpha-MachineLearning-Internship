# 🏦 Credit Scoring Model

## 📌 Project Overview
This project predicts whether an individual is **creditworthy** based on their financial and demographic data.  
It uses **Machine Learning (XGBoost) and Flask** to provide an API for credit risk prediction.

## 🔹 Technologies Used
- **Machine Learning:** XGBoost, SMOTE for data balancing
- **Web API:** Flask
- **Libraries:** Scikit-learn, Pandas, NumPy

## 🔹 Installation
1. **Clone the repository**  
   ```sh
   git clone https://github.com/your-username/CodeAlpha_Credit_Scoring.git
   cd CodeAlpha_Credit_Scoring
   ```

2. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

3. **Train the Model** (Optional)  
   ```sh
   python credit_scoring.py
   ```

4. **Run the Flask API**  
   ```sh
   python app.py
   ```

## 🔹 API Usage (Postman or cURL)
### **Endpoint:**
   ```sh
   POST http://127.0.0.1:5000/predict
   ```

### **Sample JSON Request:**
```json
[
    {
        "Age": 30,
        "Sex": 1,
        "Job": 2,
        "Housing": 1,
        "Saving accounts": 2,
        "Checking account": 1,
        "Credit amount": 5000,
        "Duration": 24,
        "Purpose": 3
    }
]
```

### **Expected Response:**
```json
{"Credit Risk": [1]}
```
- `1` → Creditworthy  
- `0` → Not Creditworthy  
```

