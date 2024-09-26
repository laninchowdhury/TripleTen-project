import streamlit as st
import pandas as pd
import plotly.express as px
import pandas as pd
df = pd.read_csv("C:\\Users\\nsuka\\Downloads\\vehicles_us.csv")

st.header('My Streamlit App')
df.columns
import streamlit as st
import plotly.express as px
fig = px.histogram(df, x='price')
st.plotly_chart(fig)

# Create scatter plot
fig = px.scatter(df, x= 'model_year', y='price', color = 'condition', size ='odometer', hover_data=['model'])

st.plotly_chart(fig)
import streamlit as st

# Checkbox to toggle visibility of 'price'
show_price = st.checkbox('Show Price')
price = 25000
model_year = 2020
model = 'Sedan'
condition = 'New'
cylinders = 4
fuel = 'Gasoline'
odometer = 15000
transmission = 'Automatic'
type = 'Car'
paint_color = 'Red'
is_4wd = True
date_posted = '2023-09-25'
days_listed = 30
if show_price:
    st.write(f"Price: ${price}")
st.write(f"Model Year: {model_year}")
st.write(f"Model: {model}")
st.write(f"Condition: {condition}")
st.write(f"Cylinders: {cylinders}")
st.write(f"Fuel: {fuel}")
st.write(f"Odometer: {odometer} miles")
st.write(f"Transmission: {transmission}")
st.write(f"Type: {type}")
st.write(f"Paint Color: {paint_color}")
st.write(f"4WD: {is_4wd}")
st.write(f"Date Posted: {date_posted}")
st.write(f"Days Listed: {days_listed}")