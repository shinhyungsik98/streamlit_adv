import streamlit as st

def run_home () :
    st.subheader('TV,News,Radio 들의 광고금액데이터를 분석하고 예측합니다')
    st.text('데이터는 캐글에 있는 advertising.csv 파일을 사용했습니다')
    st.text('탐색적 데이터 분석과 광고로 인한 판매량을 예측하는 앱입니다')
    st.text('히스토그램과 산점도를 활용해 어떤 관계가 나타나는지 확인가능합니다.')