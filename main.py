import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
from random import randint


st.title("Визуализация исселдования по чаевым")
tips_df = st.sidebar.file_uploader(
    '**Загурзите датасет tips.csv**', type='csv')

if tips_df is not None:
    df = pd.read_csv(tips_df)
    st.write(df.head(5))
else:
    st.stop()

st.divider()

df['time_order'] = [datetime.date(2023, 1, randint(1, 31))
                    for i in range(len(df))]

st.subheader('1. Динамика чаевых')
g1 = sns.relplot(data=df, kind='line', x='time_order', y='tip', height=4.5, aspect=2.3).set(
    xlabel='Даты', ylabel='Чаевые')
st.pyplot(g1)
if st.sidebar.button('Загрузить график 1'):
    g1.savefig('g1.png')

st.divider()

st.subheader('2. Гистограмма по размеру счета')
g2 = sns.displot(data=df, x='total_bill', kind='hist', height=4, aspect=2). set(
    xlabel='Размер счета', ylabel='Количество чеков')
st.pyplot(g2)
if st.sidebar.button('Загрузить график 2'):
    g2.savefig('gr2.png')
st.divider()

st.subheader('3. Зависимость между размером счета и размером чаевых')
g3 = sns.relplot(data=df, x='total_bill', y='tip', color='g',
                 kind='scatter', aspect=1.25).set(xlabel='Размер счета', ylabel='Чаевые')
st.pyplot(g3)
if st.sidebar.button('Загрузить график 3'):
    g3.savefig('gr3.png')
st.divider()
st.subheader('4. Чаевые в зависимости от размера счета и количества людей')
g4 = sns.relplot(data=df, x='total_bill', y='tip', hue='size', size='size',
                 kind='scatter').set(xlabel='Размер счета', ylabel='Чаевые')
st.pyplot(g4)
if st.sidebar.button('Загрузить график 4'):
    g4.savefig('gr4.png')
st.divider()
st.subheader('5. Зависимость между днем недели и размером счета')
g5 = sns.relplot(kind='scatter', data=df, x='day', y='total_bill').set(
    xlabel='День', ylabel='Сумма счета')
st.pyplot(g5)
if st.sidebar.button('Загрузить график 5'):
    g5.savefig('gr5.png')
st.divider()
st.subheader(
    '6. Зависимость между днем недели и размером чаевых с разбивкой по полу')
g6 = sns.relplot(data=df, x='tip', y='day', hue='sex', kind='scatter').set(
    ylabel='День недели', xlabel='Чаевые')
st.pyplot(g6)
if st.sidebar.button('Загрузить график 6'):
    g6.savefig('gr6.png')
st.divider()
st.subheader('7. Показатели размера счета с разбивкой по времени')
g7 = sns.catplot(data=df, x='day', y='total_bill', hue='time', kind='box').set(
    xlabel='День недели', ylabel='Размер счета')
st.pyplot(g7)
if st.sidebar.button('Загрузить график 7'):
    g7.savefig('gr7.png')
st.divider()
st.subheader('8. Гистограмма чаевых на обед и ужин')
g8 = sns.displot(data=df, x='tip', col='time', kind='hist').set(
    xlabel='Чаевые', ylabel='Склько раз встречаются')
st.pyplot(g8)
if st.sidebar.button('Загрузить график 8'):
    g8.savefig('gr8.png')
st.divider()
st.subheader(
    '9. Связь размера счета и чаевых с разбивкой по курящим/некурящим ')
g9 = sns.relplot(data=df, x='total_bill', y='tip', col='sex',
                 hue='smoker').set(xlabel='Размер счета', ylabel='Чаевые')
st.pyplot(g9)
if st.sidebar.button('Загрузить график 9'):
    g9.savefig('gr9.png')
st.divider()

st.subheader('10. Тепловая карта зависимости численных переменных')
fig, ax = plt.subplots(figsize=(10, 6))
tips_corr = df.corr(method='pearson', numeric_only=True)
sns.heatmap(tips_corr, annot=True, cmap='icefire')
st.pyplot(fig)
if st.sidebar.button('Загрузить график 10'):
    fig.savefig('gr10.png')
