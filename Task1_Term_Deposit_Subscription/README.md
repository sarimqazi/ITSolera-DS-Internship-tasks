# Task 1: Term Deposit Subscription Prediction (Bank Marketing)

## Task objective
To build a machine learning model that predicts whether a customer will churn (leave) or not, and interpret model predictions using SHAP.

## Approach

1️⃣ Data Preprocessing

. Removed irrelevant columns
. Handled missing values
. Encoded categorical features:
. Label Encoding (binary features)
. One-Hot Encoding (multi-class features)
. Applied feature scaling where required

2️⃣ Model Development

Trained and compared the following models:
1) Logistic Regression
2) Random Forest Classifier
3) XGBoost Classifier

🔍 Model Interpretability (SHAP Analysis)

To understand model decisions, SHAP was used:
 Global Interpretation
2) SHAP Beeswarm Plot showed most influential features.
3) Identified top churn drivers.
 Local Interpretation
5) SHAP Waterfall Plot explained individual customer predictions.
6) Helped understand why a specific customer is predicted to churn.

📊 Key Findings

1) Customers with short tenure are more likely to churn.
2) Month-to-month contracts significantly increase churn risk.
3) Higher monthly charges correlate with churn probability.
4) Long-term contracts reduce churn likelihood.