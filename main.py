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
    import pages.degree_of_participation as dop
except ImportError as e:
    dop = None
    st.error(f"🚨 `performance_evaluation` 모듈을 불러올 수 없습니다: {e}")

try:
    import pages.dataset as pdt
except ImportError as e:
    pdt = None
    st.error(f"🚨 `performance_evaluation` 모듈을 불러올 수 없습니다: {e}")


st.set_page_config(page_title="멀티 페이지 탭", layout="wide", initial_sidebar_state="collapsed")
st.title('MOOC 학습 학생 이탈 예측')

tab1, tab2, tab3, tab4, tab5 = st.tabs(["소개", "모델 학습", "최종 결과", "참여도 예측", "결과 예측"])
st.sidebar.empty()

with tab1:
    st.header("🧑소개 페이지")
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
    st.header("🔍 참여도 페이지")
    if dop and hasattr(dop, "show"):
        dop.show()
    else:
        st.warning("⚠️ `performance_evaluation.py`를 실행할 수 없습니다.")

with tab5:
    st.header("🔍 결과 예측 페이지")
    if pdt and hasattr(pdt, "show"):
        pdt.show()
    else:
        st.warning("⚠️ `performance_evaluation.py`를 실행할 수 없습니다.")
    
