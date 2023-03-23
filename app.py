# Python file

import pandas as pd
import streamlit as st
import numpy as np
import altair as alt

from libraries import *

countries = ["USA", "Morocco", "France", "Germany", "Japan"]
data_types = ["cases", "deaths", "recovered"]

country = st.sidebar.selectbox("Pick a country", countries)
days = st.sidebar.slider("Select number of days", min_value=1, max_value=90)
data_type = st.sidebar.multiselect("Pick data types", data_types)

country_codes = {
    "USA": "us",
    "Morocco": "ma",
    "France": "fr",
    "Germany": "de",
    "Japan": "jp",
}

# total records
total_cases = get_historic_cases(country, str(days))
total_deaths = get_historic_deaths(country, str(days))
total_recovered = get_historic_recoveries(country, str(days))

total_df = pd.concat([total_cases, total_deaths, total_recovered], axis=1).astype(int)

# daily records

daily_cases = get_daily_cases(country, str(days))
daily_deaths = get_daily_deaths(country, str(days))
daily_recoveries = get_daily_recoveries(country, str(days))

daily_df = pd.concat([daily_cases, daily_deaths, daily_recoveries], axis=1).astype(int)

# yesterdqy records

yesterday_cases = get_yesterday_cases(country)
yesterday_deaths = get_yesterday_deaths(country)
yesterday_recoveries = get_yesterday_recoveries(country)


st.title("Covid 19 visualization Dashboard")
st.metric("Country", country)
st.image(f"https://flagcdn.com/80x60/{country_codes[country]}.png")  # type: ignore

col1, col2, col3 = st.columns(3)
col1.metric("Cases", yesterday_cases)
col2.metric("Deaths", yesterday_deaths)
col3.metric("Recoveries", yesterday_recoveries)

st.bar_chart(daily_df)
st.write(daily_df)

video_file = open("Covid.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://media.istockphoto.com/id/1308624310/photo/coronavirus-new-strain-wide-dark-background.jpg?b=1&s=170667a&w=0&k=20&c=k8Xnn0yPD8h76z-rcos-dfADP67PUkY8U7SxUxpqekI=");
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()