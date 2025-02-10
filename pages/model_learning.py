import streamlit as st
import model_sample.Random_Forest as rf
import model_sample.Decision_Tree as dt
import model_sample.KNN as knn
import model_sample.Logistic_Regression as lr
import model_sample.LightGBM as lgbm
import model_sample.XGBoost as xgb
import model_sample.Gradient_Boosting as gb


def show():
    # 세션 상태 초기화 (탭을 이동해도 데이터 유지)
    if "selected_tab" not in st.session_state:
        st.session_state.selected_tab = "Random Forest"

    # 🏷️ 서브 탭 생성 (선택 상태 유지)
    tab_names = ['Random Forest', 'Decision Tree', 'KNN', 'Logistic Regression', 'LightGBM', 'XGBoost', 'Gradient Boosting']

    # 세션 상태의 값이 tab_names에 없는 경우 기본값으로 설정
    if st.session_state.selected_tab not in tab_names:
        st.session_state.selected_tab = 'Random Forest'  # 유효하지 않으면 기본값으로 'Random Forest'

    selected_tab = st.radio("모델 선택", tab_names, index=tab_names.index(st.session_state.selected_tab), horizontal=True)

    st.session_state.selected_tab = selected_tab  # 선택한 탭을 세션 상태에 저장

    st.sidebar.empty()  # 사이드바 숨김

    # 선택된 탭의 내용을 실행
    if selected_tab == "Random Forest":
        st.header("Random Forest")
        rf.show()

    elif selected_tab == "Decision Tree":
        st.header("Decision Tree")
        dt.show()

    elif selected_tab == "KNN":
        st.header("KNN")
        knn.show()

    elif selected_tab == "Logistic Regression":
        st.header("Logistic Regression")
        lr.show()

    elif selected_tab == "LightGBM":
        st.header("LightGBM")
        lgbm.show()

    elif selected_tab == "XGBoost":
        st.header("XGBoost")
        xgb.show()

    elif selected_tab == "Gradient Boosting":
        st.header("Gradient Boosting")
        gb.show()