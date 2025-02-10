import streamlit as st
import pages.model_learning as ml
import pages.performance_evaluation as pe
import pages.model_Interpretation as mi

#def show():
st.set_page_config(page_title="멀티 페이지 탭", layout="wide", initial_sidebar_state="collapsed")
st.title('인터넷 강의 수강생 이탈')
# 🏷️ 탭 생성
tab1, tab2, tab3 = st.tabs(["모델 학습", "성과 평가", "모델 해석"])
st.sidebar.empty()  # 사이드바 숨김
with tab1:
    st.header("🧑‍💻 모델 학습 페이지")
    ml.show()
with tab2:
    st.header("📊 성과 평가 페이지")
    pe.show()
    
with tab3:
    st.header("🔍 모델 해석 페이지")
    mi.show()


# show()
    
