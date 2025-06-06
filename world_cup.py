import streamlit as st
import pandas as pd
import numpy as np

# --- Football Stats Section ---
st.set_page_config(layout="wide")
st.header("🏆 F+P World Cup 2025 🏆")

col1, col3 = st.columns([1,1], gap="small")  

# Generate some dummy data for football teams
group1 = {
    'Team': ['Maldives', 'Myanmar', 'Iceland', 'Solomon Islands'],
    'P': [0, 0, 0, 0],
    'W': [0, 0, 0, 0],
    'D': [0, 0, 0, 0],
    'L': [0, 0, 0, 0],
    'GF': [0, 0, 0, 0],
    'GA': [0, 0, 0, 0],
    'GD': [0, 0, 0, 0],
    'Points': [0, 0, 0, 0]
}


group2 = {
    'Team': ['Ireland', 'Italy', 'Fiji', 'Oman'],
    'P': [0, 0, 0, 0],
    'W': [0, 0, 0, 0],
    'D': [0, 0, 0, 0],
    'L': [0, 0, 0, 0],
    'GF': [0, 0, 0, 0],
    'GA': [0, 0, 0, 0],
    'GD': [0, 0, 0, 0],
    'Points': [0, 0, 0, 0]
}

group3 = {
    'Team': ['New Caledonia', 'Mongolia', 'Sweden', 'Andorra'],
    'P': [0, 0, 0, 0],
    'W': [0, 0, 0, 0],
    'D': [0, 0, 0, 0],
    'L': [0, 0, 0, 0],
    'GF': [0, 0, 0, 0],
    'GA': [0, 0, 0, 0],
    'GD': [0, 0, 0, 0],
    'Points': [0, 0, 0, 0]
}


group4 = {
    'Team': ['Venezula', 'Mexico', 'Bahamas', 'Colombia', 'India'],
    'P': [0, 0, 0, 0, 0],
    'W': [0, 0, 0, 0, 0],
    'D': [0, 0, 0, 0, 0],
    'L': [0, 0, 0, 0, 0],
    'GF': [0, 0, 0, 0, 0],
    'GA': [0, 0, 0, 0, 0],
    'GD': [0, 0, 0, 0, 0],
    'Points': [0, 0, 0, 0, 0]
}
df1 = pd.DataFrame(group1)
df2 = pd.DataFrame(group2)
df3 = pd.DataFrame(group3)
df4 = pd.DataFrame(group4)

# Sort by points for a league table feel
df1 = df1.sort_values(by='Points', ascending=False).reset_index(drop=True)
df2 = df2.sort_values(by='Points', ascending=False).reset_index(drop=True)
df3 = df3.sort_values(by='Points', ascending=False).reset_index(drop=True)
df4 = df4.sort_values(by='Points', ascending=False).reset_index(drop=True)
df1.index = df1.index + 1 # Start index from 1 for ranking
df2.index = df2.index + 1
df3.index = df3.index + 1
df4.index = df4.index + 1


with col1:
    st.subheader("Group 1")
    st.dataframe(df1, use_container_width=True)
    st.subheader("Group 3")
    st.dataframe(df3, use_container_width=True)
with col3:
    st.subheader("Group 2")
    st.dataframe(df2, use_container_width=True)
    st.subheader("Group 4")
    st.dataframe(df4, use_container_width=True)

st.write("---")

st.subheader("Fixtures T.B.C.")

