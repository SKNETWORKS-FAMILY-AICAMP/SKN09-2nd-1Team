import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import pages.introduce as itd
except ImportError as e:
    itd = None
    st.error(f"🚨 `model_learning` 모듈을 불러올 수 없습니다: {e}")

try:
    import pages.model_learning as ml
except ImportError as e:
    ml = None
    st.error(f"🚨 `model_learning` 모듈을 불러올 수 없습니다: {e}")

try:
    import pages.final_result as fr
except ImportError as e:
    fr = None
    st.error(f"🚨 `model_Interpretation` 모듈을 불러올 수 없습니다: {e}")

try:
    import pages.dataset as pdt
except ImportError as e:
    pdt = None
    st.error(f"🚨 `performance_evaluation` 모듈을 불러올 수 없습니다: {e}")


st.set_page_config(page_title="멀티 페이지 탭", layout="wide", initial_sidebar_state="collapsed")
st.title('인터넷 강의 수강생 이탈')

tab1, tab2, tab3, tab4 = st.tabs(["하늘이꺼", "모델 학습", "최종 결과", "결과 데이터"])
st.sidebar.empty()

with tab1:
    st.header("🧑하늘이꺼 페이지")
    if itd and hasattr(itd, "show"):
        itd.show()
    else:
        st.warning("⚠️ `model_learning.py`를 실행할 수 없습니다.")

with tab2:
    st.header("🧑‍💻 모델 학습 페이지")
    if ml and hasattr(ml, "show"):
        ml.show()
    else:
        st.warning("⚠️ `model_learning.py`를 실행할 수 없습니다.")

with tab3:
    st.header("📊 최종 결과 페이지")
    if fr and hasattr(fr, "show"):
        fr.show()
    else:
        st.warning("⚠️ `model_Interpretation.py`를 실행할 수 없습니다.")

with tab4:
    st.header("🔍 결과 데이터 페이지")
    if pdt and hasattr(pdt, "show"):
        pdt.show()
    else:
        st.warning("⚠️ `performance_evaluation.py`를 실행할 수 없습니다.")
    
