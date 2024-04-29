import streamlit as st
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

def run_graph () :
    adv = pd.read_csv('./data/advertising.csv')

    st.subheader('그래프 데이터 분석')
    st.text('TV,Newspaper,Radio 그래프 확인')

    radio_menu = ['TV','Newspaper','Radio']

    choice=st.radio('선택하세요',radio_menu)
    if choice == radio_menu [0] :
        fig, ax = plt.subplots()
        sb.regplot(x='TV', y='Sales', data=adv, ax=ax)

        st.pyplot(fig)

        st.text('각 광고마다 각각의 장단점')

    elif choice == radio_menu [1] :
        fig, ax = plt.subplots()
        sb.regplot(x='Newspaper', y='Sales', data=adv, ax=ax)

        st.pyplot(fig)


    elif choice == radio_menu [2] :
        fig, ax = plt.subplots()
        sb.regplot(x='Radio', y='Sales', data=adv, ax=ax)

        st.pyplot(fig)

    if choice == radio_menu [0] :
        st.write('장점 : 우상향 그래프로 투자하면 투자할수록 많은 판매량 확보 가능')
        st.write('단점 : 가성비가 좋지 않아 투자할때 큰 투자가 필요하다')
    elif choice == radio_menu [1] :
        st.write('장점 : 적은 물량으로 높은 투자율을 낼수있다')
        st.write('단점 : 높은 물량으로 전환시 투자수익율이 낮고 표본수가 적어져 투자하기 위험하다')
    elif choice == radio_menu [2] :
        st.write('장점 : 적은 물량으로 TV보다 높은 수익률을 낼수 있다') 
        st.write('단점 : 그래프 분포 폭이 넓어 잘못하다간 손해를 볼 우려가 있다')

    

