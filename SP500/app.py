#Libraries

import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yfinance as yf
from PIL import Image

#Head
image_url = "https://github.com/troncosofranco/Data-apps/blob/main/SP500/logo.jpg?raw=true"
st.image(image_url, use_column_width=True)

st.write('The S&P 500 is a stock index that tracks the performance of about 500 of the largest publicly listed U.S. companies, as measured by market capitalization. Because of its broad diversification, the S&P 500 is a standard performance benchmark for many stocks, mutual funds and ETFs, especially in the large-cap space')


st.subheader("Selected companies")
st.sidebar.header('Selection options')

# Web scraping of S&P 500 data
@st.cache
def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url, header = 0)
    df = html[0]
    return df

df = load_data()
sector = df.groupby('GICS Sector')

# Sidebar - Sector selection
sorted_sector_unique = sorted( df['GICS Sector'].unique()) #Sector selection
selected_sector = st.sidebar.multiselect('Sector', sorted_sector_unique, sorted_sector_unique)

# Filtering data
df_selected_sector = df[(df['GICS Sector'].isin(selected_sector))]

st.write("companies selected: " + str(df_selected_sector.shape[0]))
st.dataframe(df_selected_sector) #display dataframe

# Download S&P500 data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_sector), unsafe_allow_html=True)

# https://pypi.org/project/yfinance/
#get financial data accordingo to ticket




data = yf.download(
        tickers = list(df_selected_sector[:10].Symbol),
        period = "ytd",
        interval = "1d",
        group_by = 'ticker',
        auto_adjust = True,
        prepost = True,
        threads = True,
        proxy = None
    )

# Plot Closing Price of Query Symbol
def price_plot(symbol):
  df = pd.DataFrame(data[symbol].Close)
  df['Date'] = df.index
  plt.fill_between(df.Date, df.Close, color='skyblue', alpha=0.3)
  plt.plot(df.Date, df.Close, color='skyblue', alpha=0.8)
  plt.xticks(rotation=90)
  plt.title(symbol, fontweight='bold')
  plt.xlabel('Date', fontweight='bold')
  plt.ylabel('Closing Price', fontweight='bold')
  return st.pyplot()

#Density function
def density_plot(symbol):
  df = pd.DataFrame(data[symbol].Close)
  df['Date'] = df.index
  fig, ax = plt.subplots(figsize=(15, 7))
  sns.distplot(df['Close'], ax=ax)
  return st.pyplot()

#Boxplot function
def box_plot(symbol):
  df = pd.DataFrame(data[symbol].Close)
  df['Date'] = df.index
  df['Month'] = df['Date'].dt.month #daily data to monthly data
  ax = sns.boxplot(x=df.Month, y=df.Close, data=df) 
  ax = sns.stripplot(x=df.Month, y=df.Close, data=df, color="orange", jitter=0.2, size=2.5)
  
  plt.title(symbol, fontweight='bold')
  plt.xlabel('Month', fontweight='bold')
  plt.ylabel('Closing Price', fontweight='bold')  
  st.set_option('deprecation.showPyplotGlobalUse', False)
  return st.pyplot()

num_company = st.sidebar.slider('Number of Top Companies', 1, 5)

if st.button('Close Price'):
    st.header('Stock Closing Price')
    for i in list(df_selected_sector.Symbol)[:num_company]:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        price_plot(i)

if st.button('Density'):
    st.header('Density Function')
    for i in list(df_selected_sector.Symbol)[:num_company]:
        st.set_option('deprecation.showPyplotGlobalUse', False)
        density_plot(i)

if st.button('BoxPlot'):
    st.header('Boxplot')
    for i in list(df_selected_sector.Symbol)[:num_company]:
        box_plot(i)


st.write("---")
st.markdown("""
Credits:
* **Image:** [Freepik] (https://www.freepik.es/foto-gratis/tableta-capital-rascacielos-pantalla-intercambio_1088871.htm#query=wall%20street&position=0&from_view=search)
* **Data source:** [pro-football-reference.com](https://www.pro-football-reference.com/).
* **Code Reference:** [Dataprofessor](https://github.com/dataprofessor/streamlit_freecodecamp/tree/main/app_5_eda_sp500_stock)
""")

