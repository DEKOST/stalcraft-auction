import streamlit as st
import requests

url_demo_items = 'https://dapi.stalcraft.net/repos/EXBO-Studio/stalcraft-database/contents/ru/items/'
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwibmJmIjoxNjczNzk3ODM4LCJleHAiOjQ4MjczOTc4MzgsImlhdCI6MTY3Mzc5NzgzOCwianRpIjoiYXhwbzAzenJwZWxkMHY5dDgzdzc1N2x6ajl1MmdyeHVodXVlb2xsZ3M2dml1YjVva3NwZTJ3eGFrdjJ1eWZxaDU5ZDE2ZTNlN2FqdW16Z3gifQ.ZNSsvwAX72xT5BzLqqYABuH2FGbOlfiXMK5aYO1H5llG51ZjcPvOYBDRR4HUoPZVLFY8jyFUsEXNM7SYz8qL9ePmLjJl6pib8FEtqVPmf9ldXvKkbaaaSp4KkJzsIEMY_Z5PejB2Vr-q-cL13KPgnLGUaSW-2X_sHPN7VZJNMjRgjw4mPiRZTe4CEpQq0BEcPrG6OLtU5qlZ6mLDJBjN2xtK0DI6xgmYriw_5qW1mj1nqF_ewtUiQ1KTVhDgXnaNUdkGsggAGqyicTei0td6DTKtnl3noD5VkipWn_CwSqb2Mhm16I9BPfX_d5ARzWrnrwPRUf6PA_7LipNU6KkkW0mhZfmwEPTm_sXPus0mHPENoVZArdFT3L5sOYBcpqwvVIEtxRUTdcsKp-y-gSzao5muoyPVoCc2LEeHEWx0cIi9spsZ46SPRQpN4baVFp7y5rp5pjRsBKHQYUJ0lTmh1_vyfzOzbtNN2v6W_5w9JTLrN1U6fhmifvKHppFSEqD6DameL1TC59kpIdufRkEU9HE4O-ErEf1GuJFRx-Dew6XDvb_ExhvEqcw31yNvKzpVqLYJfLazqn6tUbVuAiPwpy6rP9tYO2taT1vj5TGn_vxwDu9zoLWe796tFMPS-kmbCglxB5C9L4EbpfWNbWxYjUkTvjT2Ml9OnrB0UbYo1jI'

def display_items(items):
    for item in items:
        st.write(f"  - {item['name']}")

st.title('Stalcraft Auction')
st.header('Полная база данных!')
user_input = st.text_input('Введите название предмета:')

if user_input:
    bar = st.progress(0)
    for i in range(11):
        time.sleep(0.3)
        bar.progress(i * 10)
    st.error('Нету нихуя!')

st.sidebar.write("Список категорий на RU сервере:")
response = requests.get(url_demo_items, headers={'Authorization': f'Bearer {access_token}'})
if response.status_code == 200:
    categories_data = response.json()
    categories = [item['name'] for item in categories_data if item['type'] == 'dir']
    for category in categories:
        is_expanded = st.checkbox(f"- {category}")
        if is_expanded:
            items_url = f"{url_demo_items}/{category}"
            items_response = requests.get(items_url, headers={'Authorization': f'Bearer {access_token}'})
            if items_response.status_code == 200:
                items_data = items_response.json()
                items = [item['name'] for item in items_data if item['type'] == 'file']
                display_items(items)