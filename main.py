import streamlit as st
import plotly.express as px
import pandas as pd



st.title("In Search Of Happiness")

x_axis = st.selectbox("Select the data for the X-axis",("GDP", 
                                               "Happiness", "Generosity"))
y_axis = st.selectbox("Select the data for the X-axis",("Happiness", 
                                                        "GDP", "Generosity"))

st.subheader(f"{x_axis} and {y_axis}")

df = pd.read_csv("happy.csv")

match x_axis:
   case "Happiness":
      x_array = df["happiness"]
   case "GDP":
      x_axis = df["gdp"]
   case "Generosity":
      x_axis = df["generosity"]

match y_axis:
   case "Happiness":
      y_array = df["happiness"]
   case "GDP":
      y_axis = df["gdp"]
   case "Generosity":
      y_axis = df["generosity"]


fig = px.scatter(x=df[x_axis], y=df[y_axis], labels={"x": x_axis, "y": y_axis})
st.plotly_chart(fig)