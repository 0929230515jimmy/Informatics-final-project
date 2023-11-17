import pandas as pd 
import numpy as np
import plotly.express as px
import streamlit as st
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

plot1 = sns.countplot(data = df, x = 'O_win_3', color="skyblue", order=df['O_win_3'].value_counts().index)
plot2 = sns.countplot(data = df, x = 'Wu_win_3', color="olive")
plot3 = sns.countplot(data = df, x = 'O_win_5', color="gold")
plot4 = sns.countplot(data = df, x = 'Wu_win_5', color="teal")

st.pyplot(plot1.get_figure())


