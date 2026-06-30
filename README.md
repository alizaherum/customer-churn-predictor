Customer Churn Predictor
This is an end-to-end machine learning project that predicts whether a telecom customer is likely to churn. It uses the Telco Customer Churn dataset with 7,043 customers and 21 features. The problem is framed as a binary classification task, and Recall was prioritized as the key metric since missing a churner is more costly than a false alarm.
The ML pipeline was built using scikit-learn's Pipeline and ColumnTransformer, with StandardScaler applied to numerical features and OneHotEncoder for categorical ones. Three models were trained and tracked using MLflow: Logistic Regression (recall: 0.52), Random Forest (recall: 0.45), and XGBoost (recall: 0.64). XGBoost with scale_pos_weight=2.77 to handle class imbalance performed best and was selected for deployment. SHAP TreeExplainer was used to interpret predictions, revealing that month-to-month contracts, shorter tenure, and higher monthly charges are the strongest predictors of churn.
The trained model is served via a FastAPI backend and an interactive Streamlit frontend where users can input customer details and get a real-time churn probability. Both services are containerized using Docker and managed with Docker Compose, making the app fully portable and reproducible on any machine.
To run locally:
bashgit clone https://github.com/your-username/customer-churn-predictor.git
cd customer-churn-predictor
docker-compose up --build
FastAPI runs at http://localhost:8000 and Streamlit at http://localhost:8501.
Dataset: Telco Customer Churn — Kaggle
Author: Alizah Erum
