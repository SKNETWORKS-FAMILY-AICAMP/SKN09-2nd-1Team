import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, confusion_matrix, roc_curve
from lightgbm import LGBMClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

@st.cache_data
def load_data():
    return pd.read_csv('./data/merged_data_cleaned.csv')

def show():

    final_merged_data = load_data()

    sum_clicked_features = ['highest_education', 'imd_band', 'log_sum_click', 'log_studied_credits', 'scaled_score']
    mean_clicked_features = ['highest_education', 'imd_band', 'log_mean_click', 'log_studied_credits', 'scaled_score']


    data_option = st.radio("데이터 선택", ["Sum Click 기반", "Mean Click 기반", "All"])
    
    y = final_merged_data['final_result']

    if data_option == "Sum Click 기반":
        X = final_merged_data[sum_clicked_features]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42, stratify=y)
    elif data_option == "Mean Click 기반":
        X = final_merged_data[mean_clicked_features]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42, stratify=y)
    else:
        X_sum = final_merged_data[sum_clicked_features]
        X_mean = final_merged_data[mean_clicked_features]
        X_train_sum, X_test_sum, y_train, y_test = train_test_split(X_sum, y, test_size=0.1, random_state=42, stratify=y)
        X_train_mean, X_test_mean, _, _ = train_test_split(X_mean, y, test_size=0.1, random_state=42, stratify=y)  # y_train, y_test는 동일한 값 사용

    st.subheader("🔧 모델 선택 및 하이퍼파라미터 설정")


    st.markdown("""
    <style>
    .stSelectbox div[data-baseweb="select"] {
        background-color: #FFFFFF;  # 선택 박스 배경색 흰색
        color: #333333;  # 글자색은 검정으로 설정 (선택한 항목에 대한 가독성)
    }
    .stSelectbox div[data-baseweb="select"]:hover {
        background-color: #F0F0F0;  # hover 시 배경색 변경
    }
    .stSelectbox div[data-baseweb="select"] span {
        color: #333333;  # 드롭다운 항목의 글자색을 검정으로 설정
    }
    .stSelectbox div[data-baseweb="select"] div[data-focus="true"] {
        background-color: #FFFFFF;  # 선택된 항목의 배경을 흰색으로 설정
        color: #333333;  # 선택된 항목의 글자색 설정
    }
    </style>
    """, unsafe_allow_html=True)

    model_option = st.selectbox("사용할 모델을 선택하세요", 
                                ["Gradient Boosting", "Random Forest", "LightGBM", "XGBoost", "Logistic Regression", "KNN", "Decision Tree"])

    best_params = {
        "Gradient Boosting": {"n_estimators": 600, "learning_rate": 0.15, "max_depth": 9, "min_samples_split": 5, "min_samples_leaf": 1, "subsample": 0.9},
        "Random Forest": {"n_estimators": 300, "max_depth": 20, "min_samples_split": 5, "min_samples_leaf": 1},
        "LightGBM": {"n_estimators": 500, "learning_rate": 0.15, "max_depth": 5, "num_leaves": 31, "subsample": 0.7},
        "XGBoost": {"n_estimators": 200, "learning_rate": 0.15, "max_depth": 7},
        "Logistic Regression": {"C": 0.01},
        "KNN": {"n_neighbors": 5},
        "Decision Tree": {"max_depth": 10, "min_samples_split": 2}
    }

    param_choice = st.radio("하이퍼파라미터 설정", ["최적 파라미터 사용", "직접 입력"])
    params = best_params[model_option] if param_choice == "최적 파라미터 사용" else {}

    if param_choice == "직접 입력":
        if model_option in ["Gradient Boosting", "Random Forest", "LightGBM", "XGBoost"]:
            params["n_estimators"] = st.number_input("n_estimators", 50, 800, params.get("n_estimators", 600))
            params["learning_rate"] = st.number_input("learning_rate", 0.01, 0.3, params.get("learning_rate", 0.15))
            params["max_depth"] = st.number_input("max_depth", 3, 10, params.get("max_depth", 9))

        if model_option in ["Gradient Boosting", "Random Forest"]:
            params["min_samples_split"] = st.number_input("min_samples_split", 2, 10, params.get("min_samples_split", 5))
            params["min_samples_leaf"] = st.number_input("min_samples_leaf", 1, 10, params.get("min_samples_leaf", 1))

        if model_option == "KNN":
            params["n_neighbors"] = st.number_input("n_neighbors", 1, 20, params.get("n_neighbors", 5))

        if model_option == "Logistic Regression":
            params["C"] = st.number_input("Regularization Strength (C)", 0.001, 1.0, params.get("C", 0.01))

    model_classes = {
        "Gradient Boosting": GradientBoostingClassifier,
        "Random Forest": RandomForestClassifier,
        "LightGBM": LGBMClassifier,
        "XGBoost": XGBClassifier,
        "Logistic Regression": LogisticRegression,
        "KNN": KNeighborsClassifier,
        "Decision Tree": DecisionTreeClassifier
    }

    if st.button("모델 학습 및 평가 시작 🚀"):
        results = []

        def train_and_evaluate(X_train, X_test, dataset_name):
            model = model_classes[model_option](**params, random_state=42) if model_option != "KNN" else model_classes[model_option](**params)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            y_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else None

            acc = accuracy_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred, average='weighted')
            auc = roc_auc_score(y_test, y_proba) if y_proba is not None else "N/A"

            results.append([dataset_name, acc, f1, auc])

        if data_option == "All":
            train_and_evaluate(X_train_sum, X_test_sum, "Sum Click")
            train_and_evaluate(X_train_mean, X_test_mean, "Mean Click")
        else:
            train_and_evaluate(X_train, X_test, data_option)

        results_df = pd.DataFrame(results, columns=["Dataset", "Accuracy", "F1 Score", "AUC"])
        st.table(results_df.style.set_properties(**{'font-size': '14px', 'text-align': 'center'}))