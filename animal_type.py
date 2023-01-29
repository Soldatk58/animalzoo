import streamlit as st
import requests
import json
from PIL import Image
import pandas as pd
import urllib.request

def main():
    urllib.request.urlretrieve(‘https://github.com/Soldatk58/animalzoo/blob/main/icon.png?raw=true’, “foto1.png”) # Иконка сайта
    icon = Image.open('foto1.png')
    st.set_page_config(
        page_title='Animal Predict', # Название страницы
        page_icon=icon, # Иконка сайта
        layout='wide',
    )
    st.write("""
    # Классификация животных зоопарка
     """)
    st.write("""
    Прогнозируем по введенным данным, животное из зоопарка
     """)
    urllib.request.urlretrieve(‘https://github.com/Soldatk58/animalzoo/blob/main/zoo1.png?raw=true’, “foto2.png”)
    image = Image.open('foto2.png')
    st.image(image)
    st.sidebar.header('Заданные пользователем параметры')
    hair = st.sidebar.number_input('Есть ли волосы у животного (1 - да, 2 - нет)')
    feathers = st.sidebar.number_input('Есть ли перья у животного (1 - да, 2 - нет)')
    eggs = st.sidebar.number_input('Откладывает ли яйца животное (1 - да, 2 - нет)')
    milk = st.sidebar.number_input('Дает ли животное молоко (1 - да, 2 - нет)')
    airborne = st.sidebar.number_input('Умеет ли летать животное (1 - да, 2 - нет)')
    aquatic = st.sidebar.number_input('Умеет ли плавать животное (1 - да, 2 - нет)')
    predator = st.sidebar.number_input('Является ли животное хищником (1 - да, 2 - нет)')
    toothed = st.sidebar.number_input('Есть ли зубы у животного (1 - да, 2 - нет)')
    backbone = st.sidebar.number_input('Есть ли хребет у животного (1 - да, 2 - нет)')
    breathes = st.sidebar.number_input('Дышит ли животное воздухом (1 - да, 2 - нет)')
    venomous = st.sidebar.number_input('Ядовитое ли животное (1 - да, 2 - нет)')
    fins = st.sidebar.number_input('Есть ли плавники у животного (1 - да, 2 - нет)')
    legs = st.sidebar.number_input('Количество ног у животного')
    tail = st.sidebar.number_input('Есть ли у животного хвост (1 - да, 2 - нет)')
    domestic = st.sidebar.number_input('Домашнее ли это животное (1 - да, 2 - нет)')
    catsize = st.sidebar.number_input('Животное размером с кошку (1 - да, 2 - нет)')

    input_data = {
        'hair':hair,
        'feathers':feathers,
        'eggs':eggs,
        'milk':milk,
        'airborne':airborne,
        'aquatic':aquatic,
        'predator':predator,
        'toothed':toothed,
        'backbone':backbone,
        'breathes':breathes,
        'venomous':venomous,
        'fins':fins,
        'legs':legs,
        'tail':tail,
        'domestic':domestic,
        'catsize':catsize
    }

    input_data_rus = {
        'Волосы':hair,
        'Перья':feathers,
        'Яйца':eggs,
        'Молоко':milk,
        'Летает':airborne,
        'Плавает':aquatic,
        'Хищник':predator,
        'Зубы':toothed,
        'Хребет':backbone,
        'Воздух':breathes,
        'Ядовитое':venomous,
        'Плавники':fins,
        'Ноги':legs,
        'Хвост':tail,
        'Домашнее':domestic,
        'Размером с кошку':catsize
    }

    st.write('### Ваши данные')
    df = pd.DataFrame(input_data_rus, index=[0]) # Вывод пользовательских данных
    st.write(df)

    type = 0
    if st.button('Прогнозирование'):
        type = requests.post(url="http://127.0.0.1:8000/predict", data=json.dumps(input_data))
        type = type.json()
        t = type['prediction']
        t = round(t)
        list_class = {
            1:'Млекопитающее',
            2:'Птица',
            3:'Рептилия',
            4:'Рыба',
            5:'Амфибия',
            6:'Жук',
            7:'Беспозвоночный',
        }
        st.success(f'Модель машинного обучения, думает что это {list_class[t]}')

if __name__ == '__main__':
    main()        
