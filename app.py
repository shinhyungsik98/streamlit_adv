import streamlit as st
from home import run_home
from eda import run_eda
from ml import run_ml
from graph import run_graph

def main() :
    st.title('TV,News,Radio 각각 광고로 판매량 예측하기')

    menu = ['Home','EDA','ML','graph']

    choice = st.sidebar.selectbox('메뉴',menu)

    if choice == menu[0]:
        run_home()
    elif choice == menu[1] :
        run_eda()
    elif choice == menu[2] :
        run_ml()
    elif choice == menu[3] :
        run_graph()



if __name__ == '__main__' :
    main()