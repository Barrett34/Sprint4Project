import streamlit as st
import plotly.express as pex
import plotly.figure_factory as ff
import altair as al
import pandas as pd

st.header('Vehicle Sales US Data')

vehicles_df = pd.read_csv('/Users/barrett22/Desktop/Sprint_4_Project/Sprint4Project/vehicles_us.csv')
st.dataframe(vehicles_df)

mean_cost_by_model_yr = vehicles_df.groupby(['model_year']).agg(mean_price=('price','mean')).sort_index().sort_values(by='mean_price', ascending=False)
mean_price_by_yr_his = pex.histogram(mean_cost_by_model_yr, x = 'mean_price')
mean_price_by_model_yr_scatter = pex.scatter(mean_cost_by_model_yr, y="mean_price")


mean_cost_by_condition = vehicles_df.groupby('condition').agg(mean_price=('price','mean')).sort_index().sort_values(by='mean_price', ascending=False)
mean_price_by_condition_bar = pex.bar(mean_cost_by_condition, y="mean_price")




st.subheader('Mean Price By Model Year')

show_scatterplot = st.checkbox('Scatterplot', value=True)

if show_scatterplot:
    st.write(mean_price_by_model_yr_scatter)
else:
    st.write(mean_price_by_yr_his)


st.subheader("Mean Price by Condition Year")
st.write(mean_price_by_condition_bar)
