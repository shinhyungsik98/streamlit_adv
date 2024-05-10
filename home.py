import streamlit as st

def run_home () :
    st.image('./image/tv.png')
    st.text('링크주소')
    kaggle_link = "[Kaggle advertising index](https://www.kaggle.com/datasets/yasserh/advertising-sales-dataset/data)"
    st.markdown(kaggle_link, unsafe_allow_html=True)
    st.subheader('TV,News,Radio 들의 광고금액데이터를 분석하고 예측합니다')

    st.subheader('설명')
    st.text('광고 데이터 세트는 라디오, TV, 신문과 같은 여러 채널에서 광고 비용과 관련하여 생성된 판매 수익을 포착합니다.')
    st.text('광고 예산이 전체 매출에 미치는 영향을 이해하는 것이 필요합니다.')


    st.subheader('핵심내용')
    st.text('데이터는 캐글에 있는 advertising.csv 파일을 사용했습니다.')

    st.text('탐색적 데이터 분석과 광고로 인한 판매량을 예측하는 앱입니다.')

    st.text('히스토그램, 산점도, 박스플롯 를 활용해 어떤 관계가 나타나는지 확인가능합니다.')

    st.text('단일 및 다중 기능에 대한 매출을 예측하는 회귀 모델을 구축합니다.')

    st.text('최종 모델의 mse점수는 4.48이며 정확한 예측을 할수 있는 능력을 보여줍니다.')
