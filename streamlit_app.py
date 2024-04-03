import streamlit as st
import requests
import time
import json

st.title('Stalcraft Auction')
st.header('Полная база данных!')
user_input = st.text_input('Введите название предмета:')

if user_input:
    bar = st.progress(0)
    time_sleep = random.randint(1, 10)
    for i in range(11):
        time.sleep(time_sleep)
        bar.progress(i * 10)
    st.error('Нету нихуя!')
