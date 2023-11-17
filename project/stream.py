import pandas as pd 
import numpy as np
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title = 'betting dashboard',
                   page_icon = ':bar_chart:',
                   layout = 'wide'
)

df = pd.read_excel(
    io = 'df.xlsx',
    engine =  'openpyxl',
    sheet_name = 'Sheet1',
    skiprows = 0,
    usecols = 'C:AG',
    nrows = 2566
)

#  ------ SIDEBAR -----
st.sidebar.header("Please Filter Here:")

year = st.sidebar.multiselect(
    "select the year:",
    options = df["Year"].unique(),
    default= df["Year"].unique()
)

week = st.sidebar.multiselect(
    "select the week:",
    options = df["week"].unique(),
    default= df["week"].unique()
)

df_selection = df.query(
    "Year == @year & week == @week"
)

st.dataframe(df_selection)

# ----MAINPAGE ------

fig, axs = plt.subplots(2, 2, figsize=(7, 7))
a = sns.countplot(data = df, x = 'O_win_3', color="skyblue", ax=axs[0, 0])
b =sns.countplot(data = df, x = 'Wu_win_3', color="olive", ax=axs[0, 1])
c = sns.countplot(data = df, x = 'O_win_5', color="gold", ax=axs[1, 0])
d = sns.countplot(data = df, x = 'Wu_win_5', color="teal", ax=axs[1, 1])

st.pyplot(a.get_figure())  


