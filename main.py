import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search Of Happiness")

# Use separate variables for the selected options and the column names
selected_x_axis = st.selectbox("Select the data for the x-axis", ("GDP", "Happiness", "Generosity"))
selected_y_axis = st.selectbox("Select the data for the y-axis", ("Happiness", "GDP", "Generosity"))

st.subheader(f"{selected_x_axis} and {selected_y_axis}")

df = pd.read_csv("happy.csv")

# Corrected assignment of columns based on the selected options
if selected_x_axis == "Happiness":
    x_column = "happiness"
elif selected_x_axis == "GDP":
    x_column = "gdp"
else:  # Generosity
    x_column = "generosity"

if selected_y_axis == "Happiness":
    y_column = "happiness"
elif selected_y_axis == "GDP":
    y_column = "gdp"
else:  # Generosity
    y_column = "generosity"

fig = px.scatter(x=df[x_column], y=df[y_column], labels={"x": selected_x_axis, "y": selected_y_axis})
st.plotly_chart(fig)
