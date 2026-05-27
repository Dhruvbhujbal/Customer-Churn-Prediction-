import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score # ---> NEW IMPORT <---
import joblib

print("Starting model training process...")

# 1. Load the dataset
df = pd.read_csv('data/Telco-Customer-Churn.csv')

# 2. Clean the Data
print("Cleaning data...")
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(subset=['TotalCharges'], inplace=True)

selected_columns = [
    'tenure', 'MonthlyCharges', 'TotalCharges', 
    'Contract', 'InternetService', 'PaymentMethod', 'Churn'
]
df = df[selected_columns]

# ---> Convert Dollar amounts to Indian Rupees (₹) <---
conversion_rate = 83.0 
df['MonthlyCharges'] = df['MonthlyCharges'] * conversion_rate
df['TotalCharges'] = df['TotalCharges'] * conversion_rate

# 3. Separate Features (X) and Target (y)
X = df.drop('Churn', axis=1)
y = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)

# 4. Feature Engineering
print("Encoding and scaling features...")
X = pd.get_dummies(X, drop_first=True)

# Initialize and fit the scaler on numerical columns
scaler = StandardScaler()
numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
X[numerical_cols] = scaler.fit_transform(X[numerical_cols])

# 5. Split the Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 6. Train the Model
print("Training Random Forest model...")
rf_model = RandomForestClassifier(
    n_estimators=100, 
    random_state=42, 
    class_weight='balanced',
    max_depth=10
)
rf_model.fit(X_train, y_train)

# ---> NEW: Evaluate the Model <---
print("Evaluating model accuracy...")
y_pred = rf_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# 7. Export the Model and Scaler
print("Exporting brain to Flask...")
joblib.dump(rf_model, 'models/rf_churn_model.pkl')
joblib.dump(scaler, 'models/scaler.pkl')

# ---> UPDATED: Success message with accuracy <---
print(f"\n✅ Success! 'rf_churn_model.pkl' and 'scaler.pkl' are ready for your Flask app.")
print(f"📊 Model Accuracy on Test Data: {accuracy * 100:.2f}%")