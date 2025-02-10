import streamlit as st
import scores.accuracy as acc
import scores.precision as pc
import scores.recall as rc
import scores.f1_score as fs
import scores.all_data as ad

def show():

    # # 세션 상태 초기화 (탭을 이동해도 데이터 유지)
    # if "selected_tab" not in st.session_state:
    #     st.session_state.selected_tab = "Accuracy"  # 기본값은 Accuracy

    # # 🏷️ 서브 탭 생성 (선택 상태 유지)
    # tab_names = ['Accuracy', 'Precision', 'Recall', 'F1_score', 'All_Data']

    # # 'selected_tab'이 tab_names에 없는 경우, 기본값으로 설정
    # if st.session_state.selected_tab not in tab_names:
    #     st.session_state.selected_tab = "Accuracy"  # 기본값으로 설정

    # # 라디오 버튼 선택
    # selected_tab = st.radio("성능 선택", tab_names, index=tab_names.index(st.session_state.selected_tab), horizontal=True)

    # st.session_state.selected_tab = selected_tab  # 선택한 탭을 세션 상태에 저장

    # st.sidebar.empty()  # 사이드바 숨김


    # 세션 상태 초기화 (탭을 이동해도 데이터 유지)
    if "selected_tab" not in st.session_state:
        st.session_state.selected_tab = "Accuracy"  # 기본값은 Accuracy

    # 🏷️ 서브 탭 생성 (선택 상태 유지)
    sub_tab_names = ['Accuracy', 'Precision', 'Recall', 'F1_score', 'All_Data']

    # 'selected_tab'이 tab_names에 없는 경우, 기본값으로 설정
    if st.session_state.selected_tab not in sub_tab_names:
        st.session_state.selected_tab = "Accuracy"  # 기본값으로 설정

    # 라디오 버튼 선택
    selected_tab = st.radio("성능 선택", sub_tab_names, index=sub_tab_names.index(st.session_state.selected_tab), horizontal=True)

    # 선택한 탭을 세션 상태에 저장
    st.session_state.selected_tab = selected_tab

    st.sidebar.empty()  # 사이드바 숨김


    # 선택된 탭의 내용을 실행
    if selected_tab == "Accuracy":
        st.header("Accuracy")
        acc.show()

    elif selected_tab == "Precision":
        st.header("Precision")
        pc.show()

    elif selected_tab == "Recall":
        st.header("Recall")
        rc.show()

    elif selected_tab == "F1_score":
        st.header("F1_score")
        fs.show()

    elif selected_tab == "All_Data":
        st.header("All_Data")
        ad.show()