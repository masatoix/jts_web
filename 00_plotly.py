import pandas as pd
import plotly_express as px
import streamlit as st

df = pd.read_excel('compare/test.xlsx')
st.write(df)

st.write(
    px.scatter(df, x='D-score', y='E-score', size='Flight', color='age', log_x=True, size_max=30)
)


df = px.data.gapminder()
st.write(df)

st.write(
    px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent", hover_name="country", log_x=True, size_max=60)
)