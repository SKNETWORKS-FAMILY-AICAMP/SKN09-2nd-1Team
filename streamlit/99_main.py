import streamlit as st
import sys
import os

# ✅ 현재 디렉토리를 `sys.path`에 추가 (모듈 인식 문제 해결)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# ✅ 개별 페이지 모듈 불러오기 (오류 발생 시 예외 처리)
try:
    import pages.model_learning as ml
except ImportError as e:
    ml = None
    st.error(f"🚨 `model_learning` 모듈을 불러올 수 없습니다: {e}")

try:
    import pages.performance_evaluation as pe
except ImportError as e:
    pe = None
    st.error(f"🚨 `performance_evaluation` 모듈을 불러올 수 없습니다: {e}")

try:
    import pages.model_Interpretation as mi
except ImportError as e:
    mi = None
    st.error(f"🚨 `model_Interpretation` 모듈을 불러올 수 없습니다: {e}")

# ✅ Streamlit 페이지 설정
st.set_page_config(page_title="멀티 페이지 탭", layout="wide", initial_sidebar_state="collapsed")
st.title('인터넷 강의 수강생 이탈')

# 🏷️ 탭 생성
tab1, tab2, tab3 = st.tabs(["모델 학습", "성과 평가", "모델 해석"])
st.sidebar.empty()  # 사이드바 숨김

# ✅ 각 탭에서 해당 모듈 실행 (오류 발생 시 안전하게 처리)
with tab1:
    st.header("🧑‍💻 모델 학습 페이지")
    if ml and hasattr(ml, "show"):
        ml.show()
    else:
        st.warning("⚠️ `model_learning.py`를 실행할 수 없습니다.")

with tab2:
    st.header("📊 성과 평가 페이지")
    if pe and hasattr(pe, "show"):
        pe.show()
    else:
        st.warning("⚠️ `performance_evaluation.py`를 실행할 수 없습니다.")

with tab3:
    st.header("🔍 모델 해석 페이지")
    if mi and hasattr(mi, "show"):
        mi.show()
    else:
        st.warning("⚠️ `model_Interpretation.py`를 실행할 수 없습니다.")
