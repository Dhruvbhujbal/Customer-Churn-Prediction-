from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the model and scaler
model = joblib.load('models/rf_churn_model.pkl')
scaler = joblib.load('models/scaler.pkl')

@app.route('/')
def home():
    # This serves the HTML file
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # 1. Get the JSON data sent from JavaScript
    user_input = request.json
    
    # 2. Auto-calculate TotalCharges
    tenure = float(user_input['tenure'])
    monthly_charges = float(user_input['monthly_charges'])
    total_charges = tenure * monthly_charges

    # 3. Format the data EXACTLY how the model was trained
    data = {
        'tenure': tenure,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,
        'Contract_One year': 1 if user_input['contract'] == "One year" else 0,
        'Contract_Two year': 1 if user_input['contract'] == "Two year" else 0,
        'InternetService_Fiber optic': 1 if user_input['internet_service'] == "Fiber optic" else 0,
        'InternetService_No': 1 if user_input['internet_service'] == "No" else 0,
        'PaymentMethod_Credit card (automatic)': 1 if user_input['payment_method'] == "Credit card (automatic)" else 0,
        'PaymentMethod_Electronic check': 1 if user_input['payment_method'] == "Electronic check" else 0,
        'PaymentMethod_Mailed check': 1 if user_input['payment_method'] == "Mailed check" else 0
    }
    
    # 4. Convert to DataFrame and Scale the numerical columns
    df = pd.DataFrame(data, index=[0])
    df[['tenure', 'MonthlyCharges', 'TotalCharges']] = scaler.transform(df[['tenure', 'MonthlyCharges', 'TotalCharges']])
    
    # 5. Make the Prediction
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1] * 100
    
    # 6. Send the result back to the frontend
    result = {
        "churn_risk": int(prediction), # 1 = Yes, 0 = No
        "probability": round(probability, 2)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)