import streamlit as st
import time

st.title('Stalcraft Auction')
st.header('Полная база данных!')
user_input = st.text_input('Введите название предмета:')

if user_input:
    bar = st.progress(0)
    for i in range(11):
        time.sleep(0.3)
        bar.progress(i * 10)
    st.error('Нету нихуя!')
