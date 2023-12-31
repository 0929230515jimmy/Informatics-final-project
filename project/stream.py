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



#-----import data------

df = pd.read_excel(
    io = 'https://github.com/0929230515jimmy/Informatics-final-project/blob/main/project/df.xlsx?raw=True',
    engine =  'openpyxl',
    sheet_name = 'Sheet1',
    skiprows = 0,
    usecols = 'C:H,J,AD:AG',
    nrows = 2566
)

team = pd.read_excel('https://github.com/0929230515jimmy/Informatics-final-project/blob/main/project/team.xlsx?raw=True')
team2 = pd.read_excel('https://github.com/0929230515jimmy/Informatics-final-project/blob/main/project/team2.xlsx?raw=True')

current = pd.read_excel('https://github.com/0929230515jimmy/Informatics-final-project/blob/main/project/current.xlsx?raw=True')
current = current[["Week", "Home Team", "Away Team", "Spread", "my_pick", "my_pick3", "my_pick5"]]

df = df.merge(team, on='Away team', how='left')
df = df.merge(team2, on='Home team', how='left')

df = df[["Home", "Away", "Year", "week", "Awayscore", "Homescore", "Spread", "O_win_3", "Wu_win_3", "O_win_5", "Wu_win_5"]]

#  ------ SIDEBAR -----
st.sidebar.header("Please Filter Here:")
week = st.sidebar.multiselect(
    "select the week:",
    options = current["Week"].unique(),
)

team = st.sidebar.multiselect(
    "select the Home team:",
    options = current["Home Team"].unique(),
)

df_selection = current.query(
    "Week == @week and `Home Team` == @team"
)



# ---- 2023data ------
st.title(":bar_chart: 2023 week14 & week15 Pick")
st.dataframe(df_selection)

#----percentage----
O3_win = 0
O3_lose = 0
for i in range (2566):
    if df.loc[i, 'O_win_3'] == 'W':
        O3_win += 1
    elif df.loc[i, 'O_win_3'] == 'L':
        O3_lose += 1
O3_percentage = round((O3_win)/(O3_win+O3_lose),3)

W3_win = 0
W3_lose = 0
for i in range (2566):
    if df.loc[i, 'Wu_win_3'] == 'W':
        W3_win += 1
    elif df.loc[i, 'Wu_win_3'] == 'L':
        W3_lose += 1
W3_percentage = round((W3_win)/(W3_win+W3_lose),3)

O5_win = 0
O5_lose = 0
for i in range (2566):
    if df.loc[i, 'O_win_5'] == 'W':
        O5_win += 1
    elif df.loc[i, 'O_win_5'] == 'L':
        O5_lose += 1
O5_percentage = round((O5_win)/(O5_win+O5_lose),3)

W5_win = 0
W5_lose = 0
for i in range (2566):
    if df.loc[i, 'Wu_win_5'] == 'W':
        W5_win += 1
    elif df.loc[i, 'Wu_win_5'] == 'L':
        W5_lose += 1
W5_percentage = round((W5_win)/(W5_win+W5_lose),3)

st.title("Percentage")

left_column, middle_column, right_column, right_right_column = st.columns(4)

with left_column:
    st.subheader("Osbourn's win percentage/ Filter3")
    st.subheader(O3_percentage)

with middle_column:
    st.subheader("Wu's win percentage/ Filter3")
    st.subheader(W3_percentage)

with right_column:
    st.subheader("Osbourn's win percentage/ Filter5")
    st.subheader(O5_percentage)

with right_right_column:
    st.subheader("Wu's win percentage/ Filter5")
    st.subheader(W5_percentage)
#-----graph------
st.title(":bar_chart: Graph")
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
a = sns.countplot(data = df, x = 'O_win_3', color="skyblue", ax=axs[0, 0], order=df['O_win_3'].value_counts().index)
b = sns.countplot(data = df, x = 'Wu_win_3', color="olive", ax=axs[0, 1], order=df['Wu_win_3'].value_counts().index)
c = sns.countplot(data = df, x = 'O_win_5', color="gold", ax=axs[1, 0], order=df['O_win_5'].value_counts().index)
d = sns.countplot(data = df, x = 'Wu_win_5', color="teal", ax=axs[1, 1], order=df['Wu_win_5'].value_counts().index)

st.pyplot(a.get_figure())  

#-----2023data----
st.title(":bar_chart: Betting Dashboard")
st.dataframe(df)


