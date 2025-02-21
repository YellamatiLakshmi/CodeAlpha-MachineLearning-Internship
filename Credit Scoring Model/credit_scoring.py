import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE
import joblib
from xgboost import XGBClassifier

# Step 1: Load Dataset
# Dataset used in this model " german_credit_data_updated.csv "
df = pd.read_csv("german_credit_data_updated.csv")  # Change to your dataset

# Step 2: Data Preprocessing
# Convert categorical variables into numeric using Label Encoding
label_enc = LabelEncoder()
df['Sex'] = label_enc.fit_transform(df['Sex'])
df['Housing'] = label_enc.fit_transform(df['Housing'])
df['Saving accounts'] = label_enc.fit_transform(df['Saving accounts'].astype(str))
df['Checking account'] = label_enc.fit_transform(df['Checking account'].astype(str))
df['Purpose'] = label_enc.fit_transform(df['Purpose'])

# Convert Credit Risk column to binary (1 = Creditworthy, 0 = Not Creditworthy)
df['Credit Risk'] = df['Credit Risk'].map({1: 1, 2: 0})

X = df.drop(columns=['Credit Risk', 'Unnamed: 0'])  # Features
y = df['Credit Risk']  # Target variable

# Step 3: Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Handle Class Imbalance using SMOTE
smote = SMOTE(random_state=42)
X_train, y_train = smote.fit_resample(X_train, y_train)

# Step 5: Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 6: Model Training with XGBoost
xgb_model = XGBClassifier(n_estimators=200, learning_rate=0.05, max_depth=6, random_state=42)
xgb_model.fit(X_train, y_train)

# Step 7: Hyperparameter Tuning
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [6, 10, None],
    'learning_rate': [0.01, 0.05, 0.1]
}

grid_search = GridSearchCV(XGBClassifier(random_state=42), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

# Step 8: Evaluation
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
print(f"Improved Accuracy: {accuracy}")
print("Classification Report:\n", report)

# Step 9: Save the optimized model
joblib.dump(best_model, "credit_scoring_model_optimized.pkl")
print("Optimized model saved as credit_scoring_model_optimized.pkl")
