import streamlit as st
import joblib
import numpy as np

def run_ml() :
    st.subheader('TV,Newspaper,Radio 광고 금액으로 판매량 예측하기')

    st.text('TV 광고금액을 입력하시오')
    TV_ad=st.number_input('금액 입력(단위:백 만원)', min_value=1, max_value=297,value=100,step=5)

    st.text('Radio 광고금액을 입력하시오')
    radio_ad =st.number_input('금액 입력(단위:백 만원)', min_value=0,max_value=50,value=20,step=5)

    st.text('Newspaper 광고금액을 입력하시오')
    news_ad = st.number_input('금액입력(단위:백 만원)', min_value=0, max_value=114,value=40,step=5)

    st.subheader('버튼을 누르면 예측합니다')

    if st.button('예측하기') :

        regressor = joblib.load('./model/regressor.pkl')

        new_data = [TV_ad,radio_ad,news_ad]

        np.array(new_data).reshape(1,-1)

        new_data = np.array(new_data).reshape(1,-1)

        y_pred = regressor.predict(new_data)


        y_pred=y_pred[0]
        print(y_pred)
        #2.숫자의 소수점 뒤 제거
        y_pred = round(y_pred,3)
        print(y_pred)

        

        st.write(f'광고로 인하여 팔린 물품갯수는 {int(y_pred * 1000)} 개 입니다.')



        


