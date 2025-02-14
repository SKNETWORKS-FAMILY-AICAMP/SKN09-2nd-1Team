import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import platform

def show():
    def set_korean_font():
        system_name = platform.system()
        if system_name == "Windows":
            plt.rc("font", family="Malgun Gothic")
        elif system_name == "Darwin":
            plt.rc("font", family="AppleGothic")
        else:  # Linux
            plt.rc("font", family="NanumGothic")
        plt.rcParams["axes.unicode_minus"] = False

    set_korean_font()

    @st.cache_data
    def load_data():
        return pd.read_csv('./data/merged_data_cleaned.csv')

    final_merged_data = load_data()


    features = ['sum_click', 'mean_click']
    target = 'final_result'

    X = final_merged_data[features]
    y = final_merged_data[target]


    smote = SMOTE(sampling_strategy='auto', random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X, y)

  
    X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.1, random_state=42, stratify=y_resampled)


    dt_model = DecisionTreeClassifier(max_depth=10, random_state=42)
    dt_model.fit(X_train, y_train)

    st.info("본 프로젝트는 학습자의 참여도를 학습 자료 클릭 수(sum_click) 기반으로 분석하여 이탈 가능성을 예측하였습니다.")

    st.subheader("🔢 예측할 학생의 참여 수 입력")
    click_type = st.radio("입력 방식 선택", ["총 참여 수 (Sum Click)", "평균 참여 수 (Mean Click)"])

    if click_type == "총 참여 수 (Sum Click)":
        user_click = st.number_input("참여도(클릭 수) 입력", min_value=0, max_value=28615, value=1000)
        input_data = np.array([[user_click, X.mean()['mean_click']]])
    else:
        user_click = st.number_input("평균 참여 수 입력", min_value=0.0, max_value=19.42, value=5.0)
        input_data = np.array([[X.mean()['sum_click'], user_click]])


    if st.button("이탈 예측 🚀"):
        prediction = dt_model.predict(input_data)[0]
        probability = dt_model.predict_proba(input_data)[0]

        st.subheader("📌 예측 결과")
        st.write(f"이탈 예측 값: **{'이탈' if prediction == 0 else '유지'}**")
        st.write(f"이탈 확률: **{probability[0] * 100:.2f}%**, 유지 확률: **{probability[1] * 100:.2f}%**")

        labels = ["이탈 (Withdrawn)", "유지 (Not Withdrawn)"]
        colors = ['red', 'green']
        sizes = [probability[0] * 100, probability[1] * 100]
        explode = (0.1, 0)

        fig, ax = plt.subplots(figsize=(5, 5))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90, explode=explode, shadow=True, wedgeprops={'edgecolor': 'black'})
        ax.set_title("이탈 예측 확률", fontsize=14)

        st.pyplot(fig)
