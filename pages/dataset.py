import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    model_results = pd.read_csv('./data/model_results.csv')
    student_info = pd.read_csv('./data/studentInfo.csv')
    return model_results, student_info

def get_intervention_suggestions(student):
    suggestions = []

    if student['highest_education'] in ["Lower Than A Level"]:
        suggestions.append("개별 학습 튜터링 제공")
        suggestions.append("학습 가이드 및 학습 플래너 제공")

    if student['imd_band'] in ["50-60%", "60-70%", "70-80%", "80-90%", "90-100%"]:
        suggestions.append("장학금 & 학비 지원 안내")
        suggestions.append("온라인 무료 학습 자료 제공")

    if student['studied_credits'] <= 100:
        suggestions.append("과목 부담이 높은 학생은 적정 학점 유지")
        suggestions.append("학점 부담이 큰 학생 대상 학점 관리 컨설팅 제공")
    
    return suggestions

# Streamlit UI
def show():
    st.write("#### ▶  학생 이탈 예측 및 맞춤 지원 시스템")

    model_results, student_info = load_data()

    st.markdown("""
    <style>
        /* 텍스트 입력 박스 스타일 */
        .stTextInput>div>div>input {
            background-color: #FFEEEE !important;  /* 연한 핑크 배경 */
            color: #000000 !important;            /* 진한 검정색 글자 */
            border: 2px solid #FF1493 !important; /* 진한 핑크 테두리 */
            border-radius: 8px;                   /* 모서리 둥글게 */
            padding: 8px;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

    student_id = st.text_input("Enter Student ID:", "")

    models = [
        "Random Forest", "Gradient Boosting", "Decision Tree", 
        "KNN", "XGBoost", "LightGBM", "Logistic Regression"
    ]
    
    cols_model = st.columns(7)
    selected_models = []
    for i, model in enumerate(models):
        if cols_model[i].checkbox(model, key=model):
            selected_models.append(model)

    cols_sum_mean = st.columns(2)
    show_sum = cols_sum_mean[0].checkbox("Show Sum Data", value=True)
    show_mean = cols_sum_mean[1].checkbox("Show Mean Data", value=True)

    if student_id:
        filtered_df = model_results[model_results['Student_ID'].astype(str) == student_id]
        filtered_info = student_info[student_info['id_student'].astype(str) == student_id]

        if not filtered_df.empty:
            st.write("### 📋 학생 정보")
            st.dataframe(filtered_info)

            result_df = filtered_df[["Student_ID"]]  
            withdrawn_count = 0
            active_count = 0

            for model in selected_models:
                if show_sum:
                    sum_col = f"{model} (sum)"
                    result_df[sum_col] = filtered_df[sum_col]  
                    if filtered_df[sum_col].values[0] == "Withdrawn":
                        withdrawn_count += 1
                    elif filtered_df[sum_col].values[0] == "Active":
                        active_count += 1

                if show_mean:
                    mean_col = f"{model} (mean)"
                    result_df[mean_col] = filtered_df[mean_col]  
                    if filtered_df[mean_col].values[0] == "Withdrawn":
                        withdrawn_count += 1
                    elif filtered_df[mean_col].values[0] == "Active":
                        active_count += 1

            st.write("### 🔍 예측 결과 분석 📊")
            st.dataframe(result_df)  

            if withdrawn_count > active_count:
                st.write("🔴 **대부분의 모델이 Withdrawn(이탈)로 예측했습니다.**\n\n")

                student = filtered_info.iloc[0]
                interventions = get_intervention_suggestions(student)

                if interventions:
                    st.write("##### 🚀 맞춤형 지원 방안")
                    for suggestion in interventions:
                        st.write(f"- {suggestion}")
                else:
                    st.write("✅ 해당 학생은 추가 지원이 필요하지 않습니다.")


            elif active_count > withdrawn_count:
                st.write("🟢 **대부분의 모델이 Active(유지)로 예측했습니다.**")

            # else:
            #     st.write("⚖️ **Withdrawn과 Active가 비슷한 비율로 예측되었습니다.**")

        else:
            st.warning("⚠️ No matching Student ID found in model results.")


    st.header("📊 전체 결과 데이터")
    st.dataframe(model_results)  
