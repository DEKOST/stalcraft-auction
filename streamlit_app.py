# Import convention
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
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

# Just add it after st.sidebar:
a = st.sidebar.radio('Укажите регион:',['EN','RU'])
