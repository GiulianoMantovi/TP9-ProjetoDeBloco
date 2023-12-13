import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(
    layout="wide",
    page_title="Regressão Linear - Uber Fares",
)

st.title("Regressão Linear - Uber Fares")

st.subheader("Dados Antes e Depois do Tratamento")

col1, col2 = st.columns(2)
with col1:
    st.header("Antes")
    uber_valid = pd.read_csv("uber_export.csv")
    fig1 = px.histogram(uber_valid, x="distance", labels={"distance": "Distância"})
    st.plotly_chart(fig1)

    fig3 = px.box(uber_valid, y="distance", labels={"distance": "Distância"})
    st.plotly_chart(fig3)

with col2:
    st.header("Depois")
    uber_100_km = pd.read_csv("uber_100_km_export.csv")
    fig2 = px.histogram(uber_100_km, x="distance", labels={"distance": "Distância"})
    st.plotly_chart(fig2)

    fig4 = px.box(uber_100_km, y="distance", labels={"distance": "Distância"})
    st.plotly_chart(fig4)
